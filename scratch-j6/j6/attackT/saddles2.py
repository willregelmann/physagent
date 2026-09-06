import numpy as np, pickle, sys
exec(open('complexcaps.py').read().split("e=1.0; a1=3.0")[0])
from scipy.integrate import solve_ivp
def shoot2(c3,T,e,s0=1e-3):
    C5,C7=c5f(c3,e),c7f(c3,e); t0=s0*T
    y0=np.array([t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4, 0.0],dtype=complex)
    ss=np.linspace(1e-6,1,200)*t0; aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y0[4]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    def rhs(s,y):
        A,B,C,D,I=y
        return T*np.array([B,C,D,FE(A,B,C,D,e),2*np.pi**2*Lreg(A,B,C,e)/A],dtype=complex)
    small=lambda s,y: abs(y[0])-0.02; small.terminal=True; small.direction=-1
    big=lambda s,y: abs(y[0])-40.0; big.terminal=True
    sol=solve_ivp(rhs,(s0,1.0),y0,method='DOP853',rtol=1e-9,atol=1e-12,events=[small,big])
    if sol.status!=0 or len(sol.t_events[0]) or len(sol.t_events[1]): return None
    return sol.y[:,-1]
def Tnewton(c3,T,e,a1,it=25):
    y=None
    for k in range(it):
        y=shoot2(c3,T,e)
        if y is None: return None,None
        f=y[0]-a1
        if abs(f)<1e-11: return T,y
        dT=-f/y[1]
        if abs(dT)>1.0: dT=dT/abs(dT)
        T=T+dT
    return (T,y) if (y is not None and abs(y[0]-a1)<1e-8) else (None,None)
def find(c3,T,e,a1,K1,it=30):
    for k in range(it):
        T,y=Tnewton(c3,T,e,a1)
        if T is None: return None
        g=y[1]-K1
        if abs(g)<1e-9: return (c3,T,y[4],Rf(y[0],y[1],y[2]),y[1])
        h=1e-6
        T2,y2=Tnewton(c3+h,T,e,a1)
        if T2 is None: return None
        dg=(y2[1]-K1-g)/h
        dc=-g/dg
        if abs(dc)>0.1: dc=0.1*dc/abs(dc)
        c3=c3+dc
    return None
e=1.0; a1=3.0; Tsph=np.pi/2+1j*np.arccosh(a1); K1=np.cos(Tsph)
print("sphere check:",shoot2(-1/6,Tsph,e)[[0,1,4]],flush=True)
for label,data in (("dS-history data (a1=3, K1=-i sqrt8)",(3.0,K1)),("conjugate branch (a1=3, K1=+i sqrt8)",(3.0,np.conj(K1))),("double-bubble neck data (a1=0.5585, K1=0)",(0.5585,0.0)),("real Euclidean data (a1=3, K1=+2.0)",(3.0,2.0))):
    a1_,K1_=data; sols=[]
    print(f"\n=== saddles for {label} ===",flush=True)
    c3grid=(-0.5,-0.35,-0.25,-1/6,-0.1,0.0,0.1,0.3)
    Tgrid=(np.pi/2+1.76j,np.pi/2-1.76j,1.0+2.0j,2.2+1.0j,0.7+2.5j,2.5-1.5j,0.6,1.5,2.1)
    for c30 in c3grid:
        for T0 in Tgrid:
            r=find(c30,T0,e,a1_,K1_)
            if r is None: continue
            c3,T,I,Rv,ap=r
            if all(abs(c3-s[0])>1e-5 or abs(T-s[1])>1e-5 for s in sols):
                sols.append(r); print(f"  c3={c3:.6f}  T={T:.6f}  I/a={I:.5f}  R(T)={Rv:.4f}  a'(T)={ap:.5f}",flush=True)
    pickle.dump(sols,open(f'saddles_{label[:2]}.pkl','wb'))
print("\n=== double bubble c3*=-0.349489: complex continuations to a=3 ===",flush=True)
for T0 in (2.106+1.5j,2.106-1.5j,2.106+2.5j,1.0+1.5j,3.0+1.0j,0.8+2.5j,1.5+1.0j):
    T,y=Tnewton(-0.349489,T0,e,3.0)
    if T is None: print(f"  T0={T0:.3f}: no convergence",flush=True); continue
    print(f"  T0={T0:.3f}: T={T:.5f}  a'(T)={y[1]:.5f} (dS data: {K1:.4f})  R(T)={Rf(y[0],y[1],y[2]):.4f}  I/a={y[4]:.5f}",flush=True)
