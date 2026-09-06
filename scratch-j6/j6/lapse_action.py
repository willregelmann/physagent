# Item 3.1: the J-1 minisuperspace action in the FLT lapse gauge  ds^2 = N_E^2 dt^2/q + q dOmega_3^2,  t in [0,1],  q = a^2 = e^{2 sigma}.
# Conformal time: d eta = N_E dt / q. J-1's Lagrangian is per unit eta: L(sigma, sigma', sigma'') with ' = d/d eta.
# We (i) rewrite I = int_0^1 dt (N_E/q) L, (ii) check that the Euler-Lagrange equation for q at fixed N_E is proportional to the
# trace equation (T) times sqrt(g), (iii) check that dI/dN_E on shell is the Hamiltonian constraint (vanishes on the regular sphere),
# (iv) evaluate I on the round sphere reaching a_1 = sqrt(q_1) with complex N_E = T-dependent, reproducing -a(5+4 eps) for the full sphere
#      and the FLT-type half-sphere-plus-Lorentzian value, and (v) exhibit the Lorentzian continuation N_E = i N (real N).
import sympy as sp, pickle, numpy as np
eta,t=sp.symbols('eta t'); N=sp.symbols('N_E')
aa,epsl=sp.symbols('a_anom epsilon'); G=sp.pi/aa   # H0 = 1 units, G a_anom = pi
q=sp.Function('q')(t)
# J-1 Lagrangian per unit conformal time (per Vol(S^3) = 2 pi^2, with the 8 sigma'^2 -> 8(sigma'^2 - 1) regularization)
X0,X1,X2=sp.symbols('X0 X1 X2')
kap=-aa*(3*epsl+1)/(288*sp.pi**2)
L_eta=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)+(aa/(16*sp.pi**2))*(2*X2**2+8*(X1**2-1))+36*kap*(1-X2-X1**2)**2
# sigma = (1/2) ln q ; sigma' = d sigma/d eta = (q/N) d sigma/dt ; sigma'' = (q/N) d/dt[(q/N) d sigma/dt]
sig=sp.log(q)/2
s1=(q/N)*sp.diff(sig,t); s2=(q/N)*sp.diff(s1,t)
Lt=sp.simplify((N/q)*L_eta.subs({X0:sig,X1:s1,X2:s2}))      # Lagrangian per unit t
Lt=sp.expand(Lt)
# (ii) Euler-Lagrange for q at fixed N (4th order)
qd=[q]+[sp.diff(q,t,k) for k in range(1,5)]
Q=sp.symbols('Q0:5')
Lq=Lt.subs({qd[k]:Q[k] for k in range(4,-1,-1)})
EL=sp.diff(Lq,Q[0])-sp.diff(sp.diff(Lq,Q[1]).subs({Q[k]:qd[k] for k in range(5)}),t)+sp.diff(sp.diff(Lq,Q[2]).subs({Q[k]:qd[k] for k in range(5)}),t,2)
EL=sp.expand(sp.simplify(EL))
# trace equation in tau-frame invariants, converted: a = sqrt(q), d/dtau = (sqrt(q)/N) d/dt  (since d tau = N dt / sqrt(q))
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
A=[sp.sqrt(q)]
for k in range(4): A.append((sp.sqrt(q)/N)*sp.diff(A[-1],t))
rep={sp.Derivative(a,(tau,4)):A[4],sp.Derivative(a,(tau,3)):A[3],sp.Derivative(a,(tau,2)):A[2],sp.Derivative(a,tau):A[1]}
TR=sp.simplify((d['R']-sp.Rational(1,2)*d['E4']-epsl*d['boxR']).subs(rep).subs(a,A[0]))
ratio=sp.simplify(EL/TR)
print("EL(q; fixed N_E) / trace-equation =",ratio)
# (iii) dI/dN on shell: the constraint. Evaluate d L_t / d N on the round sphere: q = sin^2(tau), tau = ... with constant N_E: d tau = N dt/ a -> for the sphere a = sin(tau): t(tau) = (1/N) int_0^tau sin = (1-cos tau)/N ; choose N = N_E so that t(T)=1: N_E = 1 - cos T
T=sp.symbols('T')
Nsph=1-sp.cos(T)
tau_of_t=sp.acos(1-Nsph*t)
qs=sp.sin(tau_of_t)**2
Lt_s=Lt.subs(N,Nsph)
dLdN=sp.diff(Lt,N)
Hval=sp.simplify(dLdN.subs(N,Nsph).subs(q,qs).doit())
print("dL_t/dN_E on the sphere (should vanish identically: regular cap => constraint holds):",sp.simplify(Hval))
# (iv) on-shell action of the sphere truncated at proper length T (complex T allowed): I(T) = int_0^1 L_t dt = int_0^T L_eta dtau/a  ... do it directly in tau
Ltau=sp.simplify(L_eta.subs({X0:sp.log(sp.sin(tau)),X1:sp.cos(tau),X2:-sp.sin(tau)**2})/sp.sin(tau))  # L_eta d eta = L_eta d tau / a
Ltau=sp.simplify(Ltau.subs(G,sp.pi/aa)/aa)   # per a_anom
IT=sp.simplify(2*sp.pi**2*sp.integrate(Ltau,(tau,0,T)))
print("I(T)/a_anom for the sphere truncated at tau=T:",sp.simplify(IT))
print("full sphere T=pi:",sp.simplify(IT.subs(T,sp.pi)),"   half sphere T=pi/2:",sp.simplify(IT.subs(T,sp.pi/2)))
# FLT-type saddle: T = pi/2 + i arccosh(a1) reaches a(T) = sin T = cosh(arccosh a1) = a1
a1=sp.symbols('a_1',positive=True)
Tpm=[sp.pi/2+sp.I*sp.acosh(a1), sp.pi/2-sp.I*sp.acosh(a1), -sp.pi/2+sp.I*sp.acosh(a1), -sp.pi/2-sp.I*sp.acosh(a1)]
for Tv in Tpm:
    val=sp.simplify(sp.expand_complex(IT.subs(T,Tv).subs(a1,3)).evalf(8))
    print("T =",Tv,"  a(T) =",sp.simplify(sp.sin(Tv)),"  I/a =",val,"  (eps symbolic)")
pickle.dump({'Lt':Lt,'IT':IT},open('lapse.pkl','wb'))
