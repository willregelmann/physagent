import numpy as np
from scipy.integrate import solve_ivp
from ccaps import FE, Rf, c5f, c7f
e=1.0
for c3,lab in ((-0.349489,'DB eps=1'),):
    C5,C7=c5f(c3,e),c7f(c3,e); t0=2e-3; tau0=1j*t0
    y0=np.array([tau0+c3*tau0**3+C5*tau0**5+C7*tau0**7, 1+3*c3*tau0**2+5*C5*tau0**4+7*C7*tau0**6, 6*c3*tau0+20*C5*tau0**3+42*C7*tau0**5, 6*c3+60*C5*tau0**2+210*C7*tau0**4],dtype=complex)
    rhs=lambda t,y: 1j*np.array([y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e)],dtype=complex)
    big=lambda t,y: abs(Rf(y[0],y[1],y[2]))-1e6; big.terminal=True
    s=solve_ivp(rhs,(t0,20),y0,method='DOP853',rtol=1e-10,atol=1e-13,events=[big],dense_output=True)
    print(lab,"stopped at t=",s.t[-1],"status",s.status)
    for t in np.linspace(4.5,s.t[-1],8):
        y=s.sol(t); a=y[0].imag; H=y[1].real/a; R=Rf(y[0],y[1],y[2]).real
        print(f"  t={t:.4f} ln a={np.log(a):.3f} H={H:.4f} R={R:.4e}  (1/H... R^-1/2 = {R**-0.5:.3e})")
