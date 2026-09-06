import numpy as np, sys
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
sys.path.insert(0,'..')
from ccaps import FE, Rf, c5f, c7f
src=open('../../j1/caps.py').read().split("res={}")[0]; exec(src)   # run(), neck_a3()
c3star={0.36:-0.347204,0.40:-0.350687,0.45:-0.353077,0.5:-0.354147,1.0:-0.349489,2.0:-0.342261,5.0:-0.337009,10.0:-0.335180}
for e,br in ((20.0,(-0.345,-0.325)),(50.0,(-0.345,-0.325))):
    grid=np.linspace(br[0],br[1],9); vals=[neck_a3(c,e) for c in grid]; bb=None
    for i in range(len(grid)-1):
        if np.isfinite(vals[i]) and np.isfinite(vals[i+1]) and vals[i]*vals[i+1]<0: bb=(grid[i],grid[i+1]); break
    if bb: c3star[e]=brentq(neck_a3,bb[0],bb[1],args=(e,),xtol=1e-9); print(f"eps={e}: c3*={c3star[e]:.6f}")
    else: print(f"eps={e}: no bracket; vals={vals}")
def open_run(c3,e,T=200.0,t0=2e-3):
    C5,C7=c5f(c3,e),c7f(c3,e); tau0=1j*t0
    y0=np.array([tau0+c3*tau0**3+C5*tau0**5+C7*tau0**7, 1+3*c3*tau0**2+5*C5*tau0**4+7*C7*tau0**6, 6*c3*tau0+20*C5*tau0**3+42*C7*tau0**5, 6*c3+60*C5*tau0**2+210*C7*tau0**4],dtype=complex)
    rhs=lambda t,y: 1j*np.array([y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e)],dtype=complex)
    big=lambda t,y: abs(Rf(y[0],y[1],y[2]))-1e6; big.terminal=True
    return solve_ivp(rhs,(t0,T),y0,method='DOP853',rtol=1e-10,atol=1e-13,events=[big],dense_output=True)
print("Open (pole) continuation of the symmetric double bubble: e-folds ln a accumulated before R reaches Mbar_P^2 and M_P^2 (a2=1e6: 70.4, 1768; a2=1e7: 704, 17684), H/H0 there, and the time of the curvature singularity")
print(" eps   c3*        t(Mbar,1e6) lna   H   | t(M_P,1e6) lna   H  | t(Mbar,1e7) lna  | t_sing  lna_sing  | H range on branch | Re b max")
rows={}
for e in sorted(c3star):
    s=open_run(c3star[e],e); tt=np.linspace(s.t[0],s.t[-1],200001); Y=s.sol(tt)
    a=Y[0].imag; H=Y[1].real/a; Rv=np.array([Rf(Y[0][i],Y[1][i],Y[2][i]).real for i in range(0,len(tt),50)]); ti=tt[::50]; lna=np.log(a)
    def cross(thr):
        k=np.argmax(Rv>thr)
        if Rv[k]<=thr: return None
        return ti[k],np.interp(ti[k],tt,lna),np.interp(ti[k],tt,H)
    c1,c2,c3_=cross(70.4),cross(1768.0),cross(704.0)
    fmt=lambda c: f"{c[0]:6.2f} {c[1]:5.1f} {c[2]:5.2f}" if c else "   -      -    -  "
    print(f"{e:5.2f} {c3star[e]:+.6f}  {fmt(c1)} | {fmt(c2)} | {fmt(c3_)[:12]} | {s.t[-1]:6.2f} {lna[-1]:6.1f} | {H[len(H)//100]:.2f}..{H[-1]:.1f} | {np.abs(Y[0].real).max():.1e}")
    rows[e]=(c1,c2)
# interpolate the eps at which ln a at R=Mbar_P^2 (a2=1e6) reaches 60
es=[e for e in rows if rows[e][0]]; ns=[rows[e][0][1] for e in es]
print("N_open(Mbar_P, a2=1e6) vs eps:",[(e,round(n,1)) for e,n in zip(es,ns)])
