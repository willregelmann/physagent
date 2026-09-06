import numpy as np
from ccaps import *
e=1.0; c3db=-0.349489; tau_p=1.18499
def F(c3,tau1,q1,R1):
    path=[min(tau1.real,tau_p) if tau1.real>0.05 else 0.05, tau1] if abs(tau1.imag)>1e-12 else [tau1]
    y,_=integrate_path(c3,e,path)
    return np.array([y[0]**2-q1, Rf(y[0],y[1],y[2])-R1]), y
def newton(c3,tau1,q1,R1,maxit=60):
    x=np.array([c3,tau1],dtype=complex)
    for it in range(maxit):
        f,y=F(x[0],x[1],q1,R1)
        if np.linalg.norm(f)<1e-9: return x,y,it
        h=1e-6; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp[0],xp[1],q1,R1); J[:,k]=(fp-f)/h
        dx=np.linalg.solve(J,-f)
        if np.linalg.norm(dx)>0.3: dx*=0.3/np.linalg.norm(dx)
        x=x+dx
    return x,y,-1
for (q1,R1) in ((4.0,12.0),(4.0,20.0),(1.0,12.0),(0.312,8.47)):
    print(f"=== target q1={q1}, R1={R1}")
    # seeds: sphere branch; DB-peak branch at several t
    seeds=[(-1/6+0j,np.pi/2+1j*np.arccosh(np.sqrt(q1)) if q1>=1 else np.arcsin(np.sqrt(q1))+0j)]
    for t in (0.8,1.0,1.2,1.4):
        seeds.append((c3db+0j,tau_p+1j*t))
    for c3s,ts in seeds:
        try:
            x,y,it=newton(c3s,ts,q1,R1)
        except Exception as ex:
            print(f"  seed c3={c3s:.4f} tau={ts:.3f}: failed ({ex})"); continue
        I=y[5]+y[6]
        print(f"  seed c3={c3s.real:+.4f} tau={ts:.3f} -> {'conv' if it>=0 else 'NO conv'} c3={x[0]:.5f} tau1={x[1]:.5f}  a={y[0]:.4f}  R={Rf(y[0],y[1],y[2]):.4f}  N={y[7]:.4f}  I_loc={y[5]:.4f}  Gamma(C=1)={y[6]:.4f}  Re I={I.real:+.4f}")
