import numpy as np, pickle, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
exec(open('shoot.py').read().split("# sanity")[0])   # reuse F, run()
def neck_a3(c3,e):
    ex,cl,bl,s=run(c3,e)
    if len(ex)<3: return np.nan
    return ex[1][4]   # a''' at the second extremum (the neck)
res={}
for e in (0.25,0.5,1.0,2.0,5.0,10.0):
    # bracket: scan
    grid=np.linspace(-0.60,-0.20,41); vals=[neck_a3(c,e) for c in grid]
    br=None
    for i in range(len(grid)-1):
        if np.isfinite(vals[i]) and np.isfinite(vals[i+1]) and vals[i]*vals[i+1]<0: br=(grid[i],grid[i+1])
    if br is None: print(f"eps={e}: no neck-symmetric root in bracket; vals:",[None if not np.isfinite(v) else round(v,2) for v in vals][::5]); continue
    c3r=brentq(neck_a3,br[0],br[1],args=(e,),xtol=1e-10)
    ex,cl,bl,s=run(c3r,e)
    (t1,a1,_,a1dd,_),(t2,a2,_,a2dd,a2ddd)=ex[0],ex[1]
    res[e]=dict(c3=c3r,tau_peak=t1,a_peak=a1,tau_neck=t2,a_neck=a2,a2dd=a2dd,tau_close=s.t[-1])
    print(f"eps={e:5.2f}: c3*={c3r:+.6f}  peak (tau={t1:.4f}, a={a1:.4f})  neck (tau={t2:.4f}, a={a2:.4f}, a''={a2dd:+.4f}, a'''={a2ddd:+.1e})  closes at tau={s.t[-1]:.4f} (2*tau_neck={2*t2:.4f})")
pickle.dump(res,open('roots.pkl','wb'))
