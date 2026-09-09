# STEELMAN flaw 4: limited Newton search for COMPLEX regular caps at the REAL fixed-(a,v) data (2,-3.598) and (2,+1.0), eps=1,
# seeded from a grid in complex (c3, tau1), straight pole->tau1 path.  For each distinct converged cap: Re I_inv (theta1=pi/2 gauge)
# vs the real cap's I_inv (-33.728 at v=-3.598 ; -1.8333 at v=+1 flat ball).  Also the pointwise v-transform exponents at R_t=12:
#   E_HH = -Re I_inv + eps*12*v ,  E_T = +Re I_inv - eps*12*v   (a=2).
import numpy as np, sys, time
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
e=1.0
def F(x,a1,v1):
    y=run_path(x[0],e,[x[1]],1.0); return np.array([y[0]-a1,y[1]-v1]),y
def newton(c3,T,a1,v1,maxit=40):
    x=np.array([c3,T],dtype=complex)
    for it in range(maxit):
        try: f,y=F(x,a1,v1)
        except Exception: return x,None,-1
        if not np.all(np.isfinite(f)) or abs(y[0])>1e3: return x,y,-1
        if np.linalg.norm(f)<1e-9: return x,y,it
        h=1e-7; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h
            try: fp,_=F(xp,a1,v1)
            except Exception: return x,y,-1
            J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: return x,y,-1
        if np.linalg.norm(dx)>0.5: dx*=0.5/np.linalg.norm(dx)
        x=x+dx
        if abs(x[1])>40 or abs(x[0])>3: return x,y,-1
    return x,y,-1
from scipy.integrate import solve_ivp
from ccaps import y0_of
def lapse_geom(c3,e,NE):
    ts=1e-5; tau0=np.sqrt(2*NE*ts+0j)
    if tau0.real<0: tau0=-tau0
    y0=y0_of(c3,e,tau0)[:4]
    def rhs(t,Y):
        a,a1,a2,a3,tau=Y; dtau=NE/a
        return [a1*dtau,a2*dtau,a3*dtau,FE(a,a1,a2,a3,e)*dtau,dtau]
    Y0=np.array(list(y0)+[tau0],dtype=complex)
    sol=solve_ivp(rhs,(ts,1.0),Y0,method='DOP853',rtol=1e-10,atol=1e-13,dense_output=True)
    tt=np.linspace(ts,1.0,4001); Y=sol.sol(tt); amin=np.abs(Y[0]).min()
    return sol.y[:,-1],amin
def Iinv_of(c3,T):
    try:
        C=sym_C(c3,e,[T]); yy=run_path(c3,e,[T],C)
        ok=abs(yy[4]-np.pi/2)<1e-6
        return yy[5]+yy[6]*3*e/(3*e+1)+yy[9]-(1/3)*yy[1]**3,ok
    except Exception: return np.nan,False
cases=((2.0,-3.5978,-33.7276,"recontracting real cap"),(2.0,1.0,-1.8333,"flat ball"))
sel=int(sys.argv[1]) if len(sys.argv)>1 else None
for (a1,v1,realcap,label) in (cases if sel is None else (cases[sel],)):
    print(f"=== data (a,v)=({a1},{v1}), eps=1: complex-cap search; real cap I_inv={realcap} ===",flush=True)
    seeds=[]
    for c3r in (-0.12,-0.05,-0.004,0.02,0.1):
        for c3i in (0.0,0.07,-0.07):
            for Tr in (1.5,3.5,5.7):
                for Ti in (1.5,-1.5):
                    seeds.append((c3r+1j*c3i,Tr+1j*Ti))
    # keep it bounded: ~ 90 seeds -> subsample to 48
    rng=np.random.default_rng(1); idx=rng.choice(len(seeds),48,replace=False); seeds=[seeds[i] for i in sorted(idx)]
    found=[]; t0=time.time()
    for (c3,T) in seeds:
        x,y,it=newton(c3,T,a1,v1)
        if it<0: continue
        if abs(x[0].imag)<1e-6 and abs(x[1].imag)<1e-6: continue   # the real cap itself
        if any(abs(x[0]-f[0])<1e-5 and abs(x[1]-f[1])<1e-4 for f in found): continue
        found.append((x[0],x[1]))
    print(f"   {len(seeds)} seeds, {len(found)} distinct complex caps, {time.time()-t0:.0f}s",flush=True)
    out=[]
    for c3,T in found:
        Ii,ok=Iinv_of(c3,T); y=run_path(c3,e,[T],1.0)
        R=Rf(y[0],y[1],y[2]); NE=y[8]
        EHH=-Ii.real+e*12*v1; ET=Ii.real-e*12*v1
        out.append((Ii.real,c3,T,R,Ii,ok,EHH,ET,NE))
    out.sort(key=lambda t:t[0])
    print(f"   real cap: Re I_inv={realcap:+.3f}  E_HH={-realcap+12*v1:+.3f}  E_T={realcap-12*v1:+.3f}")
    for ReI,c3,T,R,Ii,ok,EHH,ET,NE in out:
        rel='BELOW real cap (matters for e^{-I})' if ReI<realcap else 'ABOVE real cap (matters for e^{+I})'
        try:
            yl,amin=lapse_geom(c3,e,NE); cl=abs(yl[0]-a1)<1e-3 and abs(yl[1]-v1)<1e-3; cls=f"constant-lapse={'YES' if cl else 'NO'} (t-path end a={yl[0]:.3f} v={yl[1]:.3f}, min|a|={amin:.3f})"
        except Exception as ex: cls="constant-lapse test failed"
        print(f"   c3={c3:.6f} T={T:.5f} R={R:.3f} N_E={NE:.3f} I_inv={Ii:.4f} gauge={'ok' if ok else 'NO'} | E_HH={EHH:+.3f} E_T={ET:+.3f} | {rel} | {cls}",flush=True)
    if out:
        print(f"   lowest Re I_inv={out[0][0]:+.3f}, highest={out[-1][0]:+.3f}; real cap {realcap:+.3f}")
