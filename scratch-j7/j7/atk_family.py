# ATTACK on §5: is the real a1=2 family complete?
#  (a) what happens to the -1/6 < c3 < 0 caps after they recontract through a=2: irregular pole (a->0) or bounce and re-cross?
#  (b) do the neck-class caps (c3 < -1/6, double-bubble-like) reach a=2 after their neck, giving extra real saddles/points on the v-line?
#  (c) tabulate I_(a,R) at each cap's OWN (a,R) along the real family (the on-shell (a,R) Hamilton-Jacobi function) -- is it unbounded below like I_inv?
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
def scan(c3,e,a1=2.0,tmax=40.0,amax=200.0):
    hit=lambda s,Y: Y[0].real-a1; hit.direction=0
    stop1=lambda s,Y: Y[0].real-0.02; stop1.terminal=True; stop1.direction=-1
    stop2=lambda s,Y: Y[0].real-amax; stop2.terminal=True
    y,sols=integrate_path(c3,e,[tmax],events=[hit,stop1,stop2],dense=True)
    z0,dz,sol=sols[0]
    cr=[(z0+s*dz).real for s in sol.t_events[0]]
    tend=(z0+sol.t[-1]*dz).real
    # min radius after first max, max radius
    A=sol.y[0].real; T=(z0+sol.t*dz).real
    end='a->0 (irregular pole)' if len(sol.t_events[1]) else ('a>amax' if len(sol.t_events[2]) else 'tmax reached')
    # detect local minima (necks) of a along the path
    necks=[(T[i],A[i]) for i in range(1,len(A)-1) if A[i]<A[i-1] and A[i]<A[i+1] and A[i]>0.02]
    return cr,end,tend,A.max(),necks,sol
def IaR_at(c3,e,t1):
    C=sym_C(c3,e,[t1]); y=run_path(c3,e,[t1],C); A,v=y[0].real,y[1].real; R=Rf(y[0],y[1],y[2]).real
    Iinv=(y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*y[1]**3).real
    return A,v,R,Iinv,Iinv-(e/4)*A**2*R*v,y[4]
for e in (1.0,0.3):
    print(f"\n===== eps={e} (a) fate of the -1/6<c3<0 caps after recontraction; all crossings of a=2 up to tau=40 =====")
    for c3 in (-0.0275,-0.02,-0.01,-0.004475,-0.002,-0.001,-0.0005):
        cr,end,tend,amax,necks,sol=scan(c3,e)
        print(f"c3={c3:+.5f}: crossings of a=2 at tau={['%.3f'%t for t in cr]} ; ends: {end} at tau={tend:.3f}; a_max={amax:.3f}; necks={[(round(t,3),round(a,4)) for t,a in necks][:4]}")
    print(f"\n===== eps={e} (b) neck-class caps c3 < -1/6: do they reach a=2 after a neck? =====")
    for c3 in (-0.2,-0.25,-0.3,-0.349489,-0.4,-0.5,-0.7,-1.0,-2.0,-5.0):
        try:
            cr,end,tend,amax,necks,sol=scan(c3,e)
        except Exception as ex:
            print(f"c3={c3:+.4f}: fail {ex}"); continue
        line=f"c3={c3:+.4f}: crossings of a=2 at tau={['%.3f'%t for t in cr]} ; ends: {end} at tau={tend:.3f}; a_max={amax:.3f}; necks={[(round(t,3),round(a,4)) for t,a in necks][:4]}"
        print(line,flush=True)
        for t1 in cr[:4]:
            try:
                A,v,R,Iinv,IaR,th=IaR_at(c3,e,t1)
                print(f"      crossing tau1={t1:.4f}: a={A:.4f} v={v:+.4f} R={R:+.4f} I_inv={Iinv:+.4f} I_(a,R)@own R={IaR:+.4f}  E_HH(R_t=12)={-Iinv+(e/4)*A**2*12*v:+.4f}  theta1={th:.4f}",flush=True)
            except Exception as ex:
                print(f"      crossing tau1={t1:.4f}: I_inv fail {ex}")
print("\n===== (c) on-shell I_(a,R) at each real cap's own (a=2, R): from the vfamily tables (I_inv - eps*R*v at a=2) =====")
import re
for e,block in ((1.0,0),(0.3,1)):
    txt=open('vfamily.out').read().split('=== eps=')[1+block]
    rows=[]
    for m in re.finditer(r"c3=([+-]\d+\.\d+) (expanding|contracting)\s+tau1=\s*([\d.]+) v=\s*([+-][\d.]+) R=\s*([+-][\d.]+) I_inv=\s*([+-][\d.]+)",txt):
        c3,side,t1,v,R,Ii=float(m.group(1)),m.group(2),float(m.group(3)),float(m.group(4)),float(m.group(5)),float(m.group(6))
        rows.append((c3,side,v,R,Ii,Ii-e*R*v))
    print(f"eps={e}: c3, side, v, R, I_inv, I_(a,R)@own R")
    for r in rows: print(f"   {r[0]:+.5f} {r[1]:11s} v={r[2]:+8.4f} R={r[3]:+9.3f} I_inv={r[4]:+10.3f}  I_(a,R)={r[5]:+10.3f}")
    print(f"   min of I_(a,R) along the family: {min(r[5] for r in rows):+.4f}; min of I_inv: {min(r[4] for r in rows):+.4f}")
