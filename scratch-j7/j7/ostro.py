import sympy as sp
tau=sp.symbols('tau'); a=sp.Function('a')(tau); eps=sp.symbols('epsilon',positive=True); C=sp.symbols('C')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4',real=True)
# proper-time Lagrangian per a_anom, times 2pi^2 included; G a = pi; ESU-frame local anomaly term with constant C (C=+8 per the J-6 attacks)
kap_over_a=-(3*eps+1)/(288*sp.pi**2)
def Ltau(A0,A1,A2):
    Leta=-(sp.Integer(6)/(16*sp.pi**2))*A0**2*(1+A1**2)+(1/(16*sp.pi**2))*(2*A0**2*A2**2+8*A1**2+C)+36*kap_over_a*(1-A0*A2-A1**2)**2
    return 2*sp.pi**2*Leta/A0            # d eta = d tau / a
L=Ltau(A0,A1,A2)
# Ostrogradsky momenta: p_v = dL/da'' ; p_a = dL/da' - d/dtau p_v ; EL = dL/da - d/dtau(dL/da') + d^2/dtau^2 (dL/da'')
pv=sp.diff(L,A2); pa_partial=sp.diff(L,A1); La=sp.diff(L,A0)
sub={A0:a,A1:sp.diff(a,tau),A2:sp.diff(a,tau,2)}
pv_t=pv.subs(sub); pa_t=(pa_partial.subs(sub)-sp.diff(pv_t,tau))
EL=sp.simplify(La.subs(sub)-sp.diff(pa_partial.subs(sub),tau)+sp.diff(pv_t,tau,2))
# check: EL on the round sphere and on the trace equation
sphere={a:sp.sin(tau)}
print("EL on sphere (should be 0 for the right C):",sp.simplify(EL.subs(sphere).doit()))
# energy (Hamiltonian constraint, Ostrogradsky): H = p_a a' + p_v a'' - L
H=sp.simplify((pa_t*sp.diff(a,tau)+pv_t*sp.diff(a,tau,2)-L.subs(sub)).subs(sphere).doit())
print("Ostrogradsky energy on sphere (should be 0 for the right C):",sp.simplify(H))
print("-> solve C from H=0:",sp.solve(sp.simplify(H),C))
# boundary term structure: delta I = int EL delta a + [p_a delta a + p_v delta v]; fixed (a,v): no extra term.
# fixed (a,R): R = -6(a a'' + a'^2 - 1)/a^2 ; Legendre in (v,p_v): I_(a,R) = I_(a,v) - (p_v v)|cut  [derived below via dI on-shell]
R=-6*(A0*A2+A1**2-1)/A0**2
pv_of_R=sp.simplify(pv.subs(A2,sp.solve(sp.Eq(R,sp.Symbol('Rc')),A2)[0]))
print("p_v as function of (a, v, R):",sp.factor(pv_of_R))
# on the sphere's equator (a=1,v=0,R=12): p_v
print("p_v at equator:",sp.simplify(pv_of_R.subs({A0:1,A1:0,sp.Symbol('Rc'):12,C:8})))
# cone coefficient: a = v tau near the pole, log-divergent coefficient of int L dtau ~ coeff * ln(1/delta)
v=sp.symbols('v',positive=True)
Lcone=sp.simplify(Ltau(v*tau,v,0)*tau)   # tau * L -> coefficient of 1/tau term times tau = the log coefficient
coef=sp.simplify(sp.limit(Lcone,tau,0))
print("log coefficient on a cone a=v*tau (per a, C symbolic):",sp.factor(coef))
print("  at C=8, minus the regular value (v=1):",sp.factor(sp.simplify((coef-coef.subs(v,1)).subs(C,8))))
print("  series in (v-1):",sp.series(sp.simplify((coef-coef.subs(v,1)).subs(C,8)),v,1,3))
