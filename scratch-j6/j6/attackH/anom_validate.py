import numpy as np, pickle
from scipy.integrate import quad, solve_ivp, trapezoid
from scipy.interpolate import CubicSpline
# Gamma[sigma]/a = (1/8) int_0^pi sin^3 th [24 s + 2 (box s)^2 + 4 s_th^2] dth ,  box s = s_thth + 3 cot th s_th
def Gamma_of_sigma(s,sth,sthth):
    f=lambda th: (1/8)*np.sin(th)**3*(24*s(th)+2*(sthth(th)+3*np.cos(th)/np.sin(th)*sth(th))**2+4*sth(th)**2)
    return quad(f,1e-9,np.pi-1e-9,limit=400)[0]
# (1) Mobius boost: e^{sigma} = 1/(cosh b + sinh b cos th) is a conformal isometry of the unit S^4 -> Gamma must vanish.
for b in (0.3,1.0,2.0):
    s=lambda th: -np.log(np.cosh(b)+np.sinh(b)*np.cos(th))
    sth=lambda th: np.sinh(b)*np.sin(th)/(np.cosh(b)+np.sinh(b)*np.cos(th))
    sthth=lambda th: (np.sinh(b)*np.cos(th)*(np.cosh(b)+np.sinh(b)*np.cos(th))+np.sinh(b)**2*np.sin(th)**2)/(np.cosh(b)+np.sinh(b)*np.cos(th))**2
    print(f"Mobius boost b={b}: Gamma = {Gamma_of_sigma(s,sth,sthth):+.3e}   (expect 0)")
    # wrong-sign Paneitz for contrast:
    f=lambda th: (1/8)*np.sin(th)**3*(24*s(th)+2*(sthth(th)+3*np.cos(th)/np.sin(th)*sth(th))**2-4*sth(th)**2)
    print(f"      with the opposite sign of the 2*box term: {quad(f,1e-9,np.pi-1e-9,limit=400)[0]:+.3e}   (should NOT vanish)")
# (2) radius-r sphere: sigma = ln r
for r in (0.5,2.0):
    print(f"radius {r}: Gamma = {Gamma_of_sigma(lambda th: np.log(r),lambda th:0*th,lambda th:0*th):+.6f}, 4 ln r = {4*np.log(r):+.6f}")
# (3) cutoff convergence + finite-difference cross-check on the double bubble, eps=1 and eps=0.36
import sympy as sp
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']; eps=sp.symbols('epsilon')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4')
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
odeE=sp.numer(sp.together(R-sp.Rational(1,2)*E4-eps*boxR)).subs(rep).subs(a,A0)
FE=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeE,A4)[0],'numpy')
c3s=sp.symbols('c3'); c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
def rhs(t,y,e):
    A,A1_,A2_,A3_,th=y; return [A1_,A2_,A3_,FE(A,A1_,A2_,A3_,e),np.sin(th)/A]
res=pickle.load(open('anom_check.pkl','rb'))
for e in (0.36,1.0):
    c3=res[e]['c3']
    for t0 in (1e-2,3e-3,1e-3,3e-4):
        C5,C7=c5f(c3,e),c7f(c3,e)
        y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7,1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6,6*c3*t0+20*C5*t0**3+42*C7*t0**5,6*c3+60*C5*t0**2+210*C7*t0**4,t0*(1+0)]
        close=lambda t,y,e: y[0]-t0; close.terminal=True; close.direction=-1
        s=solve_ivp(rhs,(t0,25),y0,args=(e,),method='DOP853',rtol=1e-11,atol=1e-14,events=[close],dense_output=True)
        ts=np.linspace(t0,s.t[-1],40001); Y=s.sol(ts); A,A1_,A2_,th=Y[0],Y[1],Y[2],Y[4]
        sig=np.log(A/np.sin(th)); sth=(A1_-np.cos(th))/np.sin(th); sthth=A*A2_/np.sin(th)**2+1-(A1_-np.cos(th))*np.cos(th)/np.sin(th)**2
        box=sthth+3*np.cos(th)/np.sin(th)*sth
        G_an=trapezoid((1/8)*np.sin(th)**3*(24*sig+2*box**2+4*sth**2)*np.sin(th)/A,ts)
        # finite-difference cross-check: spline sigma(theta), differentiate numerically
        cs=CubicSpline(th,sig); thg=np.linspace(th[0],th[-1],40001)
        s0=cs(thg); s1=cs(thg,1); s2=cs(thg,2); boxg=s2+3*np.cos(thg)/np.sin(thg)*s1
        G_fd=trapezoid((1/8)*np.sin(thg)**3*(24*s0+2*boxg**2+4*s1**2),thg)
        print(f"eps={e} DB c3={c3:+.6f} cutoff a0={t0:.0e}: theta_end={th[-1]:.6f}  Gamma(analytic derivs)={G_an:+.6f}  Gamma(spline FD)={G_fd:+.6f}")
