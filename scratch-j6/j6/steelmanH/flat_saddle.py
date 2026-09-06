import numpy as np, sys
sys.path.insert(0,'..')
from ccaps import *
e=1.0
def cap_real(c3,q1,tmax=40.0):
    hit=lambda z,Y: (Y[0]**2-q1).real; hit.terminal=True; hit.direction=1
    ext=lambda z,Y: Y[1].real; ext.direction=-1; ext.terminal=True
    y,sols=integrate_path(c3,e,[tmax],events=[hit,ext]); z0,dz,sol=sols[0]
    if len(sol.t_events[0])==0: return None
    return (z0+sol.t_events[0][0]*dz).real, sol.y_events[0][0]
kap=-(3*e+1)/(288*np.pi**2)
print("(1) Ostrogradsky momentum p_{a'} = dL_tau/da'' = (1/4pi^2) a a'' - 72 kappa (1 - a a'' - a'^2) at the cut, along the real family at q1=4, and I(c3):")
print("   c3      tau1     I_tot(C=1)   I_loc     Gamma    R1       K1      p_{a'}   Im I")
rows=[]
for c3 in np.concatenate([np.arange(-0.03,0.0301,0.002),[0.05,0.1,0.2,0.3]]):
    r=cap_real(c3,4.0)
    if r is None: print(f" {c3:+.3f}: does not reach q1=4 in real tau"); continue
    tau1,Y=r; A,A1,A2=Y[0].real,Y[1].real,Y[2].real
    pa=(1/(4*np.pi**2))*A*A2-72*kap*(1-A*A2-A1**2)
    I=(Y[5]+Y[6]); rows.append((c3,tau1,I.real,Y[5].real,Y[6].real,Rf(Y[0],Y[1],Y[2]).real,A1/A,pa,I.imag))
    print(f" {c3:+.3f}  {tau1:.4f}  {I.real:+.5f}  {Y[5].real:+.5f}  {Y[6].real:+.5f}  {Rf(Y[0],Y[1],Y[2]).real:+.3f}  {A1/A:+.4f}  {pa:+.5f}  {I.imag:+.1e}")
rows=np.array(rows); fine=rows[np.abs(rows[:,0])<=0.031]
dI=np.gradient(fine[:,2],fine[:,0]); dIl=np.gradient(fine[:,3],fine[:,0])
def zero(x,d):
    sc=np.where(np.sign(d[:-1])*np.sign(d[1:])<0)[0]
    return [x[i]-d[i]*(x[i+1]-x[i])/(d[i+1]-d[i]) for i in sc]
print("  zero of dI_tot/dc3 (C=1) at c3 =",zero(fine[:,0],dI),"; zero of dI_loc/dc3 at c3 =",zero(fine[:,0],dIl))
print("(2) flat cap c3=0: I_loc vs -(3/4) q1, Gamma(C=1), Im I (phase): ")
for q1 in (0.4,1.0,4.0,9.0,25.0,100.0):
    tau1,Y=cap_real(0.0,q1,tmax=60.0); print(f"   q1={q1:6.1f}: I_loc={Y[5].real:+.4f} (-(3/4)q1={-0.75*q1:+.4f})  Gamma={Y[6].real:+.4f}  Im I={(Y[5]+Y[6]).imag:+.1e}  a'={Y[1].real:.4f} (Euclidean K=3a'/a real => non-classical data)")
print("(3) weights: sphere K=0 history e^{-2 I_R}, I_R=I_S4/2=-(5/3+2eps) => exponent +(10/3+4eps) a; Milne (flat space through its pole) I_R=0 => exponent 0.  Ratio sphere/Milne = e^{+%.3f a}"%(10/3+4*e))
