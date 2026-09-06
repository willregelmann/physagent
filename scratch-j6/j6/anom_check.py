# Unambiguous anomaly action: Gamma[sigma; S^4] with the round unit S^4 as compact reference, g = e^{2 sigma} ghat.
# Compare with J-1's ESU-reduced value (8(sigma'^2-1) subtraction) for the sphere and the double bubble.
import sympy as sp, pickle, numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import brentq
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']; eps=sp.symbols('epsilon')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4')
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
odeE=sp.numer(sp.together(R-sp.Rational(1,2)*E4-eps*boxR)).subs(rep).subs(a,A0)
FE=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeE,A4)[0],'numpy')
c3s=sp.symbols('c3'); c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
# state y=[a,a',a'',a''', theta, I_EH, I_an_J1(sub=1), I_an_J1(sub=0), I_R2, Gamma_S4]
def rhs(t,y,e):
    A,A1_,A2_,A3_,th=y[:5]
    A4_=FE(A,A1_,A2_,A3_,e)
    thp=np.sin(th)/A
    # J-1 pieces per a_anom, per 2pi^2, in tau: L_eta/a
    L_EH=-(6/(16*np.pi**2))*A**2*(1+A1_**2)/A
    L_an1=(1/(16*np.pi**2))*(2*(A*A2_)**2+8*(A1_**2-1))/A
    L_an0=(1/(16*np.pi**2))*(2*(A*A2_)**2+8*(A1_**2))/A
    L_R2=36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2_-A1_**2)**2/A
    # S^4-reference Gamma density in theta: (1/8) sin^3 th [24 s + 2 (box s)^2 + 4 s_th^2] dtheta, dtheta = thp dtau
    s=np.log(A/np.sin(th)) if th>1e-12 else 0.0
    sth=(A1_-np.cos(th))/np.sin(th)
    sthth=A*A2_/np.sin(th)**2+1-(A1_-np.cos(th))*np.cos(th)/np.sin(th)**2
    box=sthth+3*np.cos(th)/np.sin(th)*sth
    G=(1/8)*np.sin(th)**3*(24*s+2*box**2+4*sth**2)*thp
    return [A1_,A2_,A3_,A4_,thp,2*np.pi**2*L_EH,2*np.pi**2*L_an1,2*np.pi**2*L_an0,2*np.pi**2*L_R2,G]
def run(c3,e,t0=1e-3,tmax=25.0):
    C5,C7=c5f(c3,e),c7f(c3,e)
    a0=t0+c3*t0**3+C5*t0**5+C7*t0**7
    y0=[a0,1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6,6*c3*t0+20*C5*t0**3+42*C7*t0**5,6*c3+60*C5*t0**2+210*C7*t0**4,0,0,0,0,0,0]
    # theta near pole: theta ~ tau (1 + O(tau^2)); set theta0 = t0 (error O(t0^3))
    y0[4]=t0
    ext=lambda t,y,e: y[1]; ext.direction=0
    close=lambda t,y,e: y[0]-1e-3; close.terminal=True; close.direction=-1
    blow=lambda t,y,e: y[0]-40.0; blow.terminal=True
    s=solve_ivp(rhs,(t0,tmax),y0,args=(e,),method='DOP853',rtol=1e-11,atol=1e-14,events=[ext,close,blow],dense_output=True)
    return s
def report(c3,e,label):
    s=run(c3,e); yf=s.y[:,-1]; te=s.t[-1]
    # symmetric tail correction: the last 1e-3 of proper time contributes ~ the first 1e-3 (mirror) -> negligible at 1e-3 level for finite pieces; log-divergent pieces (an0) excluded.
    print(f"{label}: eps={e} c3={c3:+.6f}  tau_end={te:.4f} theta_end={yf[4]:.6f} (pi={np.pi:.6f}) | I_EH={yf[5]:+.5f} I_an(J1,sub=1)={yf[6]:+.5f} I_an(sub=0)={yf[7]:+.5f} I_R2={yf[8]:+.5f} | Gamma_S4={yf[9]:+.5f} | I_J1 total={yf[5]+yf[6]+yf[8]:+.5f} | I_S4ref total={yf[5]+yf[9]+yf[8]:+.5f}")
    return yf
print("Sphere checks (Gamma_S4 should be 0 for unit sphere):")
for e in (0.36,1.0):
    report(-1/6,e,"S4")
# radius-r sphere check of Gamma via a scaled problem is not available in H0=1 units; instead verify Gamma_S4 = 4 ln r analytically below.
# Double bubbles: c3* from J-1
DB={0.36:-0.347204,0.40:-0.350687,0.45:-0.353077,0.5:-0.354147,1.0:-0.349489,2.0:-0.342261,5.0:-0.337009}
def neck_a3(c3,e):
    s=run(c3,e); 
    ev=s.t_events[0]
    if len(ev)<2: return np.nan
    y=s.sol(ev[1]); return y[3]
res={}
for e,c3g in DB.items():
    try:
        c3r=brentq(neck_a3,c3g-0.003,c3g+0.003,args=(e,),xtol=1e-10)
    except Exception as ex:
        print("bracket fail",e,ex); c3r=c3g
    yS=report(-1/6,e,"S4"); yD=report(c3r,e,"DB")
    dJ1=(yD[5]+yD[6]+yD[8])-(yS[5]+yS[6]+yS[8]); dS4=(yD[5]+yD[9]+yD[8])-(yS[5]+yS[9]+yS[8])
    print(f"   ==> eps={e}: Delta I (J-1 scheme) = {dJ1:+.4f}   Delta I (S4-reference anomaly) = {dS4:+.4f}   difference = {dS4-dJ1:+.4f}   [anomaly parts: J1 {yD[6]-yS[6]:+.4f}, S4ref {yD[9]-yS[9]:+.4f}]")
    res[e]=dict(c3=c3r,S4=yS,DB=yD)
pickle.dump(res,open('anom_check.pkl','wb'))
