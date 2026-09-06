import numpy as np
from scipy.integrate import solve_ivp
from ccaps import *
e=1.0
def y0_C(c3,e,t0,C):
    y=y0_of(c3,e,t0); y[4]=C*t0; return y
def integrate_C(c3,path,C,t0=2e-3):
    y=y0_C(c3,e,t0,C); pts=[t0+0j]+[complex(p) for p in path]
    for i in range(len(pts)-1):
        z0,z1=pts[i],pts[i+1]; dz=z1-z0
        sol=solve_ivp(lambda s,Y: dz*dens(Y,e),(0,1),y,method='DOP853',rtol=1e-10,atol=1e-13); y=sol.y[:,-1]
    return y
# the position's (4,20) saddle: c3=-0.24824-0.03924i, tau1=1.26984+1.19625i (dbsaddle.out), path via min(Re tau1, 1.185)
c3=-0.24824-0.03924j; tau1=1.26984+1.19625j; path=[1.185,tau1]
for C in (0.3,1.0,3.0):
    y=integrate_C(c3,path,C)
    print(f"C={C}: a={y[0]:.4f} R={Rf(y[0],y[1],y[2]):.4f}  I_loc={y[5]:.4f}  Gamma={y[6]:.4f}  Re I={(y[5]+y[6]).real:+.4f}")
# sphere at (4,12) for reference in the same frames
for C in (0.3,1.0,3.0):
    y=integrate_C(-1/6,[np.pi/2,np.pi/2+1j*np.arccosh(2.0)],C)
    print(f"sphere C={C}: a={y[0]:.4f} Re I={(y[5]+y[6]).real:+.4f} (I_loc {y[5].real:+.4f}, Gamma {y[6].real:+.4f})")
