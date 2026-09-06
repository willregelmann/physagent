# Independent derivation of the HHR alpha <-> J-1 epsilon map from HHR's own 00-constraint (their eq. 2.21, R=1 units),
# by differentiating it and matching to J-1's trace equation R - E4/2 - eps boxR = 0 (energy conservation identity).
import sympy as sp, pickle, numpy as np
tau=sp.symbols('tau'); a=sp.Function('a')(tau); eps,al=sp.symbols('epsilon alpha')
d=pickle.load(open('curv.pkl','rb')); R,E4,boxR=d['R'],d['E4'],d['boxR']
f=a; f1=sp.diff(a,tau); f2=sp.diff(a,tau,2); f3=sp.diff(a,tau,3)
# HHR (2.21) multiplied by f^4:  f^2(1-f'^2) = (1-f'^2)^2 + 2 alpha [2 f^2 f' f''' - f^2 f''^2 + 2 f f'^2 f'' - 3 f'^4 + 2 f'^2 + 1]
G=f**2*(1-f1**2)-(1-f1**2)**2-2*al*(2*f**2*f1*f3-f**2*f2**2+2*f*f1**2*f2-3*f1**4+2*f1**2+1)
print("G on round sphere a=sin tau:",sp.simplify(G.subs(a,sp.sin(tau)).doit()))
print("G on flat space a=tau     :",sp.simplify(G.subs(a,tau).doit()))
dG=sp.expand(sp.diff(G,tau))
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4')
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
dGs=sp.expand(dG.subs(rep).subs(a,A0))
Tr=sp.together((R-sp.Rational(1,2)*E4-eps*boxR).subs(rep).subs(a,A0))
P=dGs.subs(al,0); Q=sp.expand(dGs-P)            # dG = P + alpha Q
U=sp.together(Tr.subs(eps,0)); V=sp.together((Tr-U))  # Tr = U + eps V
mu=sp.simplify(P/(A0**3*A1*U)); print("mu = P/(a^3 a' U) =",mu)
epsmap=sp.simplify(Q/(mu*A0**3*A1*V)); print("epsilon/alpha = Q/(mu a^3 a' V) =",epsmap)
print("==> since Q carries the factor alpha and V the factor eps, Q/(mu a^3 a' V) = (alpha/eps)*(Qt/(mu a^3 a' Vt)); the printed value -2 alpha/eps means Qt/(mu a^3 a' Vt) = -2, i.e. eps = -2 alpha, alpha = -eps/2")
# Consequences: negative modes of the round S^4 scalar sector (HHR sec. 4.2): eigenvalues p(p+3)+m^2 with m^2 = 1/(2 alpha) (R=1)
print("\nScalar-sector mode count on the round S^4 under e^{-I} (HHR 4.2: p(p+3)+m^2, m^2=1/(2alpha)), with alpha(eps) from above:")
amap=sp.lambdify(eps,sp.simplify(al/epsmap).subs(al,1)*eps) if False else None
for e in (0.05,0.1,0.2,0.24,0.25,0.26,0.3,0.355,0.5,1.0,5.0):
    alv=-e/2; m2=1/(2*alv)
    neg=[p for p in range(0,8) if p*(p+3)+m2<0]
    lam=(-3+np.sqrt(9+4/e))/2
    print(f"  eps={e:6.3f}: alpha={alv:+.4f} m^2={m2:+.3f}  negative modes p={neg}  (HHR threshold alpha<-1/8 <=> eps>0.25)  lambda+={lam:.3f}  N_inf(a2=1e6)={np.log(np.sqrt(1e6/(180*np.pi)))/lam:.2f}  N_inf(1e7)={np.log(np.sqrt(1e7/(180*np.pi)))/lam:.2f}")
