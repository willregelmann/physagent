# ATTACK on §6: are the twelve 'evaluated' census values sheet/path-independent?  For each saddle, integrate along three homotopically
# different tau-paths from the pole to T (straight; real-axis-then-vertical; vertical-then-horizontal) and compare the endpoint data
# (same sheet iff a(T), a'(T) agree) and I_inv (which can differ by the anomaly functional's branch even on the same sheet).
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
sad={'sphere':(-0.166667-0.000000j,1.570796+1.762747j),'A':(-0.061078-0.074741j,0.958365-7.517934j),'B':(-0.078012-0.080863j,3.646649-7.552073j),
'C':(0.011760-0.000057j,-6.007494-4.176755j),'D':(0.006200+0.006758j,4.931966+3.047997j),'E':(-0.160805+0.117255j,-4.089197-8.820504j),
'F':(-0.024640+0.090852j,2.969438-8.244251j),'G':(-0.073135-0.070948j,2.275652-14.632213j),'H':(-0.074380-0.093827j,0.233795+9.329840j),
'K':(-0.067834+0.076298j,-6.494782-10.376287j),'L':(-0.041756-0.168680j,0.644368+8.539119j),'S':(-0.024619+0.074912j,-6.323142+10.106159j)}
e=1.0
def Iinv_on(c3,path):
    try:
        C=sym_C(c3,e,path); y=run_path(c3,e,path,C)
        ok=abs(y[4]-np.pi/2)<1e-6
        return y[0],y[1],(y[5]+y[6]*3*e/(3*e+1)+y[9]-(1/3)*y[1]**3),ok,C
    except Exception as ex:
        return None,None,None,False,None
print("=== path dependence of the fixed-(a,v) census at (3,-i sqrt8), eps=1: straight | real-then-vertical | vertical-then-horizontal ===")
for nm,(c3,T) in sad.items():
    paths={'straight':[T],'re-then-im':[T.real if abs(T.real)>1e-3 else 1e-3,T],'im-then-re':[1j*T.imag if abs(T.imag)>1e-3 else 1e-3,T]}
    line=f"{nm:7s}"
    for pn,p in paths.items():
        a,v,I,ok,C=Iinv_on(c3,p)
        if a is None: line+=f" | {pn}: FAIL"; continue
        line+=f" | {pn}: a={a:.3f} v={v:.3f} ReI={I.real:+9.4f} ImI={I.imag:+8.3f} gauge={'ok' if ok else 'NO'}"
    print(line,flush=True)
