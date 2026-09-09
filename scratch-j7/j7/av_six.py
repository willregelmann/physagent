# Gauge repair (few complex C seeds) + constant-lapse test for the six census saddles sym_C could not gauge (I, J, M, N, O, P).
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
exec(open('stm_lapse_census.py').read().split("target=(3.0")[0].split("def lapse_geom")[1].join(["def lapse_geom",""]) if False else "")
from scipy.integrate import solve_ivp
def lapse_geom(c3,e,NE,t0=2e-3):
    ts=1e-5; tau0=np.sqrt(2*NE*ts+0j)
    if tau0.real<0: tau0=-tau0
    y0=y0_of(c3,e,tau0)[:4]
    def rhs(t,Y):
        a,a1,a2,a3,tau=Y; dtau=NE/a
        return [a1*dtau,a2*dtau,a3*dtau,FE(a,a1,a2,a3,e)*dtau,dtau]
    Y0=np.array(list(y0)+[tau0],dtype=complex)
    sol=solve_ivp(rhs,(ts,1.0),Y0,method='DOP853',rtol=1e-10,atol=1e-13)
    return sol.y[:,-1]
e=1.0
six={'I':(-0.103854-0.087970j,-10.389552+3.304918j),'J':(-0.067485+0.073246j,4.536903+10.252188j),'M':(-0.099604-0.091109j,11.524847-8.253794j),
'N':(-0.071493-0.074147j,3.927697-16.782805j),'O':(-0.091483+0.095266j,-7.733206-8.265503j),'P':(0.038850+0.108716j,-1.880350+6.600720j)}
def gauge(c3,T,C0,it=50):
    def f(C):
        y=run_path(c3,e,[T],C); v=y[4]-np.pi/2
        return (v if np.isfinite(v) else None),y
    a,b=complex(C0),complex(C0)*1.05; fa,_=f(a); fb,_=f(b)
    if fa is None or fb is None: return None
    for k in range(it):
        if fb==fa: return None
        c=b-fb*(b-a)/(fb-fa); fc,y=f(c)
        if fc is None or not np.isfinite(abs(c)) or abs(c)>1e4 or abs(c)<1e-6: return None
        a,fa,b,fb=b,fb,c,fc
        if abs(fc)<1e-10: return c,y
    return None
target=(3.0,-1j*np.sqrt(8))
for nm,(c3,T) in six.items():
    y,_=integrate_path(c3,e,[T]); NE=y[7]
    yy=lapse_geom(c3,e,NE); ok=abs(yy[0]-target[0])<1e-3 and abs(yy[1]-target[1])<1e-3
    res=None
    for r in (1.0,0.3,3.0,0.1):
        for ph in (0,np.pi/4,-np.pi/4,np.pi/2,-np.pi/2,np.pi,3*np.pi/4,-3*np.pi/4):
            res=gauge(c3,T,r*np.exp(1j*ph))
            if res: break
        if res: break
    if res:
        C,yg=res; Iinv=yg[5]+yg[6]*3*e/(3*e+1)+yg[9]-(1/3)*yg[1]**3
        print(f"{nm}: gauge C*={C:.5f}  I_inv={Iinv:.4f} Re={Iinv.real:+.4f} | N_E={NE:.4f} | constant-lapse: {'YES' if ok else 'NO'} (t-path end a={yy[0]:.4f} v={yy[1]:.4f})",flush=True)
    else:
        print(f"{nm}: no gauge found from 32 seeds | N_E={NE:.4f} | constant-lapse: {'YES' if ok else 'NO'} (t-path end a={yy[0]:.4f} v={yy[1]:.4f})",flush=True)
