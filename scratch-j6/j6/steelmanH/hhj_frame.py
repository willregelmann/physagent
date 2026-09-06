# Herzog-Huang-Jensen a-type Wess-Zumino functional (their eq. 126) on the unit S^4 reference, FRW-reduced, with the boundary term,
# tested against (i) the position's closed-cap Gamma, (ii) Moebius invariance, (iii) the WZ cocycle under a change of boost frame C.
import numpy as np, sys
from scipy.integrate import solve_ivp, trapezoid
sys.path.insert(0,'..')
from ccaps import *
e=1.0; c3db=-0.349489
def dens9(y,e):
    A,A1_,A2_,A3_,th=y[:5]; A4_=FE(A,A1_,A2_,A3_,e); thp=np.sin(th)/A
    L_EH=-(6/(16*np.pi**2))*A*(1+A1_**2); L_R2=36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2_-A1_**2)**2/A
    s=np.log(A/np.sin(th)); sth=(A1_-np.cos(th))/np.sin(th)
    sthth=A*A2_/np.sin(th)**2+1-(A1_-np.cos(th))*np.cos(th)/np.sin(th)**2
    box=sthth+3*np.cos(th)/np.sin(th)*sth
    G=(1/8)*np.sin(th)**3*(24*s+2*box**2+4*sth**2)*thp                       # position's Riegert/S^4 density
    GKS=(1/8)*np.sin(th)**3*(24*s+12*sth**2+8*sthth*sth**2-2*sth**4)*thp     # HHJ/KS bulk density, tau=-sigma
    return np.array([A1_,A2_,A3_,A4_,thp,2*np.pi**2*(L_EH+L_R2),G,A,GKS],dtype=complex)
def run_C(c3,e,tau_end,C,t0=2e-3,events=None):
    y=np.zeros(9,dtype=complex); y[:8]=y0_of(c3,e,t0); y[4]=C*t0
    sol=solve_ivp(lambda s,Y: (tau_end-t0)*dens9(Y,e),(0,1),y,method='DOP853',rtol=1e-10,atol=1e-13,events=events,dense_output=True)
    return sol,t0
def bdy(sig,sth,th1):
    k=1/np.tan(th1); Q4=8*k**3-24*k/np.sin(th1)**2
    return (1/8)*np.sin(th1)**3*(-sig*Q4-(8/3)*sth**3)
ext=lambda s,Y: Y[1].real; ext.direction=0
close=lambda s,Y: Y[0].real-2e-3; close.terminal=True; close.direction=-1
print("(i) closed caps, KS bulk (no boundary) vs position's Gamma_full; and Moebius test on the round sphere in frames C:")
for c3,lab in ((-1/6,'sphere'),(c3db,'double bubble eps=1')):
    for C in (0.5,1.0,2.0):
        sol,t0=run_C(c3,e,12.0,C,events=[ext,close]); y=sol.y[:,-1]
        print(f"   {lab:20s} C={C}: theta_end={y[4].real:.5f}  Gamma_pos={y[6].real:+.5f}  Gamma_KS={y[8].real:+.5f}  diff={(y[8]-y[6]).real:+.5f}  I_R2={y[5].real+2:+.5f}(R2 part of I_loc)")
print("(ii) partial double bubble to the neck: bulk-only (position), HHJ bulk+boundary, and the cocycle-invariant Gamma[sigma_C]-Gamma[omega_C]:")
Cs=0.298429
def cap_to_neck(C):
    sol,t0=run_C(c3db,e,6.0,C,events=[ext]); s_n=sol.t_events[0][1]; tau_n=t0+s_n*(6.0-t0)
    return sol,t0,tau_n
sol_s,t0,tau_n=cap_to_neck(Cs)
ss=np.linspace(0,(tau_n-t0)/(6.0-t0),40001); tau=t0+ss*(6.0-t0)
Ys=sol_s.sol(ss); th_s=Ys[4].real
ref=None
for C in (Cs,0.5,1.0,2.0,4.0):
    sol,_,_=cap_to_neck(C); Y=sol.sol(ss); th=Y[4].real; A,A1,A2=Y[0].real,Y[1].real,Y[2].real
    thp=np.sin(th)/A
    sig=np.log(A/np.sin(th)); sth=(A1-np.cos(th))/np.sin(th); sthth=A*A2/np.sin(th)**2+1-(A1-np.cos(th))*np.cos(th)/np.sin(th)**2
    bulk_sig=trapezoid((1/8)*np.sin(th)**3*(24*sig+12*sth**2+8*sthth*sth**2-2*sth**4)*thp,tau)
    G_sig=bulk_sig+bdy(sig[-1],sth[-1],th[-1])
    # omega_C = ln(sin theta_s / sin theta_C) as a function on D_C
    om=np.log(np.sin(th_s)/np.sin(th)); om_t=np.gradient(om,tau); om_th=om_t/thp; om_thth=np.gradient(om_th,tau)/thp
    bulk_om=trapezoid((1/8)*np.sin(th)**3*(24*om+12*om_th**2+8*om_thth*om_th**2-2*om_th**4)*thp,tau)
    G_om=bulk_om+bdy(om[-1],om_th[-1],th[-1])
    inv=G_sig-G_om
    if ref is None: ref=inv
    print(f"   C={C:.6f}: theta(neck)={th[-1]:.5f}  Gamma_pos(bulk only)={Y[6].real[-1] if False else sol.sol(ss[-1])[6].real:+.5f}  Gamma_KS bulk={bulk_sig:+.5f} +bdy={G_sig-bulk_sig:+.5f} = {G_sig:+.5f} | Gamma_KS[omega_C]={G_om:+.5f} | invariant Gamma[sigma_C]-Gamma[omega_C]={inv:+.5f} (dev from C_sym: {inv-ref:+.1e})")
print("(iii) same test for the round sphere cut at its equator (expect invariant = 0):")
def sphere_to_eq(C):
    sol,t0=run_C(-1/6,e,6.0,C,events=[ext]); s_e=sol.t_events[0][0]; return sol,t0,t0+s_e*(6.0-t0)
sol_s,t0,tau_e=sphere_to_eq(1.0); ss=np.linspace(0,(tau_e-t0)/(6.0-t0),40001); tau=t0+ss*(6.0-t0); th_s=sol_s.sol(ss)[4].real
for C in (1.0,0.5,2.0,4.0):
    sol,_,_=sphere_to_eq(C); Y=sol.sol(ss); th=Y[4].real; A,A1,A2=Y[0].real,Y[1].real,Y[2].real; thp=np.sin(th)/A
    sig=np.log(A/np.sin(th)); sth=(A1-np.cos(th))/np.sin(th); sthth=A*A2/np.sin(th)**2+1-(A1-np.cos(th))*np.cos(th)/np.sin(th)**2
    G_sig=trapezoid((1/8)*np.sin(th)**3*(24*sig+12*sth**2+8*sthth*sth**2-2*sth**4)*thp,tau)+bdy(sig[-1],sth[-1],th[-1])
    om=np.log(np.sin(th_s)/np.sin(th)); om_th=np.gradient(om,tau)/thp; om_thth=np.gradient(om_th,tau)/thp
    G_om=trapezoid((1/8)*np.sin(th)**3*(24*om+12*om_th**2+8*om_thth*om_th**2-2*om_th**4)*thp,tau)+bdy(om[-1],om_th[-1],th[-1])
    print(f"   C={C}: theta(eq)={th[-1]:.5f}  Gamma_pos(bulk)={sol.sol(ss[-1])[6].real:+.5f}  Gamma_KS[sigma_C]={G_sig:+.5f}  Gamma_KS[omega_C]={G_om:+.5f}  invariant={G_sig-G_om:+.5f}")
print("(iv) generic (K != 0) cut of the double bubble at tau=1.6 (between peak and neck): invariant across frames")
def cap_to(C,tau1):
    sol,t0=run_C(c3db,e,tau1,C); return sol,t0
sol_s,t0=cap_to(Cs,1.6); ss=np.linspace(0,1,40001); tau=t0+ss*(1.6-t0); th_s=sol_s.sol(ss)[4].real
for C in (Cs,0.5,1.0,2.0):
    sol,_=cap_to(C,1.6); Y=sol.sol(ss); th=Y[4].real; A,A1,A2=Y[0].real,Y[1].real,Y[2].real; thp=np.sin(th)/A
    sig=np.log(A/np.sin(th)); sth=(A1-np.cos(th))/np.sin(th); sthth=A*A2/np.sin(th)**2+1-(A1-np.cos(th))*np.cos(th)/np.sin(th)**2
    b_sig=trapezoid((1/8)*np.sin(th)**3*(24*sig+12*sth**2+8*sthth*sth**2-2*sth**4)*thp,tau); G_sig=b_sig+bdy(sig[-1],sth[-1],th[-1])
    om=np.log(np.sin(th_s)/np.sin(th)); om_th=np.gradient(om,tau)/thp; om_thth=np.gradient(om_th,tau)/thp
    G_om=trapezoid((1/8)*np.sin(th)**3*(24*om+12*om_th**2+8*om_thth*om_th**2-2*om_th**4)*thp,tau)+bdy(om[-1],om_th[-1],th[-1])
    print(f"   C={C:.6f}: theta1={th[-1]:.5f} K1=a'/a={A1[-1]/A[-1]:.4f}  Gamma_pos(bulk)={sol.sol(ss[-1])[6].real:+.5f}  Gamma_KS bulk={b_sig:+.5f} bdy={G_sig-b_sig:+.5f}  invariant={G_sig-G_om:+.5f}")
