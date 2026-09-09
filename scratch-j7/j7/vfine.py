import numpy as np, sys
exec(open('vfamily.py').read().split("for e in (1.0,0.3):")[0])
for e,grid in ((0.3,list(np.linspace(-0.0125,-0.0015,12))),(1.0,list(np.linspace(-0.031,-0.0275,4)))):
    print(f"=== eps={e}: fine contracting-side scan near the turning point and the saddle ===")
    for c3 in grid:
        cr=crossings(c3,e)
        if not cr: print(f"c3={c3:+.5f}: no crossing"); continue
        for k,t1 in enumerate(cr[:2]):
            A,v,R,Iinv,EHH,ET=row(c3,e,t1)
            print(f"c3={c3:+.5f} {'expanding' if k==0 else 'contracting':11s} tau1={t1:7.4f} v={v:+8.4f} R={R:+9.4f} I_inv={Iinv:+10.4f}  E_HH={EHH:+10.4f}  E_T={ET:+10.4f}",flush=True)
