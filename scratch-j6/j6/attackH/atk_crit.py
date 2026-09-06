# Attack check: critical points of I(c3) at fixed q1 on the REAL-Euclidean branch (caps reaching a^2=q1 in real tau),
# which the position's qfam grid stops at c3=0.02 / straddles with a branch jump.
import numpy as np
from ccaps import *
e=1.0
def cap_real(c3,q1,tmax=30.0):
    hit=lambda z,Y: (Y[0]**2-q1).real; hit.terminal=True; hit.direction=1
    ext=lambda z,Y: Y[1].real; ext.direction=-1; ext.terminal=True   # stop at a peak (cap fails to reach q1)
    y,sols=integrate_path(c3,e,[tmax],events=[hit,ext],dense=False)
    z0,dz,sol=sols[0]
    if len(sol.t_events[0])==0: return None
    Y=sol.y_events[0][0]; tau1=(z0+sol.t_events[0][0]*dz).real
    return tau1,Y
for q1 in (4.0,0.4):
    print(f"=== q1={q1}: real-Euclidean branch, I = I_loc + Gamma (C=1 frame), plus I_loc alone")
    c3s=np.arange(-0.04,0.4001,0.01)
    rows=[]
    for c3 in c3s:
        r=cap_real(c3,q1)
        if r is None: print(f" c3={c3:+.3f}: does not reach q1 in real tau"); continue
        tau1,Y=r; I=(Y[5]+Y[6]).real; Il=Y[5].real; R1=Rf(Y[0],Y[1],Y[2]).real; K=(Y[1]/Y[0]).real
        rows.append((c3,tau1,I,Il,R1,K,Y[7].real))
    rows=np.array(rows)
    dI=np.gradient(rows[:,2],rows[:,0]); dIl=np.gradient(rows[:,3],rows[:,0])
    print("   c3     tau1     I_tot     dI/dc3    I_loc    dIloc/dc3   R1      K1      N_E")
    for r,d1,d2 in zip(rows,dI,dIl):
        print(f" {r[0]:+.3f}  {r[1]:.4f}  {r[2]:+.5f}  {d1:+.4f}  {r[3]:+.5f}  {d2:+.4f}  {r[4]:+.3f}  {r[5]:+.4f}  {r[6]:.4f}")
    sc=np.where(np.sign(dI[:-1])*np.sign(dI[1:])<0)[0]
    print("  sign changes of dI_tot/dc3 between c3 =",[(round(rows[i,0],3),round(rows[i+1,0],3)) for i in sc])
    sc=np.where(np.sign(dIl[:-1])*np.sign(dIl[1:])<0)[0]
    print("  sign changes of dI_loc/dc3 between c3 =",[(round(rows[i,0],3),round(rows[i+1,0],3)) for i in sc])
