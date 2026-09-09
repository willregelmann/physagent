# R-marginal saddles of Psi(a,R): P_R = -(eps/4) a^2 v = 0  <=>  v = 0 cuts (K = 0).  For each a_target find the real regular cap whose
# maximum radius is a_target (turning point v=0), and its I_(a,R) = I_inv (boundary term vanishes at v=0); compare with the sphere's
# de Sitter branch Re I = -(1+2 eps) at the same a, and with the flat ball's I_inv at that a.
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
from scipy.optimize import brentq
def amax_and_tau(c3,e):
    ext=lambda s,Y: Y[1].real; ext.direction=-1; ext.terminal=True
    stop=lambda s,Y: Y[0].real-0.02; stop.terminal=True; stop.direction=-1
    y,sols=integrate_path(c3,e,[14.0],events=[ext,stop],dense=True); z0,dz,sol=sols[0]
    if len(sol.t_events[0])==0: return None,None
    s=sol.t_events[0][0]; Y=sol.sol(s); return Y[0].real,(z0+s*dz).real
def Iinv_at(c3,e,t1):
    C=sym_C(c3,e,[t1]); y=run_path(c3,e,[t1],C); v=y[1]; R=Rf(y[0],y[1],y[2])
    return (y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*v**3).real, y[0].real, v.real, R.real
for e in (1.0,0.3):
    print(f"=== eps={e}: turning-point (K=0) caps with maximum radius a_t; I_(a,R)=I_inv there; sphere dS Re I=-(1+2eps)={-(1+2*e):+.3f} ===")
    for at in (1.0,1.2,1.5,2.0,3.0,4.0,6.0):
        try:
            f=lambda c3: (amax_and_tau(c3,e)[0] or 1e9)-at
            lo,hi=-1/6+1e-6,-1e-5
            flo,fhi=f(lo),f(hi)
            if flo*fhi>0: print(f"  a_t={at}: no bracket (f(lo)={flo:.3f}, f(hi)={fhi:.3f})"); continue
            c3=brentq(f,lo,hi,xtol=1e-10)
            am,t1=amax_and_tau(c3,e); Ii,a1,v1,R1=Iinv_at(c3,e,t1)
            # flat ball at the same a: c3=0, tau=a
            If,_,_,_=Iinv_at(0.0,e,at)
            print(f"  a_t={at:4.1f}: c3={c3:+.6f} tau_turn={t1:.4f} a={a1:.4f} v={v1:+.1e} R={R1:+.4f} | I_(a,R)=I_inv={Ii:+.4f} | flat ball I_inv={If:+.4f} | sphere dS {-(1+2*e):+.3f}",flush=True)
        except Exception as ex: print(f"  a_t={at}: fail {ex}")
