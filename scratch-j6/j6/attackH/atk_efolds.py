import numpy as np
from scipy.integrate import solve_ivp
from ccaps import FE, Rf, c5f, c7f
# semiclassical thresholds at a2=1e6: H0/M_P = sqrt(180 pi/a2); R <= Mbar_P^2  <=> R/H0^2 <= 8pi/(180pi/a2) ; R <= M_P^2 <=> R/H0^2 <= a2/(180 pi)
a2=1e6; thrM=a2/(180*np.pi); thrMbar=thrM/(8*np.pi)
print(f"a2=1e6: R/H0^2 thresholds: M_P^2 -> {thrM:.0f}, Mbar_P^2 -> {thrMbar:.1f} (sphere has R=12)")
for e,c3 in ((1.0,-0.349489),(2.0,-0.342261),(5.0,-0.337009),(10.0,-0.335180)):
    C5,C7=c5f(c3,e),c7f(c3,e); t0=2e-3; tau0=1j*t0
    y0=np.array([tau0+c3*tau0**3+C5*tau0**5+C7*tau0**7, 1+3*c3*tau0**2+5*C5*tau0**4+7*C7*tau0**6, 6*c3*tau0+20*C5*tau0**3+42*C7*tau0**5, 6*c3+60*C5*tau0**2+210*C7*tau0**4],dtype=complex)
    rhs=lambda t,y: 1j*np.array([y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e)],dtype=complex)
    evM=lambda t,y: Rf(y[0],y[1],y[2]).real-thrM; evM.terminal=False
    evMb=lambda t,y: Rf(y[0],y[1],y[2]).real-thrMbar; evMb.terminal=False
    big=lambda t,y: abs(Rf(y[0],y[1],y[2]))-1e6; big.terminal=True
    s=solve_ivp(rhs,(t0,80),y0,method='DOP853',rtol=1e-10,atol=1e-13,events=[evMb,evM,big],dense_output=True)
    out=[]
    for k,lab in ((0,'R=Mbar_P^2'),(1,'R=M_P^2')):
        if len(s.t_events[k]): 
            tt=s.t_events[k][0]; y=s.y_events[k][0]; out.append(f"{lab}: t={tt:.2f}, ln a={np.log(y[0].imag):.1f}, H={y[1].real/y[0].imag:.2f}")
    # H at ln a = 5 and 20 for flavour
    ts=np.linspace(0.5,s.t[-1],4000); Y=s.sol(ts); lna=np.log(Y[0].imag); Hs=Y[1].real/Y[0].imag
    hs=[f"ln a={L}: H={np.interp(L,lna,Hs):.2f}" for L in (5,20,50) if L<lna[-1]]
    print(f"eps={e}: open branch; "+"; ".join(out)+"; runaway (R=1e6) at t={s.t[-1]:.2f}, ln a={np.log(s.y[0,-1].imag):.0f}; "+", ".join(hs))
