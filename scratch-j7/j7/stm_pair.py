# STEELMAN flaw 7 / 17: (i) continue the complex pair at (4,12) in eps from 0.5 to 1.0 in small steps on the two-segment path
# [1.185, tau1] (ar_table lost it between 0.5 and 0.7) and check it connects to invariant.out's eps=1 pair (c3=-0.885788-0.478724i);
# (ii) continue the recontracting cap in q at R=12, eps=1, with small steps beyond q=9 (ar_table lost it at q=16) and at eps=0.3 beyond 16.
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
def pathof(t1):
    t1=complex(t1); return [min(t1.real,1.185) if t1.real>0.05 else 0.05, t1] if abs(t1.imag)>1e-12 else [t1]
def F(x,q1,R1,e,real=False):
    p=[x[1].real] if real else pathof(x[1])
    y=run_path(x[0].real if real else x[0],e,p,1.0); return np.array([y[0]**2-q1,Rf(y[0],y[1],y[2])-R1]),y
def newton(x,q1,R1,e,maxit=60,real=False):
    x=np.array(x,dtype=complex)
    for it in range(maxit):
        f,y=F(x,q1,R1,e,real)
        if not np.all(np.isfinite(f)): return x,y,-1
        if np.linalg.norm(f)<1e-9: return x,y,it
        h=1e-6; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp,q1,R1,e,real); J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: return x,y,-1
        if np.linalg.norm(dx)>0.2: dx*=0.2/np.linalg.norm(dx)
        x=x+dx
        if real: x=x.real+0j
    return x,y,-1
def IaR(c3,e,path):
    C=sym_C(c3,e,path); y=run_path(c3,e,path,C); A,v=y[0],y[1]; R=Rf(y[0],y[1],y[2])
    Iinv=y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*v**3; B=-(e/4)*A**2*R*v
    return Iinv,B,A,v,R,y[4]
print("=== (i) complex pair at (4,12): eps continuation 0.50 -> 1.00, step 0.05, path [1.185, tau1] ===")
x=np.array((-0.204602-0.818542j,2.46994+0.91183j),dtype=complex)
# first bring the eps=0.3 seed to 0.5 in steps
for e in list(np.arange(0.30,0.501,0.05))+list(np.arange(0.55,1.001,0.05)):
    e=round(float(e),3)
    x,y,it=newton(x,4.0,12.0,e)
    if it<0: print(f"eps={e}: lost (resid {np.linalg.norm(F(x,4,12,e)[0]):.1e}) at x={x}"); break
    Iinv,B,A,v,R,th=IaR(x[0],e,pathof(x[1]))
    print(f"eps={e:.2f}: c3={x[0]:.6f} tau1={x[1]:.5f} v={v:.4f} theta1={th:.4f} I_inv={Iinv:.4f} Re I_aR={Iinv.real+B.real:+.4f} sphere={-(1+2*e):+.4f} gap={Iinv.real+B.real+1+2*e:+.4f}",flush=True)
print("   reference eps=1 pair from invariant.out: c3=-0.885788-0.478724i tau1=2.73251+1.13928i, I_inv=-4.6439-10.9117i, Re I_aR=-4.394")
print("=== (ii) recontracting cap at (q,12), eps=1: q continuation beyond 9 in steps of 1 ===")
x=np.array((-0.000443,8.2931),dtype=complex)
for q in np.arange(9.0,26.0,1.0):
    x,y,it=newton(x,q,12.0,1.0,real=True)
    if it<0: print(f"q={q}: lost"); break
    Iinv,B,A,v,R,th=IaR(x[0].real,1.0,[x[1].real])
    print(f"q={q:5.1f}: c3={x[0].real:+.7f} tau1={x[1].real:.4f} v={v.real:+.4f} I_inv={Iinv.real:+9.4f} B={B.real:+9.4f} I_aR={Iinv.real+B.real:+9.4f} sphere=-3.000 gap={Iinv.real+B.real+3:+9.4f}",flush=True)
print("=== (iii) recontracting cap at (q,12), eps=0.3: q continuation beyond 16 in steps of 1 ===")
x=np.array((-0.000049,6.3874),dtype=complex)
for q in np.arange(16.0,31.0,1.0):
    x,y,it=newton(x,q,12.0,0.3,real=True)
    if it<0: print(f"q={q}: lost"); break
    Iinv,B,A,v,R,th=IaR(x[0].real,0.3,[x[1].real])
    print(f"q={q:5.1f}: c3={x[0].real:+.7f} tau1={x[1].real:.4f} v={v.real:+.4f} I_inv={Iinv.real:+9.4f} B={B.real:+9.4f} I_aR={Iinv.real+B.real:+9.4f} sphere=-1.600 gap={Iinv.real+B.real+1.6:+9.4f}",flush=True)
