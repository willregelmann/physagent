import numpy as np
src=open('caps.py').read().split("res={}")[0]; exec(src)
def find(e,grid):
    three=[]
    for c in grid:
        ex,cl,s=run(c,e)
        if len(ex)>=3: three.append((c,ex[1][4],ex[0][1],ex[1][1]))
    return three
for e in (0.30,0.33,0.35,0.36,0.37,0.38,0.39,0.40):
    grid=np.arange(-0.375,-0.330,0.0005); three=find(e,grid)
    if not three: print(f"eps={e:.2f}: no three-extremum solution for c3 in [-0.375,-0.330] step 5e-4",flush=True); continue
    br=None
    for i in range(len(three)-1):
        if three[i][1]*three[i+1][1]<0: br=(three[i][0],three[i+1][0])
    win=(three[0][0],three[-1][0])
    if br is None: print(f"eps={e:.2f}: window [{win[0]:.4f},{win[1]:.4f}] but no sign change (a''' from {three[0][1]:+.3f} to {three[-1][1]:+.3f}; peak-neck {three[0][2]-three[0][3]:.4f})",flush=True); continue
    c3r=brentq(neck_a3,br[0],br[1],args=(e,),xtol=1e-10)
    ex,cl,s=run(c3r,e,dense=True); IDB=Ifull(s,e,s.t_events[1][0])
    lam=(-3+np.sqrt(9+4/e))/2
    print(f"eps={e:.2f}: window [{win[0]:.4f},{win[1]:.4f}] c3*={c3r:+.6f} peak={ex[0][1]:.4f} neck={ex[1][1]:.4f} (gap {ex[0][1]-ex[1][1]:.4f}) I_DB/a={IDB:+.4f} I_S4/a={IS4(e):+.4f} dI/a={IDB-IS4(e):+.4f} | lambda+={lam:.3f}, N_inf(a2=1e6)~{3.74/lam:.1f}, N_inf(a2=1e7)~{4.89/lam:.1f}",flush=True)
print("N_inf table (no DB region): eps, lambda+, N_inf(a2=1e6):")
for e in (0.1,0.2,0.3,0.35,0.37):
    lam=(-3+np.sqrt(9+4/e))/2; print(f"  {e:.2f}  {lam:.3f}  {3.74/lam:.1f}")
