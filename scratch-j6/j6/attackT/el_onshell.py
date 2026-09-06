# On-shell check: the fixed-N q-equation of the lapse-gauge action vanishes on regular caps (which solve the trace equation and the
# constraint), while off-shell it differs from mu N/2 * (trace equation) by a multiple of the constraint.
import sympy as sp, pickle, numpy as np
from scipy.integrate import solve_ivp
t=sp.symbols('t'); N=sp.symbols('N_E'); aa,epsl=sp.symbols('a_anom epsilon'); G=sp.pi/aa
q=sp.Function('q')(t); X0,X1,X2=sp.symbols('X0 X1 X2')
kap=-aa*(3*epsl+1)/(288*sp.pi**2)
L_eta=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)+(aa/(16*sp.pi**2))*(2*X2**2+8*X1**2+8)+36*kap*(1-X2-X1**2)**2
sig=sp.log(q)/2; s1=(q/N)*sp.diff(sig,t); s2=(q/N)*sp.diff(s1,t)
Lt=sp.expand(sp.simplify((N/q)*L_eta.subs({X0:sig,X1:s1,X2:s2})))
qd=[q]+[sp.diff(q,t,k) for k in range(1,5)]; Q=sp.symbols('Q0:5')
fwd={qd[k]:Q[k] for k in range(4,-1,-1)}; back={Q[k]:qd[k] for k in range(5)}
Lq=Lt.subs(fwd)
EL=(sp.diff(Lq,Q[0]).subs(back)-sp.diff(sp.diff(Lq,Q[1]).subs(back),t)+sp.diff(sp.diff(Lq,Q[2]).subs(back),t,2)).doit()
ELn=sp.lambdify((Q[0],Q[1],Q[2],Q[3],Q[4],N,aa,epsl),EL.subs(fwd))
# chain rule: q = a^2, d/dt = (a/N) d/dtau
tau=sp.symbols('tau'); a=sp.Function('a')(tau)
qq=[a**2]
for k in range(4): qq.append(sp.expand((N/a)*sp.diff(qq[-1],tau)))
B=sp.symbols('B0:5')
repB={sp.Derivative(a,(tau,4)):B[4],sp.Derivative(a,(tau,3)):B[3],sp.Derivative(a,(tau,2)):B[2],sp.Derivative(a,tau):B[1]}
qf=[sp.lambdify((B[0],B[1],B[2],B[3],B[4],N),ex.subs(repB).subs(a,B[0])) for ex in qq]
# symbolic sphere check: q = sin^2(tau(t)), tau = acos(1-N t)
qs=sp.sin(sp.acos(1-N*t))**2
val=sp.simplify(EL.subs(q,qs).doit().subs({epsl:sp.Rational(3,2),aa:1,N:sp.Rational(1,2)}))
print("EL_t on the round sphere (symbolic, eps=3/2, N=1/2):",val)
# numeric: regular cap c3=-0.3, eps=1
d=pickle.load(open('curv.pkl','rb')); R,E4,boxR=d['R'],d['E4'],d['boxR']; eps=sp.symbols('epsilon')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4')
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
odeE=sp.numer(sp.together(R-sp.Rational(1,2)*E4-eps*boxR)).subs(rep).subs(a,A0)
FE=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeE,A4)[0],'numpy')
c3s=sp.symbols('c3'); c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
e=1.0; c3=-0.3; t0=2e-3; C5,C7=c5f(c3,e),c7f(c3,e)
y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4]
sol=solve_ivp(lambda s,y:[y[1],y[2],y[3],FE(*y,e)],(t0,1.5),y0,method='DOP853',rtol=1e-11,atol=1e-14,dense_output=True)
Nv=0.7
for tv in (0.3,0.6,0.9,1.2):
    y=sol.sol(tv); y4=FE(*y,e)
    qv=[f(y[0],y[1],y[2],y[3],y4,Nv) for f in qf]
    print(f"tau={tv}: regular cap c3=-0.3: EL_t = {ELn(*qv,Nv,1.0,e):+.3e}  (scale of individual terms ~ {abs(qv[0]*Nv):.2f})")
# off-shell: perturb q'''' only (breaks the trace equation) and also q'' (breaks constraint): EL_t vs mu N/2 * TR
TRn=sp.lambdify((A0,A1,A2,A3,A4,eps),(R-sp.Rational(1,2)*E4-eps*boxR).subs(rep).subs(a,A0))
y=sol.sol(0.6); y4=FE(*y,e)
for dq in (0.0,0.5):
    yy=[y[0],y[1],y[2]+dq,y[3]]; yy4=FE(*yy,e)+0.0   # keep trace eq satisfied? no: recompute TR honestly
    qv=[f(yy[0],yy[1],yy[2],yy[3],yy4,Nv) for f in qf]
    print(f"perturb a''+={dq}: EL_t = {ELn(*qv,Nv,1.0,e):+.4e}   (-N/16pi^2)*TR = {(-Nv/(16*np.pi**2))*TRn(yy[0],yy[1],yy[2],yy[3],yy4,e):+.4e}")
