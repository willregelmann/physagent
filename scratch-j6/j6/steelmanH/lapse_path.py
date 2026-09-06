# Constant-lapse geometry test: for a saddle (c3, tau1, N_E), integrate the cap along the t-path defined by dtau/dt = N_E/a(tau), t in [t0,1].
# If the endpoint reproduces (q1,R1) the saddle is a constant-lapse (DTL/FLT-type) geometry; the minimum of |a| along the path says
# whether the geometry approaches zero size in its interior (DTL's 'singular geometries').
import numpy as np, sys
from scipy.integrate import solve_ivp
sys.path.insert(0,'..')
from ccaps import FE, Rf, c5f, c7f, y0_of
def lapse_geom(c3,e,NE,t0=2e-3):
    ts=1e-5; tau0=np.sqrt(2*NE*ts+0j)
    if tau0.real<0: tau0=-tau0
    y0=y0_of(c3,e,tau0)[:4]
    def rhs(t,Y):
        a,a1,a2,a3,tau=Y; dtau=NE/a
        return [a1*dtau,a2*dtau,a3*dtau,FE(a,a1,a2,a3,e)*dtau,dtau]
    Y0=np.array(list(y0)+[tau0],dtype=complex)
    sol=solve_ivp(rhs,(ts,1.0),Y0,method='DOP853',rtol=1e-10,atol=1e-13,dense_output=True)
    tt=np.linspace(ts,1.0,4001); Y=sol.sol(tt); amin=np.abs(Y[0]).min(); imin=np.argmin(np.abs(Y[0]))
    y=sol.y[:,-1]
    return y,amin,tt[imin],Y[4][imin],sol.status
cases=[("sphere eps=1 (4,12)",-1/6,1.0,1.0+1.7321j,np.pi/2+1.31696j),
       ("complex pair eps=1 (4,12)",-0.885788-0.478724j,1.0,1.5343+1.6561j,2.73251+1.13928j),
       ("complex pair conj eps=1",-0.885788+0.478724j,1.0,1.5343-1.6561j,2.73251-1.13928j),
       ("real-Euclidean cap eps=1 (4,12)",-0.004475,1.0,12.9519+0j,5.70887+0j),
       ("(4,20) perturbed-sphere-like eps=1",-0.248238-0.039235j,1.0,0.6829+1.4194j,1.26984+1.19625j)]
# pair at eps=0.3 and 0.355: recompute N_E along the [1.185,tau1] path first
from ccaps import integrate_path
for e,c3,t1 in ((0.30,-0.204602-0.818542j,2.46994+0.91183j),(0.355,-0.348717-0.807122j,2.52608+0.95325j)):
    y,_=integrate_path(c3,e,[1.185,t1]); cases.append((f"complex pair eps={e} (4,12)",c3,e,y[7],t1))
    y,_=integrate_path(-1/6,e,[np.pi/2,np.pi/2+1.31696j]); cases.append((f"sphere eps={e} (4,12)",-1/6,e,y[7],np.pi/2+1.31696j))
for lab,c3,e,NE,t1 in cases:
    y,amin,tmin,taumin,st=lapse_geom(c3,e,NE)
    print(f"{lab:36s} N_E={NE:.4f}: tau(1)={y[4]:.5f} (saddle tau1={t1:.5f})  q(1)={y[0]**2:.4f}  R(1)={Rf(y[0],y[1],y[2]):.4f}  min|a| on path={amin:.4f} at t={tmin:.3f} (tau={taumin:.3f})  status={st}")
