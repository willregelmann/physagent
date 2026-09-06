import numpy as np
from scipy.optimize import brentq
import ccaps
from ccaps import *
e=1.0; c3db=-0.349489
# generalize the pole start: theta0 = C*t0 (boost freedom of the conformal map to S^4)
def y0_C(c3,e,t0,C):
    y=y0_of(c3,e,t0); y[4]=C*t0; return y
def integrate_C(c3,e,path,C,t0=2e-3,events=None,dense=False):
    y=y0_C(c3,e,t0,C); pts=[t0+0j]+[complex(p) for p in path]; sols=[]
    for i in range(len(pts)-1):
        z0,z1=pts[i],pts[i+1]; dz=z1-z0
        f=lambda s,Y: dz*dens(Y,e)
        ev=[]
        if events:
            for g in events:
                h=lambda s,Y,g=g: g(z0+s*dz,Y); h.terminal=getattr(g,'terminal',False); h.direction=getattr(g,'direction',0); ev.append(h)
        from scipy.integrate import solve_ivp
        sol=solve_ivp(f,(0,1),y,method='DOP853',rtol=1e-10,atol=1e-13,events=ev or None,dense_output=dense)
        sols.append((z0,dz,sol)); y=sol.y[:,-1]
        if sol.status==1: break
    return y,sols
close=lambda z,Y: Y[0].real-2e-3; close.terminal=True; close.direction=-1
ext=lambda z,Y: Y[1].real; ext.direction=0
print("(a) boost-independence of the closed double bubble's anomaly action Gamma_full:")
for C in (0.5,1.0,2.0,4.0):
    y,sols=integrate_C(c3db,e,[12.0],C,events=[ext,close],dense=True); z0,dz,sol=sols[0]
    Yn=sol.y_events[0][1]; 
    print(f"   C={C}: theta(neck)={Yn[4].real:.5f}  Gamma(to neck)={Yn[6].real:+.5f}  Gamma_full={y[6].real:+.5f}  I_full={(y[5]+y[6]).real:+.5f}  theta_end={y[4].real:.5f}")
print("(b) symmetric frame: choose C so that theta(neck)=pi/2")
def th_neck(C):
    y,sols=integrate_C(c3db,e,[12.0],C,events=[ext,close],dense=True); return sols[0][2].y_events[0][1][4].real-np.pi/2
Cs=brentq(th_neck,0.05,1.0,xtol=1e-10); print(f"   C_sym={Cs:.6f}")
y,sols=integrate_C(c3db,e,[12.0],Cs,events=[ext,close],dense=True); z0,dz,sol=sols[0]
Yp,Yn=sol.y_events[0][0],sol.y_events[0][1]; tau_n=(z0+sol.t_events[0][1]*dz).real
print(f"   theta(neck)={Yn[4].real:.6f}  I(to neck)={(Yn[5]+Yn[6]).real:+.5f}  I_full/2={(y[5]+y[6]).real/2:+.5f}   [I_loc half {Yn[5].real:+.5f} vs {y[5].real/2:+.5f}; Gamma half {Yn[6].real:+.5f} vs {y[6].real/2:+.5f}]")
print("(c) Re I along the real recollapsing continuation from the neck, symmetric frame:")
for t in (0.1,0.2,0.3,0.4,0.5,0.55,0.6):
    yy,_=integrate_C(c3db,e,[tau_n,tau_n+1j*t],Cs)
    print(f"   t={t:.2f}: a={yy[0].real:+.4f}{yy[0].imag:+.1e}i  Re I={(yy[5]+yy[6]).real:+.5f}  Im I={(yy[5]+yy[6]).imag:+.4f}  theta={yy[4].real:.4f}{yy[4].imag:+.4f}i")
print("(d) sphere in a boosted frame C=2: half action to the equator and full:")
y,sols=integrate_C(-1/6,e,[12.0],2.0,events=[ext,close],dense=True); z0,dz,sol=sols[0]; Yp=sol.y_events[0][0]
print(f"   theta(equator)={Yp[4].real:.5f}  I(to equator)={(Yp[5]+Yp[6]).real:+.5f} (C=1 gives -3.66667)  I_full={(y[5]+y[6]).real:+.5f} (expect -7.33333)")
