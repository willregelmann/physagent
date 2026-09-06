# Family of regular caps cut at a^2 = q1, over complex c3; N = int a dtau, I = bulk action (no boundary term), R1 at the cut.
import numpy as np, pickle, sys
from ccaps import *
e=1.0
def cap_at(c3,tau1):
    # path: real axis to min(Re tau1, tau_r) then straight to tau1
    tr=min(max(tau1.real,0.05),3.0)
    path=[tr] if abs(tau1.imag)<1e-14 and abs(tau1.real-tr)<1e-14 else [tr,tau1]
    y,_=integrate_path(c3,e,path); return y
def solve_tau1(c3,q1,tau_guess,maxit=40):
    tau=complex(tau_guess)
    for it in range(maxit):
        y=cap_at(c3,tau); f=y[0]**2-q1; df=2*y[0]*y[1]
        if abs(df)<1e-14: return None,None
        step=-f/df
        if abs(step)>0.5: step*=0.5/abs(step)
        tau=tau+step
        if abs(step)<1e-11: 
            y=cap_at(c3,tau); return tau,y
    return None,None
def scan(q1,tau_seed,c3_re,c3_im,fname):
    nr,ni=len(c3_re),len(c3_im); T=np.full((ni,nr),np.nan+0j); Y=np.full((ni,nr,8),np.nan+0j)
    # continuation: start from the real axis row nearest Im=0 at the sphere column, sweep outward
    i0=int(np.argmin(abs(c3_im))); j0=int(np.argmin(abs(c3_re-(-1/6))))
    tau,y=solve_tau1(c3_re[j0]+1j*c3_im[i0],q1,tau_seed); T[i0,j0]=tau; Y[i0,j0]=y
    order=[]
    for j in list(range(j0,nr))+list(range(j0-1,-1,-1)):
        for i in list(range(i0,ni))+list(range(i0-1,-1,-1)):
            if (i,j)==(i0,j0): continue
            # seed from nearest solved neighbour
            cands=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            seed=None
            for (ii,jj) in cands:
                if 0<=ii<ni and 0<=jj<nr and not np.isnan(T[ii,jj]): seed=T[ii,jj]; break
            if seed is None: continue
            try:
                tau,y=solve_tau1(c3_re[j]+1j*c3_im[i],q1,seed)
            except Exception: tau,y=None,None
            if tau is not None: T[i,j]=tau; Y[i,j]=y
    pickle.dump(dict(q1=q1,c3_re=c3_re,c3_im=c3_im,T=T,Y=Y),open(fname,'wb'))
    return T,Y
q1=float(sys.argv[1]); 
if q1<1: seed=np.arcsin(np.sqrt(q1))
else: seed=np.pi/2+1j*np.arccosh(np.sqrt(q1))
c3_re=np.linspace(-0.56,0.02,59); c3_im=np.linspace(-0.24,0.24,49)
T,Y=scan(q1,seed,c3_re,c3_im,f'qfam_{q1}.pkl')
ok=~np.isnan(T); print(f"q1={q1}: solved {ok.sum()} of {ok.size} grid points")
# report along the real c3 axis
i0=int(np.argmin(abs(c3_im)))
print("   c3      tau1 (complex)          N (complex)              Re I      Im I     R1 (complex)        K1=a'/a")
for j in range(0,len(c3_re),2):
    if np.isnan(T[i0,j]): continue
    y=Y[i0,j]; I=y[5]+y[6]; Rv=Rf(y[0],y[1],y[2]); K=y[1]/y[0]
    print(f" {c3_re[j]:+.4f}  {T[i0,j].real:+.4f}{T[i0,j].imag:+.4f}i   {y[7].real:+.4f}{y[7].imag:+.4f}i   {I.real:+9.4f} {I.imag:+9.4f}   {Rv.real:+8.3f}{Rv.imag:+8.3f}i   {K.real:+.4f}{K.imag:+.4f}i")
# critical points of I(c3) on the grid: |dI/dc3| minima
I=np.array([[ (Y[i,j,5]+Y[i,j,6]) for j in range(len(c3_re))] for i in range(len(c3_im))])
dr=c3_re[1]-c3_re[0]; di=c3_im[1]-c3_im[0]
dIdx=np.gradient(I,dr,axis=1); dIdy=np.gradient(I,di,axis=0)
# analytic: dI/dc3 = dIdx = -i dIdy ; measure |dIdx| and Cauchy-Riemann residual
g=np.abs(dIdx); cr=np.abs(dIdx+1j*dIdy)
print("smallest |dI/dc3| on grid (candidate critical points), with Cauchy-Riemann residual:")
idx=np.dstack(np.unravel_index(np.argsort(g,axis=None),g.shape))[0][:8]
for i,j in idx:
    y=Y[i,j]; print(f"  c3={c3_re[j]:+.4f}{c3_im[i]:+.4f}i |dI/dc3|={g[i,j]:.3e} CR={cr[i,j]:.2e}  N={y[7]:.4f} I={I[i,j]:.4f} R1={Rf(y[0],y[1],y[2]):.3f}")
