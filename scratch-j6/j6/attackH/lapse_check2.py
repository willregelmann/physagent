# Fix of the EL check in lapse_action.py: substitute the placeholder symbols back before differentiating in t.
import sympy as sp, pickle, numpy as np
from scipy.integrate import quad
t=sp.symbols('t'); N=sp.symbols('N_E'); aa,epsl=sp.symbols('a_anom epsilon'); G=sp.pi/aa
q=sp.Function('q')(t)
X0,X1,X2=sp.symbols('X0 X1 X2')
kap=-aa*(3*epsl+1)/(288*sp.pi**2)
L_eta=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)+(aa/(16*sp.pi**2))*(2*X2**2+8*(X1**2-1))+36*kap*(1-X2-X1**2)**2
sig=sp.log(q)/2; s1=(q/N)*sp.diff(sig,t); s2=(q/N)*sp.diff(s1,t)
Lt=sp.expand(sp.simplify((N/q)*L_eta.subs({X0:sig,X1:s1,X2:s2})))
qd=[q]+[sp.diff(q,t,k) for k in range(1,5)]; Q=sp.symbols('Q0:5')
fwd={qd[k]:Q[k] for k in range(4,-1,-1)}; back={Q[k]:qd[k] for k in range(5)}
Lq=Lt.subs(fwd)
EL=sp.diff(Lq,Q[0]).subs(back)-sp.diff(sp.diff(Lq,Q[1]).subs(back),t)+sp.diff(sp.diff(Lq,Q[2]).subs(back),t,2)
EL=sp.simplify(EL.doit())
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
A=[sp.sqrt(q)]
for k in range(4): A.append((sp.sqrt(q)/N)*sp.diff(A[-1],t))
rep={sp.Derivative(a,(tau,4)):A[4],sp.Derivative(a,(tau,3)):A[3],sp.Derivative(a,(tau,2)):A[2],sp.Derivative(a,tau):A[1]}
TR=sp.simplify((d['R']-sp.Rational(1,2)*d['E4']-epsl*d['boxR']).subs(rep).subs(a,A[0]))
ratio=sp.simplify(EL/TR)
print("EL(q; fixed N_E) / (trace equation) =",ratio)
# expected: mu * sqrt(g) * (dt-measure): sqrt(g) d^4x = (N/sqrt q) q^{3/2} dt = N q dt  -> ratio should be mu*N*q with mu = -a/(8 pi^2) per unit Vol(S^3)... check:
print("ratio / (N_E q) =",sp.simplify(ratio/(N*q)))
# numerical constraint check: int_0^1 dL_t/dN_E dt on the round sphere, N_E = 1 - cos T, q = sin^2(acos(1-N t))
dLdN=sp.diff(Lt,N)
for Tv in (0.7,1.2,sp.pi/2):
    Nv=1-sp.cos(Tv); qs=sp.sin(sp.acos(1-Nv*t))**2
    f=sp.lambdify(t,sp.simplify(dLdN.subs({epsl:1,aa:1}).subs(N,Nv).subs(q,qs).doit()),'numpy')
    val,err=quad(f,1e-6,1-1e-6,limit=200)
    print(f"T={float(Tv):.4f}: int_0^1 dL_t/dN_E dt = {val:+.3e} (quad err {err:.1e})  [should vanish: H=0 on the regular sphere]")
# and for comparison the same integral when the cap is truncated at a NON-regular start (conical): skip.
