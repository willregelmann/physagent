import sympy as sp, pickle, numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import brentq
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']; eps=sp.symbols('epsilon')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4',real=True)
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
odeE=sp.numer(sp.together(R-sp.Rational(1,2)*E4-eps*boxR)).subs(rep).subs(a,A0)
FE=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeE,A4)[0],'numpy')
# Lorentzian continuation: a' -> -i adot, a''-> -addot, a'''-> i adddot, a''''-> addddot
I=sp.I
odeL=sp.expand(odeE.subs({A1:-I*A1,A2:-A2,A3:I*A3}))
assert not odeL.has(I), 'Lorentzian continuation not real'
FL=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeL,A4)[0],'numpy')
c3s=sp.symbols('c3'); c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
def rhsE(t,y,e): return [y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e)]
def rhsL(t,y,e): return [y[1],y[2],y[3],FL(y[0],y[1],y[2],y[3],e)]
def run(c3,e,t0=2e-3,tmax=25.0,dense=False):
    C5,C7=c5f(c3,e),c7f(c3,e)
    y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4]
    ext=lambda t,y,e: y[1]; ext.direction=0
    close=lambda t,y,e: y[0]-1e-4; close.terminal=True; close.direction=-1
    blow=lambda t,y,e: y[0]-40.0; blow.terminal=True
    s=solve_ivp(rhsE,(t0,tmax),y0,args=(e,),method='DOP853',rtol=1e-10,atol=1e-13,events=[ext,close,blow],dense_output=dense)
    return [(t,*y) for t,y in zip(s.t_events[0],s.y_events[0])],len(s.t_events[1])>0,s
def neck_a3(c3,e):
    ex,cl,s=run(c3,e); return ex[1][4] if len(ex)>=3 else np.nan
# action density per 2 pi^2, in units H0=1 with G a_anom = pi; report I/a_anom (multiply by a2/180 for the physical action)
def Ifull(sol,e,tmax):
    # L = -(6/(16 pi G)) e^{2s}(1+s'^2) + (a/16pi^2)(2 s''^2 + 8(s'^2-1)) + 36 kappa (1-s''-s'^2)^2 ; d eta = d tau / a
    # divide by a_anom: 1/G = a_anom/pi -> -(6/(16 pi^2)) ; (1/(16 pi^2)) ; kappa/a = -(3e+1)/(288 pi^2)
    ts=np.linspace(sol.t[0],tmax,20001); Y=sol.sol(ts); A,A1,A2=Y[0],Y[1],Y[2]
    sp1=A1; sp2=A*A2
    L=(-(6/(16*np.pi**2))*A**2*(1+sp1**2) + (1/(16*np.pi**2))*(2*sp2**2+8*(sp1**2-1)) + 36*(-(3*e+1)/(288*np.pi**2))*(1-sp2-sp1**2)**2)/A
    return 2*np.pi**2*trapezoid(L,ts)
def IS4(e): return -(5+4*e)   # analytic, per a_anom, full sphere
res={}
for e in (0.25,0.5,1.0,2.0,5.0,10.0):
    # S4 numeric check
    ex,cl,s=run(-1/6,e,dense=True); IS4num=Ifull(s,e,s.t_events[1][0])
    # bracket the neck-symmetric root
    grid=np.linspace(-0.50,-0.28,12); vals=[neck_a3(c,e) for c in grid]; br=None
    for i in range(len(grid)-1):
        if np.isfinite(vals[i]) and np.isfinite(vals[i+1]) and vals[i]*vals[i+1]<0: br=(grid[i],grid[i+1]); break
    if br is None:
        print(f"eps={e}: no root; vals",[round(v,2) if np.isfinite(v) else None for v in vals]); continue
    c3r=brentq(neck_a3,br[0],br[1],args=(e,),xtol=1e-9)
    ex,cl,s=run(c3r,e,dense=True); (t1,a1,_,a1dd,_),(t2,a2,_,a2dd,a2ddd)=ex[0],ex[1]
    tclose=s.t_events[1][0]; IDB=Ifull(s,e,tclose)
    # Lorentzian continuation from the neck: adot=0, addot=-a''_E, adddot=0
    yL=[a2,0.0,-a2dd,0.0]
    stopL=lambda t,y,e: y[0]-1e-3; stopL.terminal=True; stopL.direction=-1
    growL=lambda t,y,e: y[0]-50.0; growL.terminal=True
    sL=solve_ivp(rhsL,(0,60),yL,args=(e,),method='DOP853',rtol=1e-9,atol=1e-12,events=[stopL,growL])
    fate="recollapse" if len(sL.t_events[0]) else ("grows to 50" if len(sL.t_events[1]) else "neither by t=60")
    amax=sL.y[0].max()
    res[e]=dict(c3=c3r,a_peak=a1,tau_neck=t2,a_neck=a2,IS4=IS4(e),IS4num=IS4num,IDB=IDB,fate=fate,amax=amax,tL=sL.t[-1])
    print(f"eps={e:5.2f} c3*={c3r:+.6f} peak a={a1:.4f} neck a={a2:.4f} (tau={t2:.4f}, a'''={a2ddd:+.1e}) | I_S4/a: analytic {IS4(e):+.4f} numeric {IS4num:+.4f} | I_DB/a = {IDB:+.4f} | dI=(I_DB-I_S4)/a = {IDB-IS4(e):+.4f} -> {'S4 dominates' if IDB>IS4(e) else 'DOUBLE BUBBLE dominates'} | neck continuation: {fate}, a_max={amax:.3f} at t<={sL.t[-1]:.2f}",flush=True)
pickle.dump(res,open('caps.pkl','wb'))
