# Open (pole) continuation of the symmetric double bubble at other eps: runaway generic?
import numpy as np
from scipy.integrate import solve_ivp
from ccaps import FE, Rf, c5f, c7f
for e,c3 in ((0.5,-0.354147),(2.0,-0.342261),(5.0,-0.337009)):
    C5,C7=c5f(c3,e),c7f(c3,e); t0=2e-3; tau0=1j*t0
    y0=np.array([tau0+c3*tau0**3+C5*tau0**5+C7*tau0**7, 1+3*c3*tau0**2+5*C5*tau0**4+7*C7*tau0**6, 6*c3*tau0+20*C5*tau0**3+42*C7*tau0**5, 6*c3+60*C5*tau0**2+210*C7*tau0**4],dtype=complex)
    rhs=lambda t,y: 1j*np.array([y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e)],dtype=complex)
    big=lambda t,y: abs(Rf(y[0],y[1],y[2]))-1e5; big.terminal=True
    small=lambda t,y: abs(y[0])-1e-3; small.terminal=True; small.direction=-1
    s=solve_ivp(rhs,(t0,40),y0,method='DOP853',rtol=1e-10,atol=1e-13,events=[big,small],dense_output=True)
    print(f"eps={e}: c3*={c3}: stopped t={s.t[-1]:.3f} (status {s.status}; R>1e5 hit: {len(s.t_events[0])>0}, a->0 hit: {len(s.t_events[1])>0})")
    for t in np.linspace(0.5,s.t[-1],7):
        y=s.sol(t); a=y[0].imag; H=y[1].real/a; R=Rf(y[0],y[1],y[2])
        print(f"   t={t:6.3f}  a={a:.3e}  H={H:+.4f}  R={R.real:+.4e}  |Re b|={abs(y[0].real):.1e}")
