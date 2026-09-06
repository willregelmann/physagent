import numpy as np, sys
exec(open('invariant.py').read().split("e=1.0; c3db=")[0])
def F(c3,tau1,q1,R1,e,path=None):
    if path is None: path=[min(tau1.real,1.185) if tau1.real>0.05 else 0.05, tau1] if abs(tau1.imag)>1e-12 else [tau1]
    y=run_path(c3,e,path,1.0); return np.array([y[0]**2-q1, Rf(y[0],y[1],y[2])-R1]), y
def newton(c3,tau1,q1,R1,e,maxit=40,path=None):
    x=np.array([c3,tau1],dtype=complex)
    for it in range(maxit):
        f,y=F(x[0],x[1],q1,R1,e,path)
        if not np.all(np.isfinite(f)): return x,y,-1
        if np.linalg.norm(f)<1e-9: return x,y,it
        h=1e-6; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp[0],xp[1],q1,R1,e,path); J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: return x,y,-1
        if np.linalg.norm(dx)>0.3: dx*=0.3/np.linalg.norm(dx)
        x=x+dx
    return x,y,-1
e=1.0; c3p=-0.885788-0.478724j; t1p=2.73251+1.13928j
print("=== (1) path-independence check of the complex-pair saddle at (4,12), eps=1:")
for path in ([1.185,t1p],[t1p],[0.8+0.3j,t1p],[0.5,1.5+0.8j,t1p]):
    f,y=F(c3p,t1p,4.0,12.0,e,path); print(f"   path={path}: residual={np.abs(f).max():.1e}  a={y[0]:.5f} R={Rf(y[0],y[1],y[2]):.4f} I_loc={y[5]+y[6]:.4f} a'''={y[3]:.4f}")
print("   data at the cut: a'''=",y[3]," (sphere dS at a=2 has a'''=+i sinh(arccosh 2)*... = ",np.cos(np.pi/2+1j*np.arccosh(2.0))*(-1),")")
print("=== (2) continuation of the complex-pair cap from its cut along +i t and -i t (is it a classical history?):")
for sgn in (1,-1):
    for t in (0.25,0.5,1.0,1.5,2.0,3.0):
        path=[1.185,t1p,t1p+sgn*1j*t]
        y=run_path(c3p,e,path,1.0); A=y[0]
        try: Ii=inv(c3p,e,path,f"pair cont {'+' if sgn>0 else '-'}i t={t}")
        except Exception as ex: print("   inv failed",ex)
        print(f"        Im a/Re a={A.imag/A.real:+.4f}  R={Rf(y[0],y[1],y[2]):.3f}  K={y[1]/y[0]:.4f}")
print("=== (3) the same saddle family at larger dS data (q1,12), eps=1: track from (4,12) by continuation in q1:")
c3,t1=c3p,t1p
for q1 in (6.0,9.0,16.0,25.0):
    x,y,it=newton(c3,t1+0.5j,q1,12.0,e)
    if it<0: print(f"   q1={q1}: no convergence (c3={x[0]:.4f}, tau1={x[1]:.4f})"); break
    c3,t1=x[0],x[1]; Ii=inv(c3,e,[1.185,t1],f"pair at ({q1},12)")
    print(f"        sphere at ({q1},12): I_inv=-3.0000 (frozen);  pair K={y[1]/y[0]:.4f}, dS K would be {np.cos(np.pi/2+1j*np.arccosh(np.sqrt(q1)))/np.sqrt(q1):.4f}")
print("=== (4) saddles at (4,12) inside the window and at eps_c: eps=0.30, 0.355 (seeds: sphere, complex pair, real-Euclidean, others):")
for e in (0.30,0.355):
    found=[]
    seeds=[(-1/6,np.pi/2+1j*np.arccosh(2.0)),(c3p,t1p),(np.conj(c3p),np.conj(t1p)),(-0.5,2+0.5j),(-0.5,2.5-1j),(-0.005,5.7),(-0.01,4.0),(-0.05,2.0),(-0.3,2.0+0.5j),(0.05,1+1j),(-0.25,2.5-1j)]
    for c3s,ts in seeds:
        try: x,y,it=newton(complex(c3s),complex(ts),4.0,12.0,e)
        except Exception as ex: continue
        if it<0: continue
        if all(abs(x[0]-f[0])>1e-5 or abs(x[1]-f[1])>1e-5 for f in found):
            found.append((x[0],x[1]))
            path=[min(x[1].real,1.185) if x[1].real>0.05 else 0.05, x[1]] if abs(x[1].imag)>1e-12 else [x[1]]
            print(f"  eps={e}: saddle c3={x[0]:.6f} tau1={x[1]:.5f} K={y[1]/y[0]:.4f} I_loc={y[5]+y[6]:.4f}  [seed {c3s},{ts}]")
            try: inv(x[0],e,path,f"      eps={e} saddle")
            except Exception as ex: print("      inv failed",ex)
    print(f"  eps={e}: distinct saddles found: {len(found)}")
