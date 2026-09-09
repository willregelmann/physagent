# STEELMAN flaw 1 + flaw 2 (conical initial data, §7 of the J-7a note).
# (1) Closed form of the sign-change threshold v*(eps) of the log coefficient; sector decomposition (R^2 vs anomaly).
# (2) A smoothing family that satisfies ALL fourth-order pole-regularity conditions (a odd near the pole: a(0)=0, a'(0)=1, a''(0)=0),
#     a = tau + (v-1) tau^3/(tau^2+delta^2), still has the same log divergence -> no pole condition bounds the exponent.
#     Compare with the note's family a = tau + (v-1)(sqrt(tau^2+delta^2)-delta), which has a''(0) = (v-1)/delta (R ~ 1/tau at the tip).
import sympy as sp, numpy as np
from scipy.integrate import quad
v,eps,tau,d=sp.symbols('v epsilon tau delta',positive=True)
coef=-(v-1)**2*(3*eps*(v+1)**2+(v-1)*(v+3))/(4*v)
print("(1) c(v)-c(1) =",sp.factor(coef))
R2part=-3*eps*(v**2-1)**2/(4*v); anpart=-(v-1)**3*(v+3)/(4*v)
print("    R^2 sector: ",sp.factor(R2part)," (<=0 for all v>0, every eps>0)")
print("    anomaly sector:",sp.factor(anpart)," (>0 for v<1, <0 for v>1)")
print("    check sum:",sp.simplify(R2part+anpart-coef))
# threshold: bracket 3eps(v+1)^2+(v-1)(v+3)=0 -> (3eps+1)v^2+(6eps+2)v+(3eps-3)=0
vs=sp.solve(sp.Eq(3*eps*(v+1)**2+(v-1)*(v+3),0),v)
print("    roots of the bracket:",[sp.simplify(r) for r in vs])
vstar=2/sp.sqrt(1+3*eps)-1
print("    closed form v*(eps) = 2/sqrt(1+3 eps) - 1 ; check bracket at v*:",sp.simplify((3*eps*(v+1)**2+(v-1)*(v+3)).subs(v,vstar)))
for e in (0.25,0.3,0.355,0.5,0.8,1.0):
    print(f"      eps={e}: v*={float(vstar.subs(eps,e)):.4f}  (I->+inf for 0<v<v*; I->-inf for v>v*, v!=1)")
print("    v*(eps)>0 iff eps<1 ; v*(1)=0 ; at eps>=1 the coefficient is <=0 for every v>0:",sp.factor(coef.subs(eps,1)))
print("    near v=1 (both signs of v-1):",sp.series(coef,v,1,4))
print("    v->0+:",sp.limit(coef*v,v,0),"/v")
print("    v->inf:",sp.limit(coef/v**3,v,sp.oo),"* v^3")
# (2) quadrature: note's family vs fully regular odd family
def L(a,vv,w,e):
    C=8; kap=-(3*e+1)/(288*np.pi**2)
    return 2*np.pi**2*(-(6/(16*np.pi**2))*a**2*(1+vv**2)+(1/(16*np.pi**2))*(2*a**2*w**2+8*vv**2+C)+36*kap*(1-a*w-vv**2)**2)/a
def cone_note(vv,dd,e,tau1=1.0):
    f=lambda t: t+(vv-1)*(np.sqrt(t*t+dd*dd)-dd); fp=lambda t: 1+(vv-1)*t/np.sqrt(t*t+dd*dd); fpp=lambda t: (vv-1)*dd*dd/(t*t+dd*dd)**1.5
    return quad(lambda t: L(f(t),fp(t),fpp(t),e),1e-9,tau1,limit=400,points=[dd,10*dd])[0]
def cone_odd(vv,dd,e,tau1=1.0):
    # a = tau + (v-1) tau^3/(tau^2+d^2): a(0)=0, a'(0)=1, a''(0)=0, a'''(0)=6(v-1)/d^2 (i.e. c3=(v-1)/d^2), a -> v tau for tau>>d
    f=lambda t: t+(vv-1)*t**3/(t*t+dd*dd)
    fp=lambda t: 1+(vv-1)*(t**4+3*t*t*dd*dd)/(t*t+dd*dd)**2
    fpp=lambda t: (vv-1)*(6*t*dd**4-2*t**3*dd*dd)/(t*t+dd*dd)**3
    return quad(lambda t: L(f(t),fp(t),fpp(t),e),1e-9,tau1,limit=400,points=[dd,10*dd])[0]
# symbolic check of the odd family's pole data and curvature
af=tau+(v-1)*tau**3/(tau**2+d**2)
print("(2) odd family: a'(0)=",sp.simplify(sp.diff(af,tau).subs(tau,0))," a''(0)=",sp.simplify(sp.diff(af,tau,2).subs(tau,0))," a'''(0)=",sp.simplify(sp.diff(af,tau,3).subs(tau,0)))
Rf=lambda A: -6*(A*sp.diff(A,tau,2)+sp.diff(A,tau)**2-1)/A**2
print("    odd family R at tau->0:",sp.limit(Rf(af),tau,0),"  (finite: fully regular pole)")
an=tau+(v-1)*(sp.sqrt(tau**2+d**2)-d)
print("    note's family R at tau->0: ~",sp.limit(Rf(an)*tau,tau,0),"/tau  (integrable 1/tau curvature singularity at the tip: a''(0)=(v-1)/delta)")
print("    quadrature (dI/dln(1/delta) between delta=1e-3 and 1e-4):")
for e,vv in ((1.0,2.0),(1.0,0.1),(0.3,2.0),(0.3,0.1),(0.3,0.8),(0.3,1.2),(0.25,0.3)):
    pred=float(coef.subs({v:vv,eps:e}))
    In=[cone_note(vv,dd,e) for dd in (1e-3,1e-4)]; Io=[cone_odd(vv,dd,e) for dd in (1e-3,1e-4)]
    print(f"      eps={e} v={vv}: note-family slope={(In[1]-In[0])/np.log(10):+.4f}  odd(fully regular)-family slope={(Io[1]-Io[0])/np.log(10):+.4f}  sympy cone coeff={pred:+.4f}")
