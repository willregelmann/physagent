import numpy as np
from scipy.integrate import solve_ivp
from ccaps import *
e=1.0
def y0_C(c3,e,t0,C):
    y=y0_of(c3,e,t0); y[4]=C*t0; return y
def cap_real_C(c3,q1,C,tmax=60.0):
    hit=lambda s,Y: (Y[0]**2-q1).real; hit.terminal=True; hit.direction=1
    y=y0_C(c3,e,2e-3,C); dz=tmax-2e-3
    sol=solve_ivp(lambda s,Y: dz*dens(Y,e),(0,1),y,method='DOP853',rtol=1e-10,atol=1e-13,events=[hit])
    if len(sol.t_events[0])==0: return None
    return sol.y_events[0][0]
print("(1) flat-space cap (c3=0) cut at a^2=q1: action vs q1 (C=1 frame); I_loc should be -(3/4) q1")
for q1 in (0.4,1,4,10,40,100):
    Y=cap_real_C(0.0,q1,1.0); print(f"  q1={q1:6.1f}: I_loc={Y[5].real:+.4f}  Gamma={Y[6].real:+.4f}  I_tot={(Y[5]+Y[6]).real:+.4f}  theta1={Y[4].real:.4f}  R1={Rf(Y[0],Y[1],Y[2]).real:+.2e}")
print("(2) location of the critical point of I(c3) at q1=4 on the real branch, in frames C=0.3,1,3 (fine grid):")
c3s=np.arange(-0.02,0.0301,0.002)
for C in (0.3,1.0,3.0):
    Is=[]; 
    for c3 in c3s:
        Y=cap_real_C(c3,4.0,C); Is.append((Y[5]+Y[6]).real if Y is not None else np.nan)
    Is=np.array(Is); d=np.gradient(Is,c3s); sc=np.where(np.sign(d[:-1])*np.sign(d[1:])<0)[0]
    print(f"  C={C}: I at c3=-0.02..0.03:",[f"{v:+.3f}" for v in Is[::5]]," dI/dc3 sign change between",[(round(c3s[i],3),round(c3s[i+1],3)) for i in sc])
