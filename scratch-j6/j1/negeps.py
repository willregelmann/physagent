import numpy as np
exec(open('shoot.py').read().split("# sanity")[0])
for e in (-0.5,-2.0):
    print(f"=== eps={e} (stable sign)")
    for c3 in np.linspace(-1.0,0.0,11):
        try:
            ex,cl,bl,s=run(c3,e)
            desc=" | ".join(f"{t:.2f},{y:.3f},{y3:+.3f}" for t,y,y1,y2,y3 in ex[:3])
            print(f"c3={c3:+.2f} n_ext={len(ex)} closed={int(cl)} blow={int(bl)} {desc}")
        except Exception as ex_: print(f"c3={c3:+.2f} failed: {ex_}")
