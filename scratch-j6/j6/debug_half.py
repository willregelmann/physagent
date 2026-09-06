import numpy as np
from ccaps import *
e=1.0; c3=-0.349489
ext=lambda z,Y: Y[1].real; ext.direction=0
close=lambda z,Y: Y[0].real-1e-3; close.terminal=True; close.direction=-1
y,sols=integrate_path(c3,e,[12.0],events=[ext,close],dense=True)
z0,dz,sol=sols[0]
for s_ev,Y in zip(sol.t_events[0],sol.y_events[0]):
    print(f"extremum at tau={(z0+s_ev*dz).real:.4f}: a={Y[0].real:.4f} theta={Y[4].real:.5f} (pi/2={np.pi/2:.5f}) I_loc={Y[5].real:+.5f} Gamma={Y[6].real:+.5f} N={Y[7].real:.4f}")
Yf=sol.y[:,-1]; print(f"close at tau={(z0+sol.t[-1]*dz).real:.4f}: a={Yf[0].real:.4e} theta={Yf[4].real:.5f} I_loc={Yf[5].real:+.5f} Gamma={Yf[6].real:+.5f}")
# density profile of the R2 and EH parts vs tau, to see symmetry
ts=np.linspace(0,sol.t[-1],9); 
for s in ts:
    Y=sol.sol(s); A,A1_,A2_=Y[0].real,Y[1].real,Y[2].real
    print(f"  tau={(z0+s*dz).real:.3f} a={A:.4f} a'={A1_:+.4f} R2dens={(1-A*A2_-A1_**2)**2/A:+.4f} EHdens={A*(1+A1_**2):+.4f} theta={Y[4].real:.4f}")
