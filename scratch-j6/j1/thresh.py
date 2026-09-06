import numpy as np, pickle
src=open('caps.py').read().split("res={}")[0]; exec(src)
def scan(e,grid):
    out=[]
    for c in grid:
        ex,cl,s=run(c,e); out.append((c,len(ex),ex[1][4] if len(ex)>=3 else np.nan))
    return out
for e in (0.15,0.20,0.25,0.30,0.35,0.40,0.45):
    grid=np.linspace(-0.70,-0.25,46); o=scan(e,grid)
    three=[(c,v) for c,n,v in o if n>=3]
    if not three: print(f"eps={e:.2f}: no three-extremum solutions in c3 in [-0.70,-0.25]; n_ext values: {sorted(set(n for c,n,v in o))}",flush=True); continue
    br=None
    for i in range(len(three)-1):
        if three[i][1]*three[i+1][1]<0: br=(three[i][0],three[i+1][0])
    if br is None: print(f"eps={e:.2f}: three-extremum window c3 in [{three[0][0]:.3f},{three[-1][0]:.3f}] but no sign change of a''' at neck (values {three[0][1]:+.2f}..{three[-1][1]:+.2f})",flush=True); continue
    c3r=brentq(neck_a3,br[0],br[1],args=(e,),xtol=1e-9)
    ex,cl,s=run(c3r,e,dense=True); tclose=s.t_events[1][0]; IDB=Ifull(s,e,tclose)
    print(f"eps={e:.2f}: window c3 in [{three[0][0]:.3f},{three[-1][0]:.3f}]; symmetric DB at c3*={c3r:+.5f}, peak a={ex[0][1]:.4f}, neck a={ex[1][1]:.4f}; I_DB/a={IDB:+.4f}, I_S4/a={IS4(e):+.4f}, dI/a={IDB-IS4(e):+.4f}",flush=True)
