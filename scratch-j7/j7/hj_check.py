import sympy as sp
tau,T=sp.symbols('tau T'); a=sp.Function('a')(tau); eps=sp.symbols('epsilon',positive=True)
A0,A1,A2=sp.symbols('A0 A1 A2',real=True); C=8
kap=-(3*eps+1)/(288*sp.pi**2)
L=2*sp.pi**2*(-(sp.Integer(6)/(16*sp.pi**2))*A0**2*(1+A1**2)+(1/(16*sp.pi**2))*(2*A0**2*A2**2+8*A1**2+C)+36*kap*(1-A0*A2-A1**2)**2)/A0
pv=sp.diff(L,A2); pa_partial=sp.diff(L,A1)
sub={A0:a,A1:sp.diff(a,tau),A2:sp.diff(a,tau,2)}
pv_t=pv.subs(sub); pa_t=pa_partial.subs(sub)-sp.diff(pv_t,tau)
sph={a:sp.sin(tau)}
pv_s=sp.simplify(pv_t.subs(sph).doit()); pa_s=sp.simplify(pa_t.subs(sph).doit())
print("bulk p_v on sphere:",sp.factor(pv_s)); print("bulk p_a on sphere:",sp.factor(pa_s))
# candidate HJ functions for the sphere cut at proper length T (a=sin T, v=cos T):
I_T=-(sp.Rational(5,3)+2*eps)+(sp.Rational(7,4)+3*eps)*sp.cos(T)-(eps+sp.Rational(1,12))*sp.cos(T)**3   # position T's corrected-scheme (pole-frame Riegert, Gamma=0) 
# HJ: dI/dT = p_a * da/dT + p_v * dv/dT = p_a cos T - p_v sin T  (bulk momenta at tau=T, plus pole terms which vanish for a regular pole with delta a=0)
lhs=sp.diff(I_T,T); rhs=(pa_s*sp.cos(tau)-pv_s*sp.sin(tau)).subs(tau,T)
print("HJ residual dI_T/dT - (p_a cos T - p_v sin T) for position T's I(T):",sp.simplify(lhs-rhs))
# Ostrogradsky energy on the sphere with these momenta (should vanish identically):
H=sp.simplify((pa_t*sp.diff(a,tau)+pv_t*sp.diff(a,tau,2)-L.subs(sub)).subs(sph).doit()); print("Ostrogradsky energy on sphere:",H)
# (a,R)-representation: generating function F(v,R;a) with p_v = dF/dv: F = eps a^2 R v/4 - v^3/6 + v/2 ; I_(a,R) = I_(a,v) - F
v,R,aa=sp.symbols('v R a',real=True); F=eps*aa**2*R*v/4-v**3/6+v/2
print("dF/dv =",sp.expand(sp.diff(F,v)),"  vs bulk p_v(a,v,R) =",sp.expand((eps*aa**2*R-2*v**2+2)/4))
# variational check on the general Lagrangian: with B = -v p_v - v^3/3, is delta(I+B)=0 for delta a = delta R = 0 at the cut?
Bv=-A1*pv-A1**3/3
cond=sp.simplify(pv+sp.diff(Bv,A1)-(2*A1/A0)*sp.diff(Bv,A2))
print("fixed-(a,R) boundary condition residual p_v + B_v - (2v/a) B_{a''} =",cond)
# sphere at (q,R)=(4,12): a=2, v=-i sqrt3 -> B is imaginary; recontracting cap: v real -> B real. Evaluate B symbolically:
Bsym=sp.simplify(Bv.subs({A2:sp.solve(sp.Eq(-6*(A0*A2+A1**2-1)/A0**2,R),A2)[0]}))
print("B(a,v,R) =",sp.factor(Bsym))
print("B on sphere at (4,12) (a=2,v=-i sqrt3):",sp.simplify(Bsym.subs({A0:2,A1:-sp.I*sp.sqrt(3),R:12})))
