# STEELMAN flaw 8: constant-lapse (sheet) test of steelman H for the twelve evaluated census saddles at (a,v)=(3,-i sqrt8), eps=1.
# For each saddle: N_E = int a dtau along the straight pole->T path (= y[7]); then integrate dtau/dt = N_E/a from the pole to t=1
# (lapse_path.py's criterion) and check whether (a(1), a'(1)) reproduce (3, -i sqrt8).  Report min|a| along the t-path.
import numpy as np, sys
from scipy.integrate import solve_ivp
sys.path.insert(0,'..')
from ccaps import FE, Rf, y0_of, integrate_path
e=1.0
sad={'sphere':(-0.166667-0.000000j,1.570796+1.762747j),'A':(-0.061078-0.074741j,0.958365-7.517934j),'B':(-0.078012-0.080863j,3.646649-7.552073j),
'C':(0.011760-0.000057j,-6.007494-4.176755j),'D':(0.006200+0.006758j,4.931966+3.047997j),'E':(-0.160805+0.117255j,-4.089197-8.820504j),
'F':(-0.024640+0.090852j,2.969438-8.244251j),'G':(-0.073135-0.070948j,2.275652-14.632213j),'H':(-0.074380-0.093827j,0.233795+9.329840j),
'K':(-0.067834+0.076298j,-6.494782-10.376287j),'L':(-0.041756-0.168680j,0.644368+8.539119j),'S':(-0.024619+0.074912j,-6.323142+10.106159j)}
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
    return sol.y[:,-1],amin,tt[imin],Y[4][imin],sol.status
target=(3.0,-1j*np.sqrt(8))
print("=== constant-lapse test, census saddles at (3,-i sqrt8), eps=1; straight path N_E = int a dtau ===")
for nm,(c3,T) in sad.items():
    y,_=integrate_path(c3,e,[T]); NE=y[7]
    yy,amin,tmin,taumin,st=lapse_geom(c3,e,NE)
    ok=abs(yy[0]-target[0])<1e-3 and abs(yy[1]-target[1])<1e-3
    print(f"{nm:7s} c3={c3:.6f} T={T:.6f} N_E={NE:.4f} | straight-path end a={y[0]:.4f} v={y[1]:.4f} | lapse-path end tau(1)={yy[4]:.4f} a(1)={yy[0]:.4f} v(1)={yy[1]:.4f} R(1)={Rf(yy[0],yy[1],yy[2]):.3f} | constant-lapse: {'YES' if ok else 'NO'} | min|a| on t-path={amin:.4f} at t={tmin:.3f} status={st}",flush=True)
