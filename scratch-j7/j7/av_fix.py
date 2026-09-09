import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
e=1.0
fail={'I':(-0.103854-0.087970j,-10.389552+3.304918j),'J':(-0.067485+0.073246j,4.536903+10.252188j),'M':(-0.099604-0.091109j,11.524847-8.253794j),
'N':(-0.071493-0.074147j,3.927697-16.782805j),'O':(-0.091483+0.095266j,-7.733206-8.265503j),'P':(0.038850+0.108716j,-1.880350+6.600720j)}
def try_gauge(c3,T,C0,C1,it=60):
    def f(C):
        y=run_path(c3,e,[T],C); v=y[4]-np.pi/2
        return (v if np.isfinite(v) else None),y
    a,b=complex(C0),complex(C1); fa,_=f(a); fb,_=f(b)
    if fa is None or fb is None: return None
    for k in range(it):
        if fb==fa: return None
        c=b-fb*(b-a)/(fb-fa); fc,y=f(c)
        if fc is None: return None
        a,fa,b,fb=b,fb,c,fc
        if abs(fc)<1e-10:
            Iinv=y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*y[1]**3
            return c,Iinv,y
    return None
print("=== gauge repair for the six (a,v) saddles where sym_C failed: scan complex C seeds ===")
for nm,(c3,T) in fail.items():
    sols=[]
    for r in (0.02,0.05,0.1,0.3,1.0,3.0):
        for ph in np.linspace(0,2*np.pi,12,endpoint=False):
            C0=r*np.exp(1j*ph); res=try_gauge(c3,T,C0,C0*1.05)
            if res is None: continue
            c,Iinv,y=res
            if all(abs(c-s[0])>1e-6 for s in sols): sols.append((c,Iinv))
    if not sols: print(f"{nm}: no gauge found"); continue
    for c,Iinv in sols: print(f"{nm}: C*={c:.5f}  I_inv={Iinv:.4f}  Re I_inv={Iinv.real:+.4f}")
print("=== complex pair at (4,12) for eps=1.0, 0.85, 0.7 (h=1e-6, tol 1e-8) ===")
def Fq(x,q1,R1,e,path):
    y=run_path(x[0],e,path,1.0); return np.array([y[0]**2-q1,Rf(y[0],y[1],y[2])-R1]),y
x=np.array((-0.885788-0.478724j,2.73251+1.13928j),dtype=complex)
for e in (1.0,0.85,0.7,0.6):
    for it in range(60):
        path=[1.185,x[1]]; f,y=Fq(x,4.0,12.0,e,path)
        if np.linalg.norm(f)<1e-8: break
        h=1e-6; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=Fq(xp,4.0,12.0,e,path); J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: break
        if np.linalg.norm(dx)>0.3: dx*=0.3/np.linalg.norm(dx)
        x=x+dx
    path=[1.185,x[1]]; C=sym_C(x[0],e,path); yy=run_path(x[0],e,path,C)
    A,v=yy[0],yy[1]; R=Rf(yy[0],yy[1],yy[2]); Iinv=yy[5]+yy[6]*3*e/(3*e+1)+yy[9]-(1/3)*v**3; B=-(e/4)*A**2*R*v
    print(f"eps={e}: pair c3={x[0]:.6f} tau1={x[1]:.5f} resid={np.linalg.norm(f):.1e} theta1={yy[4]:.4f} v={v:.4f} I_inv={Iinv:.4f} B={B:.4f} Re I_aR={Iinv.real+B.real:+.4f} (sphere {-(1+2*e):+.4f}) gap={Iinv.real+B.real+1+2*e:+.4f}",flush=True)
