import numpy as np, pickle, sys
from ccaps import *
def real_cuts(c3,e,tmax=12.0):
    """integrate along real tau; return list of extrema dicts (tau, a, a'', a''', R, I, N) and closing info"""
    ext=lambda z,Y: Y[1].real; ext.direction=0
    close=lambda z,Y: Y[0].real-1e-3; close.terminal=True; close.direction=-1
    blow=lambda z,Y: 40-abs(Y[0]); blow.terminal=True
    y,sols=integrate_path(c3,e,[tmax],events=[ext,close,blow],dense=True)
    z0,dz,sol=sols[0]; out=[]
    for s_ev,Y in zip(sol.t_events[0],sol.y_events[0]):
        out.append(dict(tau=(z0+s_ev*dz).real,a=Y[0].real,a2=Y[2].real,a3=Y[3].real,R=Rf(Y[0],Y[1],Y[2]).real,I=(Y[5]+Y[6]).real,N=Y[7].real,theta=Y[4].real))
    closed=len(sol.t_events[1])>0
    return out,closed,y
e=float(sys.argv[1]) if len(sys.argv)>1 else 1.0
res={}
print(f"# eps={e}: cuts at extrema of a along real caps; I = corrected action from pole to the cut (per a_anom), q1=a^2, R = scalar curvature at the cut")
print("#  c3        | peak: tau      a       a'''     R       I_peak   N_peak  | neck: tau     a       a'''     R       I_neck   N_neck")
for c3 in np.concatenate([np.linspace(-0.60,-0.36,25),np.linspace(-0.3595,-0.30,40),np.linspace(-0.30,-0.05,26)]):
    ex,closed,y=real_cuts(c3,e)
    row=dict(c3=c3,ex=ex,closed=closed)
    res[c3]=row
    p=ex[0] if len(ex)>0 else None; n=ex[1] if len(ex)>1 else None
    sp_=f"{p['tau']:.4f} {p['a']:.4f} {p['a3']:+.4f} {p['R']:+.3f} {p['I']:+.5f} {p['N']:.4f}" if p else "-"
    sn=f"{n['tau']:.4f} {n['a']:.4f} {n['a3']:+.4f} {n['R']:+.3f} {n['I']:+.5f} {n['N']:.4f}" if n else "-"
    print(f"{c3:+.5f} | {sp_} | {sn}  {'closed' if closed else 'open'} nex={len(ex)}")
pickle.dump(res,open(f'realfam_{e}.pkl','wb'))
