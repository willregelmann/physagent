import sympy as sp, pickle, numpy as np
d=pickle.load(open('lapse.pkl','rb')); t=sp.symbols('t'); q=sp.Function('q')(t); N,eps=sp.symbols('N epsilon')
Q0,Q1,Q2,Q3,Q4=sp.symbols('Q0 Q1 Q2 Q3 Q4')
rep={sp.Derivative(q,(t,4)):Q4,sp.Derivative(q,(t,3)):Q3,sp.Derivative(q,(t,2)):Q2,sp.Derivative(q,t):Q1}
EL=d['EL'].subs(rep).subs(q,Q0); TR=d['TR'].subs(rep).subs(q,Q0)
fEL=sp.lambdify((Q0,Q1,Q2,Q3,Q4,N,eps),EL); fTR=sp.lambdify((Q0,Q1,Q2,Q3,Q4,N,eps),TR)
rng=np.random.default_rng(1)
print("EL/TR at fixed (q,N,eps), random derivatives -> should be constant if EL = f(q,N) * TR:")
for trial in range(2):
    q0,NN,ee=0.7,1.3,0.8
    vals=[fEL(q0,*rng.normal(size=4),NN,ee)/fTR(q0,*rng.normal(size=4),NN,ee) for _ in range(4)]
    print(vals)
# guess f = -N q /(8 pi^2)?  (mu sqrt g: mu=-1/(8pi^2) per a_anom; sqrt g d^4x -> N/sqrt(q) * q^{3/2} = N q per 2pi^2)
print("compare with -N*q/(8*pi^2) =",-1.3*0.7/(8*np.pi**2))
# Constraint on the sphere:
H=d['H']; qs=2*N*t-N**2*t**2
print("dL/dN on sphere:",sp.simplify(H.subs({Q0:qs,Q1:sp.diff(qs,t),Q2:sp.diff(qs,t,2)})))
# --- pole series in t: q = 2N t + 6 c3 N^2 t^2 + d3 t^3 + d4 t^4 ..., check against trace eq
c3,d3,d4,d5=sp.symbols('c3 d3 d4 d5')
qser=2*N*t+6*c3*N**2*t**2+d3*t**3+d4*t**4+d5*t**5
TRs=sp.numer(sp.together(TR.subs({Q0:qser,Q1:sp.diff(qser,t),Q2:sp.diff(qser,t,2),Q3:sp.diff(qser,t,3),Q4:sp.diff(qser,t,4)})))
TRs=sp.expand(TRs)
coeffs=[sp.factor(TRs.coeff(t,k)) for k in range(0,4)]
for k,c in enumerate(coeffs): print("order t^%d:"%k,c)
sol3=sp.solve(coeffs[0],d3) if coeffs[0]!=0 else None
print("d3 from lowest order:",sol3)
# compare with tau-series: a = tau + c3 tau^3 + c5 tau^5, c5 = c3(6 c3 eps + 6 c3 + 1)/(20 eps); q=a^2, tau^2 from int a dtau = N t
tau=sp.symbols('tau'); c5=c3*(6*c3*eps+6*c3+1)/(20*eps)
aser=tau+c3*tau**3+c5*tau**5
F=sp.integrate(aser,(tau,0,tau))   # = N t
# invert: tau^2 = u; F = u/2 + c3 u^2/4 + c5 u^3/6 = N t -> u = 2Nt + u2 t^2 + u3 t^3
u2,u3=sp.symbols('u2 u3'); u=2*N*t+u2*t**2+u3*t**3
eqF=sp.expand((u/2+c3*u**2/4+c5*u**3/6-N*t))
s=sp.solve([eqF.coeff(t,2),eqF.coeff(t,3)],[u2,u3]); u=u.subs(s)
qtau=sp.expand((u+2*c3*u**2+(c3**2+2*c5)*u**3))
print("q(t) from tau-series:",[sp.factor(qtau.coeff(t,k)) for k in range(1,4)])
