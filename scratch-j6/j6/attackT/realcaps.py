import numpy as np, sys
exec(open('complexcaps.py').read().split("e=1.0; a1=3.0")[0])
from scipy.integrate import solve_ivp
e=1.0
def realcap(c3,e,a1=3.0,t0=2e-3):
    C5,C7=c5f(c3,e),c7f(c3,e)
    y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4, 0.0]
    ss=np.linspace(1e-6,1,200)*t0; aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y0[4]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    def rhs(s,y):
        A,B,C,D,I=y
        return [B,C,D,FE(A,B,C,D,e),2*np.pi**2*Lreg(A,B,C,e)/A]
    hit=lambda s,y: y[0]-a1; hit.terminal=True; hit.direction=1
    turn=lambda s,y: y[1]; turn.terminal=True; turn.direction=-1
    sol=solve_ivp(rhs,(t0,60),y0,method='DOP853',rtol=1e-10,atol=1e-13,events=[hit,turn])
    if len(sol.t_events[0]): return sol.t_events[0][0],sol.y_events[0][0]
    return None,(sol.y_events[1][0] if len(sol.t_events[1]) else None)
print("c3        T(a=3)     K1=a'(T)   R(T)        I/a         [a_max if never reaches 3]")
for c3 in (-0.16,-0.1,-0.05,-0.02,-0.01,-0.005,0.0,0.01,0.05,0.1,0.3,1.0,3.0,10.0):
    T,y=realcap(c3,e)
    if T is None: print(f"{c3:+.3f}   never reaches 3; a_max={y[0] if y is not None else float('nan'):.4f}"); continue
    print(f"{c3:+.3f}   {T:8.4f}   {y[1]:8.4f}   {Rf(y[0],y[1],y[2]):9.4f}   {y[4]:10.4f}")
