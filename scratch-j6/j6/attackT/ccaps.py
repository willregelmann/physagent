# Complex regular caps of the anomaly+R^2 minisuperspace (H0=1, per a_anom), with the corrected (S^4-reference) anomaly action.
# State y = [a, a', a'', a''', theta, I_loc (2pi^2 * (EH+R2) density), Gamma (S^4-ref anomaly density), Nacc (= int a dtau)] all complex.
import sympy as sp, pickle, numpy as np
from scipy.integrate import solve_ivp
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']; eps=sp.symbols('epsilon')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4')
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
odeE=sp.numer(sp.together(R-sp.Rational(1,2)*E4-eps*boxR)).subs(rep).subs(a,A0)
FE=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeE,A4)[0],'numpy')
Rf=sp.lambdify((A0,A1,A2),R.subs(rep).subs(a,A0),'numpy')   # scalar curvature
c3s=sp.symbols('c3'); c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
def dens(y,e):
    A,A1_,A2_,A3_,th=y[:5]
    A4_=FE(A,A1_,A2_,A3_,e)
    thp=np.sin(th)/A
    L_EH=-(6/(16*np.pi**2))*A*(1+A1_**2)
    L_R2=36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2_-A1_**2)**2/A
    s=np.log(A/np.sin(th))
    sth=(A1_-np.cos(th))/np.sin(th)
    sthth=A*A2_/np.sin(th)**2+1-(A1_-np.cos(th))*np.cos(th)/np.sin(th)**2
    box=sthth+3*np.cos(th)/np.sin(th)*sth
    G=(1/8)*np.sin(th)**3*(24*s+2*box**2+4*sth**2)*thp
    return np.array([A1_,A2_,A3_,A4_,thp,2*np.pi**2*(L_EH+L_R2),G,A],dtype=complex)
def y0_of(c3,e,t0):
    C5,C7=c5f(c3,e),c7f(c3,e)
    # theta series near pole: theta = tau + th3 tau^3, from dtheta/dtau = sin(theta)/a: th3 = (1 - 6 c3)/... derive: theta=tau+k tau^3: theta' = 1+3k tau^2 ; sin(theta)/a = (tau + k tau^3 - tau^3/6)/(tau + c3 tau^3) = 1 + (k - 1/6 - c3) tau^2 -> 3k = k - 1/6 - c3 -> k = -(1/6 + c3)/2
    k=-(1/6+c3)/2
    return np.array([t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4, t0+k*t0**3, 0,0,0],dtype=complex)
def integrate_path(c3,e,path,t0=2e-3,rtol=1e-10,atol=1e-13,events=None,dense=False):
    """path: list of complex tau waypoints starting after tau0=t0 (real). Integrates y along straight segments. Returns final y and per-segment solutions."""
    y=y0_of(c3,e,t0); pts=[t0+0j]+[complex(p) for p in path]; sols=[]
    for i in range(len(pts)-1):
        z0,z1=pts[i],pts[i+1]; dz=z1-z0
        f=lambda s,Y: dz*dens(Y,e)
        ev=[]
        if events:
            for g in events:
                h=lambda s,Y,g=g: g(z0+s*dz,Y)
                h.terminal=getattr(g,'terminal',False); h.direction=getattr(g,'direction',0); ev.append(h)
        sol=solve_ivp(f,(0,1),y,method='DOP853',rtol=rtol,atol=atol,events=ev or None,dense_output=dense)
        sols.append((z0,dz,sol)); y=sol.y[:,-1]
        if sol.status==1: break
    return y,sols
def action(y): return y[5]+y[6]      # I/a_anom for the cap up to the endpoint (no boundary term)
if __name__=="__main__":
    # sanity: sphere half cap to tau=pi/2, then Lorentzian continuation to a=2 (T=arccosh 2)
    e=1.0
    y,_=integrate_path(-1/6,e,[np.pi/2]); print("sphere half: a=",y[0]," I=",action(y)," (expect -(10/3+4eps)/2 =",-(10/3+4*e)/2,") N=",y[7])
    T=np.arccosh(2.0); y,_=integrate_path(-1/6,e,[np.pi/2,np.pi/2+1j*T]); print("sphere -> a=2:",y[0]," I=",action(y)," N=",y[7]," expect N=1+i sqrt3=",1+1j*np.sqrt(3))
