import numpy as np, sys, time
sys.path.insert(0,'..')
from ccaps import *
e=1.0
def F(c3,tau1,q1,R1):
    path=[min(tau1.real,1.185) if tau1.real>0.05 else 0.05, tau1] if abs(tau1.imag)>1e-12 else [tau1]
    y,_=integrate_path(c3,e,path); return np.array([y[0]**2-q1, Rf(y[0],y[1],y[2])-R1]), y
def newton(c3,tau1,q1,R1,maxit=40):
    x=np.array([c3,tau1],dtype=complex)
    for it in range(maxit):
        f,y=F(x[0],x[1],q1,R1)
        if not np.all(np.isfinite(f)): return x,y,-1
        if np.linalg.norm(f)<1e-9: return x,y,it
        h=1e-6; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp[0],xp[1],q1,R1); J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: return x,y,-1
        if np.linalg.norm(dx)>0.3: dx*=0.3/np.linalg.norm(dx)
        x=x+dx
    return x,y,-1
c3seeds=[-0.5,-0.35,-0.25,-1/6,-0.05,0.0,0.05,0.2,0.5,0.1+0.1j,-0.2-0.2j]
for (q1,R1) in ((4.0,12.0),(4.0,20.0),(4.0,0.0),(9.0,12.0)):
    t0=time.time(); found=[]
    tseeds=[np.pi/2+1j*np.arccosh(np.sqrt(q1)),1.0+1.0j,2.0+0.5j,0.5+2.0j,2.5-1.0j,2.0+0j]
    print(f"=== data (q1,R1)=({q1},{R1})",flush=True)
    for c3s in c3seeds:
        for ts in tseeds:
            try: x,y,it=newton(c3s+0j,ts,q1,R1)
            except Exception as ex: continue
            if it<0: continue
            new=all(abs(x[0]-f[0])>1e-5 or abs(x[1]-f[1])>1e-5 for f in found)
            if new:
                found.append((x[0],x[1]))
                I=y[5]+y[6]; K=y[1]/y[0]
                print(f"  NEW saddle: c3={x[0]:.6f} tau1={x[1]:.5f} N_E={y[7]:.4f} K1=a'/a={K:.4f} Re I(C=1)={I.real:+.4f} Im I={I.imag:+.3f} I_loc={y[5]:.4f}  [seed c3={c3s}, tau={ts}]",flush=True)
    print(f"  distinct saddles: {len(found)}  ({time.time()-t0:.0f}s)",flush=True)
