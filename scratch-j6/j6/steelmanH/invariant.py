# Frame-invariant partial action: I_inv = I_loc' + Gamma_KS[sigma; frame with theta(cut)=pi/2] - (1/3) a'(cut)^3,
# where Gamma_KS is the HHJ/KS a-anomaly WZ bulk functional (pure E4 anomaly), the boundary term is HHJ eq.126's at theta1=pi/2
# (Q4=0 there, tau_n^3 term survives), and I_loc' = I_EH + I_R2*3eps/(3eps+1) moves the Riegert -(2/3)boxR scheme term out of
# the anomaly functional (Gamma_pos = Gamma_KS + (1/288pi^2) int sqrt g R^2 up to a cap-independent constant, verified in hhj_frame.out).
# I_inv is defined up to one universal constant (W[S^4-ref; hemisphere]); differences between caps/cuts are physical.
import numpy as np, sys
from scipy.integrate import solve_ivp
sys.path.insert(0,'..')
from ccaps import *
def dens10(y,e):
    A,A1_,A2_,A3_,th=y[:5]; A4_=FE(A,A1_,A2_,A3_,e); thp=np.sin(th)/A
    L_EH=-(6/(16*np.pi**2))*A*(1+A1_**2); L_R2=36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2_-A1_**2)**2/A
    s=np.log(A/np.sin(th)); sth=(A1_-np.cos(th))/np.sin(th)
    sthth=A*A2_/np.sin(th)**2+1-(A1_-np.cos(th))*np.cos(th)/np.sin(th)**2
    box=sthth+3*np.cos(th)/np.sin(th)*sth
    G=(1/8)*np.sin(th)**3*(24*s+2*box**2+4*sth**2)*thp
    GKS=(1/8)*np.sin(th)**3*(24*s+12*sth**2+8*sthth*sth**2-2*sth**4)*thp
    return np.array([A1_,A2_,A3_,A4_,thp,2*np.pi**2*L_EH,2*np.pi**2*L_R2,G,A,GKS],dtype=complex)
def run_path(c3,e,path,C,t0=2e-3):
    y=np.zeros(10,dtype=complex); y[:8]=y0_of(c3,e,t0); y[4]=C*t0
    pts=[t0+0j]+[complex(p) for p in path]
    for i in range(len(pts)-1):
        z0,z1=pts[i],pts[i+1]; dz=z1-z0
        sol=solve_ivp(lambda s,Y: dz*dens10(Y,e),(0,1),y,method='DOP853',rtol=1e-10,atol=1e-13); y=sol.y[:,-1]
    return y
def sym_C(c3,e,path,C0=1.0,C1=0.8,it=40):
    def f(C):
        y=run_path(c3,e,path,C); v=y[4]-np.pi/2
        return v if np.isfinite(v) else None
    a,b=complex(C0),complex(C1); fa,fb=f(a),f(b)
    if fa is None or fb is None: a,b=0.5+0j,0.4+0j; fa,fb=f(a),f(b)
    for k in range(it):
        step=-fb*(b-a)/(fb-fa)
        if abs(step)>0.5*abs(b): step*=0.5*abs(b)/abs(step)
        c=b+step; fc=f(c); tries=0
        while fc is None and tries<6:
            step*=0.5; c=b+step; fc=f(c); tries+=1
        if fc is None: return b
        a,fa,b,fb=b,fb,c,fc
        if abs(fc)<1e-11: return c
    print("   [sym_C: not converged, |f|=%.1e]"%abs(fb)); return b
def inv(c3,e,path,label=""):
    C=sym_C(c3,e,path); y=run_path(c3,e,path,C)
    A,A1=y[0],y[1]; Iloc=y[5]+y[6]; Ilocp=y[5]+y[6]*3*e/(3*e+1)
    bdy=-(1/3)*A1**3
    Iinv=Ilocp+y[9]+bdy
    Rv=Rf(y[0],y[1],y[2])
    print(f"{label:44s} C*={C:.4f} theta1={y[4]:.4f} a={A:.4f} R={Rv:.3f} K={A1/A:.4f} | I_loc={Iloc:.4f} | Gamma_KS(sym)={y[9]:.4f} bdy={bdy:.4f} | I_inv={Iinv:.4f}  Re I_inv={Iinv.real:+.5f}")
    return Iinv
e=1.0; c3db=-0.349489; tau_n=2.10590; tau_p=1.18499
print("=== (a) sphere de Sitter continuation from the equator (expect Re I_inv frozen at I_S4/2 = -3.66667 + const):")
for t in (0.0,0.5,1.0,1.5,2.0,3.0):
    inv(-1/6,e,[np.pi/2,np.pi/2+1j*t] if t>0 else [np.pi/2],f"sphere t={t}")
print("=== (b) double bubble neck continuation (expect Re I_inv frozen):")
for t in (0.0,0.1,0.3,0.5,0.55):
    inv(c3db,e,[tau_p,tau_n,tau_n+1j*t] if t>0 else [tau_p,tau_n],f"DB neck t={t}")
print("=== (c) perturbed spheres from their K=0 peak (attack flaw 11: bulk-only Re I drifted by O(1)):")
ext=lambda z,Y: Y[1].real; ext.direction=0
for dc in (1e-3,-1e-3):
    c3=-1/6+dc; y,sols=integrate_path(c3,e,[6.0],events=[ext],dense=True); z0,dz,sol=sols[0]; tp=(z0+sol.t_events[0][0]*dz).real
    for t in (0.0,1.0,2.0,3.0):
        inv(c3,e,[tp,tp+1j*t] if t>0 else [tp],f"sphere+{dc:+.0e} t={t}")
print("=== (d) saddles at (q1,R1)=(4,12):")
inv(-1/6,e,[np.pi/2,np.pi/2+1j*np.arccosh(2.0)],"sphere dS (4,12)")
inv(-0.885788-0.478724j,e,[1.185,2.73251+1.13928j],"complex pair (4,12)")
inv(-0.004475,e,[5.70887],"real-Euclidean recontracting cap (4,12)")
print("=== (e) saddles at (4,20):")
inv(-0.248238-0.039235j,e,[1.185,1.26984+1.19625j],"(4,20) perturbed-sphere-like")
inv(-0.185677-0.089761j,e,[1.185,3.91571+0.78925j],"(4,20) second complex")
inv(-0.001524,e,[6.98753],"(4,20) real-Euclidean")
print("=== (f) neck-data saddles (0.311894, 8.49375):")
inv(c3db,e,[tau_p,tau_n],"DB at neck")
inv(-0.381507,e,[1.185,1.98813],"asymmetric neighbour at neck data")
inv(-0.116466,e,[0.58119],"sphere-branch rising cap at neck data")
print("=== (g) flat cap at q1=4 and q1=25 (R1=0):")
inv(0.0,e,[2.0],"flat cap q1=4"); inv(0.0,e,[5.0],"flat cap q1=25")
print("=== (h) (4,0) complex saddle:")
inv(-0.073307+0.126784j,e,[1.185,2.31399+2.82886j],"(4,0) complex")
