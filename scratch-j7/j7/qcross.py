# crossover q (at R=12) where the recontracting cap's I_(a,R) equals the sphere's, for eps in the window
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
def F(x,q1,R1,e):
    y=run_path(x[0].real,e,[x[1].real],1.0); return np.array([y[0]**2-q1,Rf(y[0],y[1],y[2])-R1]).real,y
def newton(x,q1,R1,e,maxit=60):
    x=np.array(x,dtype=float)
    for it in range(maxit):
        f,y=F(x,q1,R1,e)
        if np.linalg.norm(f)<1e-10: return x,y,it
        h=1e-6; J=np.zeros((2,2))
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp,q1,R1,e); J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: return x,y,-1
        if np.linalg.norm(dx)>0.3: dx*=0.3/np.linalg.norm(dx)
        x=x+dx
    return x,y,-1
def IaR_rec(x,e):
    C=sym_C(x[0],e,[x[1]]); y=run_path(x[0],e,[x[1]],C); A,v=y[0],y[1]; R=Rf(y[0],y[1],y[2])
    return (y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*v**3-(e/4)*A**2*R*v).real
seeds={0.25:(-0.007626,3.08672),0.28:(-0.007939,3.20951),0.30:(-0.008064,3.29029),0.32:(-0.008135,3.37024),0.33:(-0.00815,3.41)}
for e,x0 in seeds.items():
    x=np.array(x0); 
    def gap(q):
        global x
        xx,y,it=newton(x,q,12.0,e)
        if it<0: return np.nan
        x=xx; return IaR_rec(xx,e)+(1+2*e)
    q=4.0; g4=gap(4.0)
    if not g4<0: print(f"eps={e}: gap(4)={g4:+.4f} >= 0, no crossover above q=4"); continue
    lo,hi=4.0,4.0; glo=g4
    while True:
        hi=lo+0.5; ghi=gap(hi)
        if np.isnan(ghi): print(f"eps={e}: lost the cap at q={hi}"); break
        if ghi>0: break
        lo,glo=hi,ghi
    if np.isnan(ghi): continue
    for k in range(20):
        mid=0.5*(lo+hi); gm=gap(mid)
        if gm<0: lo,glo=mid,gm
        else: hi,ghi=mid,gm
    print(f"eps={e}: gap(q=4)={g4:+.4f};  crossover q* = {0.5*(lo+hi):.4f} (a* = {np.sqrt(0.5*(lo+hi)):.4f}), recontracting cap lower only for q < q*",flush=True)
