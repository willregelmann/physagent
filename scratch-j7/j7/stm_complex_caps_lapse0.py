# constant-lapse test for the six complex caps found at (a,v)=(2,-3.5978), eps=1 (stm_complex_caps_0.out)
import numpy as np, sys
from scipy.integrate import solve_ivp
sys.path.insert(0,'..')
from ccaps import FE, Rf, y0_of, integrate_path
e=1.0; a1,v1=2.0,-3.5978
caps=[(-0.055830-0.119030j,1.61488+9.04540j,-50.6029),(-0.055830+0.119030j,1.61488-9.04540j,-50.6029),
      (-0.541815-0.272128j,2.31165-4.06617j,+38.6508),(-0.541815+0.272128j,2.31165+4.06617j,+38.6508),
      (0.163547+0.355949j,-0.57993+2.05280j,+38.6897),(0.163547-0.355949j,-0.57993-2.05280j,+38.6897)]
def lapse_geom(c3,e,NE):
    ts=1e-5; tau0=np.sqrt(2*NE*ts+0j)
    if tau0.real<0: tau0=-tau0
    y0=y0_of(c3,e,tau0)[:4]
    def rhs(t,Y):
        a,a1_,a2,a3,tau=Y; dtau=NE/a
        return [a1_*dtau,a2*dtau,a3*dtau,FE(a,a1_,a2,a3,e)*dtau,dtau]
    Y0=np.array(list(y0)+[tau0],dtype=complex)
    sol=solve_ivp(rhs,(ts,1.0),Y0,method='DOP853',rtol=1e-10,atol=1e-13,dense_output=True)
    tt=np.linspace(ts,1.0,4001); Y=sol.sol(tt); amin=np.abs(Y[0]).min()
    return sol.y[:,-1],amin
for c3,T,ReI in caps:
    y,_=integrate_path(c3,e,[T]); NE=y[7]
    yl,amin=lapse_geom(c3,e,NE); cl=abs(yl[0]-a1)<1e-3 and abs(yl[1]-v1)<1e-3
    print(f"c3={c3:.6f} T={T:.5f} Re I_inv={ReI:+.3f} N_E={NE:.4f} | straight end a={y[0]:.4f} v={y[1]:.4f} | t-path end a={yl[0]:.4f} v={yl[1]:.4f} tau(1)={yl[4]:.4f} | constant-lapse: {'YES' if cl else 'NO'} | min|a|={amin:.4f}")
