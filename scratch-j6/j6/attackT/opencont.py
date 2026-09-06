# Hawking-Turok-type open continuation: a(t) = -i b(i t), b the Euclidean regular cap. Integrate the Euclidean ODE along tau = i t from the pole.
import numpy as np, pickle
from scipy.integrate import solve_ivp
from ccaps import FE, Rf, c5f, c7f
def open_hist(c3,e,T=25.0,t0=2e-3):
    C5,C7=c5f(c3,e),c7f(c3,e)
    tau0=1j*t0
    b=[tau0+c3*tau0**3+C5*tau0**5+C7*tau0**7, 1+3*c3*tau0**2+5*C5*tau0**4+7*C7*tau0**6, 6*c3*tau0+20*C5*tau0**3+42*C7*tau0**5, 6*c3+60*C5*tau0**2+210*C7*tau0**4]
    y0=np.array(b,dtype=complex)
    def rhs(t,y): return 1j*np.array([y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e)],dtype=complex)
    stop=lambda t,y: abs(y[0])-1e-3; stop.terminal=True; stop.direction=-1
    grow=lambda t,y: abs(y[0])-1e4; grow.terminal=True
    s=solve_ivp(rhs,(t0,T),y0,method='DOP853',rtol=1e-10,atol=1e-13,events=[stop,grow],dense_output=True)
    return s
e=1.0
for c3,lab in ((-1/6,'sphere -> open de Sitter (expect a=sinh t, R=12)'),(-0.349489,'double bubble (eps=1)')):
    s=open_hist(c3,e)
    print(f"=== {lab}")
    print("   t      a=Im b       Re b (should be 0)   H=adot/a    addot/a     R")
    ts=list(np.arange(0.5,min(s.t[-1],25)+1e-9,0.5))
    N_acc=0.0
    for t in ts:
        y=s.sol(t); b0,b1,b2=y[0],y[1],y[2]
        a=b0.imag; adot=b1.real; addot=-b2.imag   # a=-i b(it): adot = -i * i b' = b', addot = i b''... careful: d/dt[-i b(it)] = -i*i*b'(it)= b'(it); d2 = i b''(it)
        addot=(1j*b2).real
        Rv=Rf(b0,b1,b2)  # scalar curvature of the Euclidean metric at complex tau = that of the Lorentzian open metric (analytic continuation)
        print(f" {t:5.1f} {a:12.5f} {b0.real:+.1e}          {adot/a:+.5f}   {addot/a:+.5f}   {Rv.real:+.4f}{Rv.imag:+.1e}i")
    print(f"   ended at t={s.t[-1]:.3f}, status={s.status}, |a|={abs(s.y[0,-1]):.3e}")
    # e-folds of acceleration
    tt=np.linspace(s.t[0],s.t[-1],4000); Y=s.sol(tt); a=Y[0].imag; add=(1j*Y[2]).real
    acc=add>0
    if acc.any():
        i1=np.argmax(acc); 
        # last accelerating index
        i2=len(acc)-1-np.argmax(acc[::-1])
        print(f"   accelerating (addot>0) from t={tt[i1]:.3f} to t={tt[i2]:.3f}; ln(a2/a1)={np.log(a[i2]/a[i1]):.3f} e-folds")
