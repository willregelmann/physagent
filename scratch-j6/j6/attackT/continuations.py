import numpy as np, pickle
from ccaps import *
e=1.0; c3db=-0.349489
def first_two_extrema(c3,e):
    ext=lambda z,Y: Y[1].real; ext.direction=0
    y,sols=integrate_path(c3,e,[12.0],events=[ext],dense=True); z0,dz,sol=sols[0]
    return [(z0+s*dz).real for s in sol.t_events[0]]
def continue_from(c3,e,tau_start,T,n=25,direction=1j,label=""):
    ts=np.linspace(0,T,n+1)[1:]
    print(f"--- {label}: c3={c3}, from tau={tau_start:.4f} along {direction}*t")
    print("   t      Re a      Im a     |a|^2    Re I      Im I      Re N     Im N    R (complex)")
    out=[]
    for t in ts:
        y,_=integrate_path(c3,e,[tau_start,tau_start+direction*t])
        Rv=Rf(y[0],y[1],y[2]); I=action(y)
        out.append((t,y[0],I,y[7],Rv))
        print(f" {t:5.2f} {y[0].real:+9.4f} {y[0].imag:+9.4f} {abs(y[0])**2:8.4f} {I.real:+9.4f} {I.imag:+9.4f} {y[7].real:+8.4f} {y[7].imag:+8.4f}  {Rv.real:+8.3f}{Rv.imag:+8.3f}i")
    return out
ex=first_two_extrema(c3db,e); print("DB extrema (tau):",ex)
tau_p,tau_n=ex[0],ex[1]
res={}
res['sphere']=continue_from(-1/6,e,np.pi/2,3.0,n=12,label="sphere from equator")
res['db_neck']=continue_from(c3db,e,tau_n,0.7,n=14,label="double bubble from neck")
res['db_peak']=continue_from(c3db,e,tau_p,3.0,n=15,label="double bubble from first peak")
res['db_peak_minus']=continue_from(c3db,e,tau_p,1.5,n=6,direction=-1j,label="double bubble from first peak, conjugate direction")
# perturbed spheres from their peak (K=0, a''' != 0)
for dc in (1e-3,-1e-3,1e-3j):
    c3=-1/6+dc; exs=first_two_extrema(c3,e) if abs(dc.imag)==0 else None
    if exs:
        res[f'sphere+{dc}']=continue_from(c3,e,exs[0],3.0,n=6,label=f"perturbed sphere c3=-1/6+{dc} from its peak (tau_p={exs[0]:.4f})")
pickle.dump(res,open('continuations.pkl','wb'))
