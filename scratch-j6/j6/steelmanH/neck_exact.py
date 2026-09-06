import numpy as np, sys
sys.path.insert(0,'..')
from ccaps import *
e=1.0; c3db=-0.349489
ext=lambda z,Y: Y[1].real; ext.direction=0
def neck(c3):
    y,sols=integrate_path(c3,e,[6.0],events=[ext],dense=True); z0,dz,sol=sols[0]
    if len(sol.t_events[0])<2: return None
    Yn=sol.y_events[0][1]; tn=(z0+sol.t_events[0][1]*dz).real
    return tn,Yn[0].real,Rf(Yn[0],Yn[1],Yn[2]).real,Yn[3].real
print("R_neck(c3) near the symmetric double bubble (eps=1):")
for c3 in (-0.37,-0.36,-0.355,-0.352,-0.35,-0.349489,-0.348,-0.345,-0.34,-0.335):
    r=neck(c3)
    if r is None: print(f"  c3={c3:+.6f}: <2 extrema"); continue
    print(f"  c3={c3:+.6f}: tau_n={r[0]:.5f} a_n={r[1]:.6f} q_n={r[1]**2:.6f} R_n={r[2]:.5f} a'''_n={r[3]:+.2e}")
tn,an,Rn,_=neck(c3db); qn=an**2
print(f"exact DB neck data: q_n={qn:.6f}, R_n={Rn:.6f}, tau_n={tn:.5f}")
def F(c3,tau1,q1,R1):
    path=[min(tau1.real,1.185) if tau1.real>0.05 else 0.05, tau1] if abs(tau1.imag)>1e-12 else [tau1]
    y,_=integrate_path(c3,e,path); return np.array([y[0]**2-q1, Rf(y[0],y[1],y[2])-R1]), y
def newton(c3,tau1,q1,R1,maxit=60):
    x=np.array([c3,tau1],dtype=complex)
    for it in range(maxit):
        f,y=F(x[0],x[1],q1,R1)
        if np.linalg.norm(f)<1e-10: return x,y,it
        h=1e-6; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp[0],xp[1],q1,R1); J[:,k]=(fp-f)/h
        dx=np.linalg.solve(J,-f)
        if np.linalg.norm(dx)>0.3: dx*=0.3/np.linalg.norm(dx)
        x=x+dx
    return x,y,-1
for (q1,R1,lab) in ((qn,Rn,'exact neck data'),(0.312,8.47,'position rounded data')):
    print(f"Newton at ({q1:.6f},{R1:.5f}) [{lab}]:")
    found=[]
    for c3s,ts in ((c3db,tn),(c3db,1.185+0.8j),(-1/6,np.arcsin(np.sqrt(q1))),(-0.38,2.0),(-0.45,1.0),(-0.6,0.9),(-0.25,3.0),(-0.05,0.6),(0.05,0.55),(-0.2,1.0+1.0j)):
        try: x,y,it=newton(c3s+0j,ts+0j,q1,R1)
        except Exception as ex: print("   seed",c3s,ts,"failed",ex); continue
        new=all(abs(x[0]-f[0])>1e-5 or abs(x[1]-f[1])>1e-5 for f in found)
        if it>=0 and new: found.append((x[0],x[1]))
        print(f"   seed c3={c3s:+.3f} tau={ts:.3f} -> {'conv' if it>=0 else 'NO'} c3={x[0]:.6f} tau1={x[1]:.5f} a'''={y[3]:.3f} K1={(y[1]/y[0]):.3f} I(C=1)={(y[5]+y[6]).real:+.4f} I_loc={y[5].real:+.4f} {'NEW' if (it>=0 and new) else ''}")
    print("  distinct saddles:",len(found))
