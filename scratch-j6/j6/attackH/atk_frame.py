# Attack checks on frame dependence and on the double bubble's neck data.
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from ccaps import *
e=1.0; c3db=-0.349489
def y0_C(c3,e,t0,C):
    y=y0_of(c3,e,t0); y[4]=C*t0; return y
def integrate_C(c3,e,path,C,t0=2e-3,events=None,dense=False):
    y=y0_C(c3,e,t0,C); pts=[t0+0j]+[complex(p) for p in path]; sols=[]
    for i in range(len(pts)-1):
        z0,z1=pts[i],pts[i+1]; dz=z1-z0
        f=lambda s,Y: dz*dens(Y,e)
        ev=[]
        if events:
            for g in events:
                h=lambda s,Y,g=g: g(z0+s*dz,Y); h.terminal=getattr(g,'terminal',False); h.direction=getattr(g,'direction',0); ev.append(h)
        sol=solve_ivp(f,(0,1),y,method='DOP853',rtol=1e-10,atol=1e-13,events=ev or None,dense_output=dense)
        sols.append((z0,dz,sol)); y=sol.y[:,-1]
        if sol.status==1: break
    return y,sols
# (A) the DB's exact neck data and R_neck(c3) near c3*
ext=lambda z,Y: Y[1].real; ext.direction=0
print("(A) R at the neck as a function of c3 (eps=1):")
for c3 in (-0.36,-0.355,-0.352,-0.3495,-0.349489,-0.347,-0.345,-0.34):
    y,sols=integrate_C(c3,e,[6.0],1.0,events=[ext],dense=True); z0,dz,sol=sols[0]
    if len(sol.t_events[0])<2: print(f"  c3={c3}: fewer than 2 extrema"); continue
    Yn=sol.y_events[0][1]; tn=(z0+sol.t_events[0][1]*dz).real
    print(f"  c3={c3:+.6f}: neck tau={tn:.5f} a={Yn[0].real:.6f} q={Yn[0].real**2:.6f} R={Rf(Yn[0],Yn[1],Yn[2]).real:.5f} a'''={Yn[3].real:+.2e}")
# (B) Newton at the DB's exact neck data, seeds sphere-branch and DB
y,sols=integrate_C(c3db,e,[6.0],1.0,events=[ext],dense=True); z0,dz,sol=sols[0]; Yn=sol.y_events[0][1]; tau_n=(z0+sol.t_events[0][1]*dz).real
qn=Yn[0].real**2; Rn=Rf(Yn[0],Yn[1],Yn[2]).real
print(f"(B) exact DB neck: q_n={qn:.6f} R_n={Rn:.6f} tau_n={tau_n:.5f}")
def F(c3,tau1,q1,R1):
    path=[min(tau1.real,1.185) if tau1.real>0.05 else 0.05, tau1] if abs(tau1.imag)>1e-12 else [tau1]
    y,_=integrate_path(c3,e,path)
    return np.array([y[0]**2-q1, Rf(y[0],y[1],y[2])-R1]), y
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
for (q1,R1,lab) in ((qn,Rn,'exact DB neck data'),(0.312,8.47,"position's rounded data")):
    print(f"  target ({q1:.6f},{R1:.5f}) [{lab}]")
    for c3s,ts in ((c3db+0j,tau_n+0j),(c3db+0j,1.185+0.8j),(-1/6+0j,np.arcsin(np.sqrt(q1))+0j),(-0.38+0j,2.0+0j)):
        x,y,it=newton(c3s,ts,q1,R1)
        print(f"    seed c3={c3s.real:+.4f} tau={ts:.3f} -> {'conv' if it>=0 else 'NO'} c3={x[0]:.6f} tau1={x[1]:.5f} a'''={y[3]:.3f} I(C=1)={(y[5]+y[6]).real:+.4f}")
# (C) Re I along the neck history in the pole-normalized frame C=1 vs symmetric frame
print("(C) Re I along the real recollapsing continuation from the neck, C=1 (pole-normalized) frame:")
for t in (0.1,0.2,0.3,0.4,0.5,0.55):
    yy,_=integrate_C(c3db,e,[tau_n,tau_n+1j*t],1.0)
    print(f"   t={t:.2f}: a={yy[0].real:+.4f}{yy[0].imag:+.1e}i  Re I={(yy[5]+yy[6]).real:+.5f} (Re I_loc={yy[5].real:+.5f}, Re Gamma={yy[6].real:+.5f})  theta={yy[4]:.4f}")
# (D) frame dependence of I(c3) along the real c3 family at q1=0.4 (first crossing), C = 0.3, 1, 3
q1=0.4
hit=lambda z,Y: (Y[0]**2-q1).real; hit.terminal=True; hit.direction=1
print("(D) I(c3) at q1=0.4 along real c3 for three boost frames C (first real crossing):")
print("   c3      I(C=0.3)   I(C=1)    I(C=3)    I_loc     theta1(C=0.3,1,3)")
rows=[]
for c3 in np.arange(-0.46,0.0201,0.02):
    vals=[];ths=[]
    for C in (0.3,1.0,3.0):
        y,sols=integrate_C(c3,e,[3.0],C,events=[hit],dense=False); z0,dz,sol=sols[0]
        if len(sol.t_events[0])==0: vals.append(np.nan); ths.append(np.nan); continue
        Y=sol.y_events[0][0]; vals.append((Y[5]+Y[6]).real); ths.append(Y[4].real); Il=Y[5].real
    rows.append((c3,*vals,Il)); print(f" {c3:+.3f}  {vals[0]:+.5f}  {vals[1]:+.5f}  {vals[2]:+.5f}  {Il:+.5f}   {ths[0]:.3f} {ths[1]:.3f} {ths[2]:.3f}")
rows=np.array(rows)
for k,lab in ((1,'C=0.3'),(2,'C=1'),(3,'C=3'),(4,'I_loc')):
    d=np.gradient(rows[:,k],rows[:,0]); sc=np.where(np.sign(d[:-1])*np.sign(d[1:])<0)[0]
    print(f"   dI/dc3 sign changes for {lab}:",[(round(rows[i,0],2)) for i in sc], " min|dI/dc3|=%.3f"%np.nanmin(abs(d)))
# (E) perturbed sphere from its peak: split Re I into local and anomaly parts
print("(E) perturbed sphere c3=-1/6+1e-3 from its peak, C=1: Re I_loc and Re Gamma separately")
c3=-1/6+1e-3
y,sols=integrate_C(c3,e,[6.0],1.0,events=[ext],dense=True); z0,dz,sol=sols[0]; tp=(z0+sol.t_events[0][0]*dz).real
for t in (0.5,1.0,1.5,2.0,2.5,3.0):
    yy,_=integrate_C(c3,e,[tp,tp+1j*t],1.0)
    print(f"   t={t:.1f}: Re a={yy[0].real:.3f} Im a={yy[0].imag:+.4f}  Re I_loc={yy[5].real:+.4f}  Re Gamma={yy[6].real:+.4f}  Re I={(yy[5]+yy[6]).real:+.4f}")
