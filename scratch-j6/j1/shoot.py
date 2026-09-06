import sympy as sp, pickle, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']
eps=sp.symbols('epsilon')
ode=sp.together(R-sp.Rational(1,2)*E4-eps*boxR)
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4')
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
num=sp.numer(ode).subs(rep).subs(a,A0)
sol4=sp.solve(num,A4)[0]
F=sp.lambdify((A0,A1,A2,A3,eps),sol4,'numpy')
# pole series coefficients
c3s=sp.symbols('c3')
c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
def rhs(t,y,e): return [y[1],y[2],y[3],F(y[0],y[1],y[2],y[3],e)]
def run(c3,e,t0=2e-3,tmax=25.0):
    C5,C7=c5f(c3,e),c7f(c3,e)
    y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4]
    ext=lambda t,y,e: y[1]; ext.direction=0
    close=lambda t,y,e: y[0]-1e-4; close.terminal=True; close.direction=-1
    blow=lambda t,y,e: y[0]-40.0; blow.terminal=True
    s=solve_ivp(rhs,(t0,tmax),y0,args=(e,),method='Radau',rtol=1e-10,atol=1e-12,events=[ext,close,blow],dense_output=True,max_step=0.05)
    extrema=[(t,*y) for t,y in zip(s.t_events[0],s.y_events[0])]   # (tau, a, a', a'', a''')
    closed=len(s.t_events[1])>0; blown=len(s.t_events[2])>0
    return extrema,closed,blown,s
# sanity: S^4 at c3=-1/6 for eps=1
ex,cl,bl,s=run(-1/6,1.0); print("S4 test eps=1: extrema",[(round(t,4),round(y,4),round(y3,6)) for t,y,y1,y2,y3 in ex],"closed",cl,"tau_end",round(s.t[-1],4))
for e in (0.5,1.0,2.0,5.0):
    print(f"\n=== eps={e} : c3 scan; per extremum (tau, a, a''') ; closed?")
    for c3 in np.linspace(-1.0,0.2,25):
        ex,cl,bl,s=run(c3,e)
        desc=" | ".join(f"{t:.2f},{y:.3f},{y3:+.3f}" for t,y,y1,y2,y3 in ex[:3])
        print(f"c3={c3:+.3f}  n_ext={len(ex)}  closed={int(cl)} blow={int(bl)}  {desc}")
