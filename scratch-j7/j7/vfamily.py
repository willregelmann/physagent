# J-7a: the v-transform. Along the real regular-cap family at fixed a1=2, tabulate v, R, I_inv and the two exponents
#   E_HH(v) = -I_inv + (eps/4) a^2 R_t v   (Psi_HH(a,R) = int dv e^{-I_inv + (eps/4)a^2 R v})
#   E_T (v) = +I_inv - (eps/4) a^2 R_t v   (tunneling sign)
# with R_t = 12. Saddles of E along real v sit where R(v) = R_t.
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
from scipy.integrate import solve_ivp
def crossings(c3,e,a1=2.0,tmax=12.0):
    # integrate the real cap, return tau values where a crosses a1 (up to 2), stop if a<0.02 or a>60
    hit=lambda s,Y: Y[0].real-a1; hit.direction=0
    stop1=lambda s,Y: Y[0].real-0.02; stop1.terminal=True; stop1.direction=-1
    stop2=lambda s,Y: Y[0].real-60.0; stop2.terminal=True
    y,sols=integrate_path(c3,e,[tmax],events=[hit,stop1,stop2],dense=True)
    z0,dz,sol=sols[0]
    return [(z0+s*dz).real for s in sol.t_events[0]]
def row(c3,e,tau1,Rt=12.0):
    C=sym_C(c3,e,[tau1]); y=run_path(c3,e,[tau1],C); A,v=y[0].real,y[1].real; R=Rf(y[0],y[1],y[2]).real
    Iinv=(y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*y[1]**3).real
    EHH=-Iinv+(e/4)*A**2*Rt*v; ET=Iinv-(e/4)*A**2*Rt*v
    return A,v,R,Iinv,EHH,ET
for e in (1.0,0.3):
    print(f"=== eps={e}: real caps through a1=2 (R_t=12).  columns: c3, side, tau1, v, R(cut), I_inv, E_HH=-I_(a,R), E_T=+I_(a,R)-form ===")
    grid=list(np.linspace(-0.16,-0.001,25))+[-0.0005,0.0,0.0005]+list(np.linspace(0.002,0.05,13))+[0.1,0.2,0.5,1.0,2.0]
    for c3 in grid:
        try: cr=crossings(c3,e)
        except Exception as ex: print(f"c3={c3:+.5f}: fail {ex}"); continue
        if not cr: print(f"c3={c3:+.5f}: no crossing of a=2 (max radius below 2)"); continue
        for k,t1 in enumerate(cr[:2]):
            side='expanding' if k==0 else 'contracting'
            try: A,v,R,Iinv,EHH,ET=row(c3,e,t1)
            except Exception as ex: print(f"c3={c3:+.5f} {side}: fail {ex}"); continue
            print(f"c3={c3:+.5f} {side:11s} tau1={t1:7.4f} v={v:+8.4f} R={R:+9.4f} I_inv={Iinv:+10.4f}  E_HH={EHH:+10.4f}  E_T={ET:+10.4f}",flush=True)
