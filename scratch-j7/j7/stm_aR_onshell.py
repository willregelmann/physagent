# STEELMAN flaw 6: the on-shell fixed-(a,R) action of the real regular caps at a=2, at each cap's OWN R:
#   I_(a,R)(cap) = I_inv - (eps/4) a^2 R v = I_inv - eps R v   (a=2).
# Along the family dI_(a,R)/dv = -v dQ/dv = -eps v dR/dv, so it is stationary exactly at v=0 (the K=0 turning-point cap).
# Locate the K=0 cap (a_max = 2), scan v finely around it, and confirm (i) the minimum is at v=0, (ii) the family is bounded below,
# (iii) both ends -> +inf, at eps=1 and 0.3.  Also P_R at the flat ball.
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
from scipy.optimize import brentq
def crossings(c3,e,a1=2.0,tmax=14.0):
    hit=lambda s,Y: Y[0].real-a1; hit.direction=0
    stop1=lambda s,Y: Y[0].real-0.02; stop1.terminal=True; stop1.direction=-1
    stop2=lambda s,Y: Y[0].real-60.0; stop2.terminal=True
    y,sols=integrate_path(c3,e,[tmax],events=[hit,stop1,stop2],dense=True)
    z0,dz,sol=sols[0]
    return [(z0+s*dz).real for s in sol.t_events[0]]
def amax(c3,e,tmax=14.0):
    ext=lambda s,Y: Y[1].real; ext.direction=-1; ext.terminal=True
    stop1=lambda s,Y: Y[0].real-0.02; stop1.terminal=True; stop1.direction=-1
    y,sols=integrate_path(c3,e,[tmax],events=[ext,stop1],dense=True)
    z0,dz,sol=sols[0]
    if len(sol.t_events[0]): return sol.y_events[0][0][0].real,(z0+sol.t_events[0][0]*dz).real
    return np.nan,np.nan
def row(c3,e,tau1):
    C=sym_C(c3,e,[tau1]); y=run_path(c3,e,[tau1],C); A,vv=y[0].real,y[1].real; R=Rf(y[0],y[1],y[2]).real
    Iinv=(y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*y[1]**3).real
    return A,vv,R,Iinv,Iinv-(e/4)*A**2*R*vv
for e in (1.0,0.3):
    # K=0 cap: c3 with a_max=2
    c3k=brentq(lambda c: amax(c,e)[0]-2.0,-0.06,-0.005,xtol=1e-10)
    tk=amax(c3k,e)[1]
    A,vv,R,Iinv,IaR=row(c3k,e,tk)
    print(f"=== eps={e}: K=0 cap at a=2: c3={c3k:.7f} tau1={tk:.5f} a={A:.5f} v={vv:+.2e} R={R:.4f} I_inv={Iinv:+.5f}  I_(a,R)={IaR:+.5f}  (P_R=-(eps/4)a^2 v = {-(e/4)*A**2*vv:+.2e})")
    rows=[]
    # scan c3 from the K=0 cap toward 0 (both crossings) and c3>0 (expanding only)
    grid=list(c3k+np.geomspace(1e-5,abs(c3k)*0.999,22))+[0.0]+list(np.geomspace(1e-4,0.05,8))
    for c3 in grid:
        try: cr=crossings(c3,e)
        except Exception as ex: continue
        for k,t1 in enumerate(cr[:2]):
            try: A,vv,R,Iinv,IaR=row(c3,e,t1)
            except Exception: continue
            rows.append((vv,c3,R,Iinv,IaR))
    rows.sort()
    print("      v        c3          R        I_inv     I_(a,R)@own R    (E_HH at R_t=12 = -I_inv+eps*12*v, for contrast)")
    for vv,c3,R,Iinv,IaR in rows:
        if abs(vv)<1.6: print(f"   {vv:+8.4f}  {c3:+.6f}  {R:+9.4f}  {Iinv:+9.4f}   {IaR:+9.4f}        {-Iinv+e*12*vv:+9.4f}")
    m=min(rows,key=lambda r:r[4])
    print(f"   minimum of I_(a,R) on the scanned family: {m[4]:+.5f} at v={m[0]:+.4f} (R={m[2]:.4f}); K=0 cap value {IaR:+.5f}")
    print(f"   ends: v={rows[0][0]:+.3f} -> I_(a,R)={rows[0][4]:+.2f};  v={rows[-1][0]:+.3f} -> I_(a,R)={rows[-1][4]:+.2f}")
    # second derivative at v=0: -eps dR/dv
    near=[r for r in rows if abs(r[0])<0.3]
    if len(near)>3:
        vv=np.array([r[0] for r in near]); RR=np.array([r[2] for r in near]); II=np.array([r[4] for r in near])
        pR=np.polyfit(vv,RR,2); pI=np.polyfit(vv,II,2)
        print(f"   fit near v=0: dR/dv={pR[1]:+.4f}  ->  -eps dR/dv={-e*pR[1]:+.4f};  fitted d^2 I_(a,R)/dv^2 = {2*pI[0]:+.4f}; fitted dI/dv at 0 = {pI[1]:+.2e}")
# flat ball: P_R
print("flat ball (v=1, R=0) at a=2: boundary term -vQ = -(eps/4)a^2 R v = 0 ; P_R = -(eps/4) a^2 v = -eps (eps=1: -1) != 0")
