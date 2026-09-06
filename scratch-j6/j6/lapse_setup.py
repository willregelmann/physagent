# Lapse-gauge minisuperspace action for the anomaly + R^2 theory, H0=1 units, G a = pi, per Vol(S^3)=2 pi^2, divided by a_anom.
# Metric (Euclidean): ds^2 = N^2 dt^2/q + q dOmega_3^2, i.e. dtau = N dt/sqrt(q), a = sqrt(q).
import sympy as sp, pickle
t=sp.symbols('t'); q=sp.Function('q')(t); N=sp.symbols('N'); eps=sp.symbols('epsilon')
Q0,Q1,Q2,Q3,Q4=sp.symbols('Q0 Q1 Q2 Q3 Q4')
# J-1 Lagrangian in conformal time, per a_anom: L_eta = -(6/16pi^2) e^{2s}(1+s'^2) + (1/16pi^2)(2 s''^2 + 8(s'^2-1)) + 36 (kappa/a)(1-s''-s'^2)^2,  kappa/a = -(3eps+1)/(288 pi^2)
# with s = ln a, s' = a_tau, s'' = a a_tautau, d eta = d tau / a.  So I = int L_eta d eta = int (L_eta / a) d tau = int (L_eta/a)(N/sqrt q) dt.
# a_tau = q_dot/(2N);  a_tautau = (sqrt q / N) d/dt (q_dot/(2N)) = sqrt(q) q_ddot/(2 N^2)   (N constant)
a=sp.sqrt(Q0); at=Q1/(2*N); att=sp.sqrt(Q0)*Q2/(2*N**2)
s1=at; s2=a*att
kap_over_a=-(3*eps+1)/(288*sp.pi**2)
L_eta=-(sp.Integer(6)/(16*sp.pi**2))*a**2*(1+s1**2)+(1/(16*sp.pi**2))*(2*s2**2+8*(s1**2-1))+36*kap_over_a*(1-s2-s1**2)**2
Lt=sp.simplify(L_eta/a*N/sp.sqrt(Q0))    # Lagrangian density in t, per a_anom, per 2pi^2
Lt=sp.expand(Lt)
print("L_t (per a_anom, per 2 pi^2) =",Lt)
# Euler-Lagrange in q at fixed N
back={Q0:q,Q1:sp.diff(q,t),Q2:sp.diff(q,t,2)}
EL=sp.diff(Lt,Q0).subs(back)-sp.diff(sp.diff(Lt,Q1).subs(back),t)+sp.diff(sp.diff(Lt,Q2).subs(back),t,2)
EL=sp.expand(EL.doit())
# trace equation in tau-frame variables, converted to t: a(tau) with d/dtau = (sqrt q/N) d/dt
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); af=sp.Function('a')(tau)
A=[sp.sqrt(q)]
for k in range(4): A.append(sp.sqrt(q)/N*sp.diff(A[-1],t))
rep={sp.Derivative(af,(tau,4)):A[4],sp.Derivative(af,(tau,3)):A[3],sp.Derivative(af,(tau,2)):A[2],sp.Derivative(af,tau):A[1]}
TR=(d['R']-sp.Rational(1,2)*d['E4']-eps*d['boxR']).subs(rep).subs(af,A[0])
TR=sp.simplify(TR)
ratio=sp.simplify(EL/TR)
print("EL/TR =",ratio)   # should be a function of q,N only (the sqrt g * mu factor)
# Constraint: dL/dN at fixed q(t) — should vanish on regular solutions (checked numerically later); print its form
H=sp.expand(sp.diff(Lt,N))
print("dL/dN =",H)
# Ostrogradsky momenta
p_qdot=sp.simplify(sp.diff(Lt,Q2)); print("p_{qdot} = dL/dqddot =",p_qdot)
p_q=sp.simplify(sp.diff(Lt,Q1)-sp.diff(sp.diff(Lt,Q2).subs(back),t).subs({sp.diff(q,t,3):Q3,sp.diff(q,t,2):Q2,sp.diff(q,t):Q1,q:Q0}))
print("p_q =",p_q)
# Sphere check: q = 2Nt - N^2 t^2 (radius 1), N=2 full sphere; N=1 half sphere
for NN,lab in ((2,'full'),(1,'half')):
    qs=2*NN*t-NN**2*t**2
    Ls=Lt.subs({Q0:qs,Q1:sp.diff(qs,t),Q2:sp.diff(qs,t,2),N:NN})
    Is=2*sp.pi**2*sp.integrate(sp.simplify(Ls),(t,0,1))
    print(lab,"sphere action / a_anom =",sp.simplify(Is), "  expected:", -(5+4*eps) if NN==2 else -(5+4*eps)/2)
pickle.dump({'Lt':Lt,'EL':EL,'TR':TR,'ratio':ratio,'H':H,'p_qdot':p_qdot,'p_q':p_q},open('lapse.pkl','wb'))
