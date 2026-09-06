import numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import brentq
src=open('caps.py').read().split("res={}")[0]; exec(src)
e=1.0; a1=3.0
def cap_to_a1(c3):
    C5,C7=c5f(c3,e),c7f(c3,e); t0=2e-3
    y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4]
    hit=lambda t,y,ee: y[0]-a1; hit.terminal=True; hit.direction=1
    s=solve_ivp(rhsE,(t0,60),y0,args=(e,),method='DOP853',rtol=1e-10,atol=1e-13,events=[hit],dense_output=True)
    if len(s.t_events[0])==0: return None
    T=s.t_events[0][0]; ts=np.linspace(t0,T,200001); Y=s.sol(ts); A,A1,A2,A3=Y[0],Y[1],Y[2],Y[3]
    EH_bulk=2*np.pi**2*trapezoid((-(6/(16*np.pi**2))*A**2*(1+A1**2))/A,ts)      # bulk EH piece (with the by-parts form used in J-1, valid for closed caps; for cut caps the GH term differs -- report both)
    R2=2*np.pi**2*trapezoid((36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2-A1**2)**2)/A,ts)
    R_T=-6*(A[-1]*A2[-1]+A1[-1]**2-1)/A[-1]**2
    # proper EH action of a cut cap: -(1/16piG) Int sqrt(g) R - (1/8piG) oint sqrt(h) K, per a with 1/G = a/pi:
    Rt=-6*(A*A2+A1**2-1)/A**2; bulk=-(1/(16*np.pi))*2*np.pi**2*trapezoid(Rt*A**3,ts)*(1/np.pi)   # per a: (a/pi)*... -> divide: -(a/pi)/(16 pi) * 2pi^2 Int R a^3 = -(a/8) Int R a^3
    bulk=-(1/8)*trapezoid(Rt*A**3,ts); GH=-(1/8)*2*np.pi**2*(3*A1[-1]/A[-1])*A[-1]**3/np.pi**2*(1/2)  # K = 3 a'/a on the S^3 of radius a; (1/8piG) oint sqrt(h) K = (a/(8 pi^2)) * 2 pi^2 a^3 * 3a'/a
    GH=-(1/8)*2*3*A1[-1]*A[-1]**2*0 - (3/4)*A1[-1]*A[-1]**2*0  # placeholder, computed explicitly below
    GH=-(1/(8*np.pi))*(1/np.pi)*2*np.pi**2*(3*A1[-1]/A[-1])*A[-1]**3   # = -(3/4) a1^2 a'(T)  per a
    return dict(T=T,K1=A1[-1],R_T=R_T,R2=R2,EH_byparts=EH_bulk,EH_bulk=bulk,GH=GH,EH_total=bulk+GH)
print(f"eps={e}, a1={a1}: local (scheme-independent) pieces per a; flat ball check at c3=0: expect EH_total = -(3/4) a1^2 = -6.75, R2 = 0")
for c3 in (-1/6,-0.005,0.0,0.05,0.1,0.3,1.0):
    r=cap_to_a1(c3)
    if r is None: print(f"c3={c3:+.4f}: does not reach a1"); continue
    print(f"c3={c3:+.4f}: T={r['T']:.3f} K1=a'(T)={r['K1']:+.3f} R(T)={r['R_T']:+.2f} | EH bulk={r['EH_bulk']:+.3f} GH={r['GH']:+.3f} EH total={r['EH_total']:+.3f} | R2 piece={r['R2']:+.3f} | EH+R2={r['EH_total']+r['R2']:+.3f}")
