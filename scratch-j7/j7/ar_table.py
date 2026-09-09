# J-7a: fixed-(q,R) relevance table with the correct boundary term.  I_(a,R) = I_inv - (eps/4) a^2 R v |_cut.
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
def pathof(t1):
    t1=complex(t1); return [min(t1.real,1.185) if t1.real>0.05 else 0.05, t1] if abs(t1.imag)>1e-12 else [t1]
def F(x,q1,R1,e):
    y=run_path(x[0],e,pathof(x[1]),1.0); return np.array([y[0]**2-q1, Rf(y[0],y[1],y[2])-R1]), y
def newton(c3,tau1,q1,R1,e,maxit=60,real=False):
    x=np.array([c3,tau1],dtype=complex)
    for it in range(maxit):
        f,y=F(x,q1,R1,e)
        if not np.all(np.isfinite(f)): return x,y,-1
        if np.linalg.norm(f)<1e-10: return x,y,it
        h=1e-6; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp,q1,R1,e); J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: return x,y,-1
        if np.linalg.norm(dx)>0.3: dx*=0.3/np.linalg.norm(dx)
        x=x+dx
        if real: x=x.real+0j
    return x,y,-1
def IaR(c3,e,path):
    C=sym_C(c3,e,path); y=run_path(c3,e,path,C)
    A,v=y[0],y[1]; R=Rf(y[0],y[1],y[2])
    Iinv=y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*v**3
    B=-(e/4)*A**2*R*v
    return Iinv,B,Iinv+B,A,v,R
q1,R1=4.0,12.0
print("=== fixed (q,R)=(4,12): sphere-dS, real-Euclidean recontracting cap, complex pair; I_(a,R)=I_inv-(eps/4)a^2 R v ===")
eps_grid=[0.25,0.26,0.28,0.30,0.32,0.34,0.355,0.40,0.50,0.70,1.00]
# continuation seeds
rc=(-0.008064,3.29029); pr=(-0.204602-0.818542j,2.46994+0.91183j); e_prev=0.30
res={}
for e in [0.30]+[x for x in eps_grid if x>0.30]+[x for x in sorted(eps_grid,reverse=True) if x<0.30]:
    if e==0.30 or e>0.30 and e!=0.30: pass
    Tsph=np.pi/2+1j*np.arccosh(np.sqrt(q1))
    Is,Bs,IaRs,As,vs,Rs=IaR(-1/6,e,[np.pi/2,Tsph])
    # recontracting (real): continue from nearest solved eps
    seedkey=min(res.keys(),key=lambda k:abs(k-e)) if res else None
    rc_seed=res[seedkey]['rc'] if seedkey else rc; pr_seed=res[seedkey]['pr'] if seedkey else pr
    x,y,it=newton(rc_seed[0],rc_seed[1],q1,R1,e,real=True)
    rec=None
    if it>=0:
        Ir,Br,IaRr,Ar,vr,Rr=IaR(x[0].real,e,[x[1].real]); rec=(x[0].real,x[1].real)
    xp,yp,itp=newton(pr_seed[0],pr_seed[1],q1,R1,e)
    pair=None
    if itp>=0:
        Ip,Bp,IaRp,Ap,vp,Rp=IaR(xp[0],e,pathof(xp[1])); pair=(xp[0],xp[1])
    res[e]={'rc':rec or rc_seed,'pr':pair or pr_seed}
    line=f"eps={e:5.3f} | sphere: I_inv={Is.real:+8.4f} B={Bs:+.4f} I_aR(Re)={IaRs.real:+8.4f}"
    if rec: line+=f" | recontracting: c3={x[0].real:+.6f} tau1={x[1].real:.5f} v={vr.real:+.4f} I_inv={Ir.real:+8.4f} B={Br.real:+8.4f} I_aR={IaRr.real:+8.4f}  gap(rec-sph)={IaRr.real-IaRs.real:+8.4f}"
    else: line+=" | recontracting: NOT FOUND"
    if pair: line+=f" | pair: v={vp:.4f} I_inv={Ip:.4f} B={Bp:.4f} Re I_aR={IaRp.real:+8.4f} gap={IaRp.real-IaRs.real:+.4f}"
    else: line+=" | pair: NOT FOUND"
    print(line,flush=True)
# crossover eps between recontracting cap and sphere in Re I_(a,R)
def gap(e):
    seedkey=min(res.keys(),key=lambda k:abs(k-e)); x,y,it=newton(res[seedkey]['rc'][0],res[seedkey]['rc'][1],q1,R1,e,real=True)
    if it<0: return np.nan
    res[e]={'rc':(x[0].real,x[1].real),'pr':res[seedkey]['pr']}
    Ir,Br,IaRr,Ar,vr,Rr=IaR(x[0].real,e,[x[1].real]); Is,Bs,IaRs,As,vs,Rs=IaR(-1/6,e,[np.pi/2,np.pi/2+1j*np.arccosh(2.0)])
    return IaRr.real-IaRs.real
lo,hi=0.30,0.355; glo,ghi=gap(lo),gap(hi); print(f"bisection start: gap({lo})={glo:+.5f} gap({hi})={ghi:+.5f}")
for k in range(25):
    mid=0.5*(lo+hi); gm=gap(mid)
    if np.isnan(gm): break
    if gm*glo>0: lo,glo=mid,gm
    else: hi,ghi=mid,gm
print(f"crossover eps* = {0.5*(lo+hi):.5f}  (gap={gap(0.5*(lo+hi)):+.2e})")
# q-dependence of the recontracting cap at R=12 for eps=1 and eps=0.3
for e in (1.0,0.30):
    print(f"=== recontracting cap vs sphere at (q,12), eps={e}: continuation in q ===")
    seedkey=min(res.keys(),key=lambda k:abs(k-e)); x=np.array(res[seedkey]['rc'],dtype=complex)
    for q in (4.0,6.0,9.0,16.0,25.0,49.0):
        x,y,it=newton(x[0],x[1],q,12.0,e,real=True)
        if it<0: print(f"   q={q}: not found"); break
        Ir,Br,IaRr,Ar,vr,Rr=IaR(x[0].real,e,[x[1].real]); Is,Bs,IaRs,As,vs,Rs=IaR(-1/6,e,[np.pi/2,np.pi/2+1j*np.arccosh(np.sqrt(q))])
        print(f"   q={q:5.1f}: rec c3={x[0].real:+.6f} tau1={x[1].real:.4f} v={vr.real:+.4f} I_inv={Ir.real:+9.4f} B={Br.real:+9.4f} I_aR={IaRr.real:+9.4f} | sphere I_aR={IaRs.real:+8.4f} | gap={IaRr.real-IaRs.real:+9.4f}",flush=True)
