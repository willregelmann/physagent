# ATTACK on §7 (conical initial data).
# (1) The note's own coefficient c(v,eps)-c(1,eps) = -(v-1)^2 [3 eps (v+1)^2 + (v-1)(v+3)]/(4v) is POSITIVE for narrow cones
#     (v<1 with 3 eps (1+v)^2 < (1-v)(3+v)) -> I -> +infinity, i.e. e^{+I} (tunneling sign) is UNBOUNDED there. Check sign map and quad.
# (2) Scheme independence: the note computes in the ESU/Riegert scheme. Compute the log coefficient of the KS a-anomaly functional
#     on the unit-S^4 reference (the anomaly sector of I_inv) on the cone a=v tau directly, and compare with ESU-anomaly + (1/288pi^2) int R^2.
import sympy as sp, numpy as np
from scipy.integrate import quad
v,eps,tau,th=sp.symbols('v epsilon tau theta',positive=True)
coef=-(v-1)**2*(3*eps*(v+1)**2+(v-1)*(v+3))/(4*v)
print("(1) note's coefficient c(v)-c(1) =",sp.factor(coef))
vstar=lambda e: sp.nsolve(3*e*(1+v)**2-(1-v)*(3+v),v,0.3)
for e in (0.25,0.3,0.355,0.5,0.8,1.0,2.0):
    try: vs=float(vstar(e))
    except Exception: vs=float('nan')
    vals={vv:float(coef.subs({v:vv,eps:e})) for vv in (0.05,0.1,0.2,0.3,0.45,0.6,0.8,1.2,2.0)}
    print(f"   eps={e}: threshold v*={vs:.4f} (I->+inf for v<v*); c(v)-c(1) at v=0.05..2: "+", ".join(f"{k}:{x:+.3f}" for k,x in vals.items()))
print("   limit v->0+ of the coefficient:",sp.limit(coef*v,v,0),"/v  -> sign of (1-eps): positive (I->+inf, e^{+I} unbounded) for eps<1")
# quad on the note's smoothing family for narrow cones at eps=0.3 (same L as cone_num.py)
def L(a,vv,w,e):
    C=8; kap=-(3*e+1)/(288*np.pi**2)
    return 2*np.pi**2*(-(6/(16*np.pi**2))*a**2*(1+vv**2)+(1/(16*np.pi**2))*(2*a**2*w**2+8*vv**2+C)+36*kap*(1-a*w-vv**2)**2)/a
def cone(vv,d,e,tau1=1.0):
    f=lambda t: t+(vv-1)*(np.sqrt(t*t+d*d)-d); fp=lambda t: 1+(vv-1)*t/np.sqrt(t*t+d*d); fpp=lambda t: (vv-1)*d*d/(t*t+d*d)**1.5
    val,err=quad(lambda t: L(f(t),fp(t),fpp(t),e),1e-9,tau1,limit=400,points=[d,10*d]); return val
print("(1b) quadrature on the smoothed-cone family (note's family, a'(0)=1) for narrow cones:")
for e in (0.3,0.5,1.0):
    for vv in (0.1,0.2,0.3,0.45):
        Is=[cone(vv,d,e) for d in (1e-2,1e-3,1e-4)]
        slope=(Is[2]-Is[1])/np.log(10)
        print(f"   eps={e} v={vv}: I(d=1e-2,1e-3,1e-4)={Is[0]:+.4f},{Is[1]:+.4f},{Is[2]:+.4f}  dI/dln(1/d)={slope:+.4f}  sympy={float(coef.subs({v:vv,eps:e})):+.4f}")
# (2) KS functional on the unit S^4 reference, cone a = v tau: dtheta/dtau = sin(theta)/a -> tan(theta/2) = K tau^(1/v); sigma = ln(a/sin theta)
print("(2) scheme independence of the anomaly-sector log coefficient on the cone:")
K=sp.symbols('K',positive=True)
theta=2*sp.atan(K*tau**(1/v))
a=v*tau
sig=sp.log(a/sp.sin(theta))
dth=sp.diff(theta,tau)
sig_th=sp.diff(sig,tau)/dth
sig_thth=sp.diff(sig_th,tau)/dth
GKS=sp.Rational(1,8)*sp.sin(theta)**3*(24*sig+12*sig_th**2+8*sig_thth*sig_th**2-2*sig_th**4)*dth   # per dtau, as in invariant.py dens10
# log coefficient = lim tau->0 of tau*GKS
cKS=sp.simplify(sp.limit(sp.simplify(tau*GKS),tau,0))
print("   KS (S^4 frame) log coefficient on the cone:",sp.factor(cKS))
# ESU Riegert anomaly sector on the cone (C=8): (1/8)(8 v^2 + 8)/(v tau) -> (v^2+1)/v ; plus the local scheme term (1/288pi^2) int sqrt g R^2 -> (1/4)(v^2-1)^2/v
cESU=(v**2+1)/v; cR2=sp.Rational(1,4)*(v**2-1)**2/v
print("   ESU Riegert anomaly log coeff:",cESU,"; (1/288pi^2) int R^2 log coeff:",sp.factor(cR2))
print("   ESU - R2 - KS =",sp.simplify(cESU-cR2-cKS),"  (should be 0 for scheme independence)")
print("   KS coefficient minus its regular value (v=1):",sp.factor(sp.simplify(cKS-cKS.subs(v,1))))
print("   [anomaly-sector part of the note's coefficient: (v-1)^2/v - (v^2-1)^2/(4v) =",sp.factor(sp.simplify((v-1)**2/v-(v**2-1)**2/(4*v))),"]")
# (3) the claim 'regular-pole restriction is a definition': the note's smoothing family HAS a'(0)=1. Print a'(0), a''(0) explicitly.
d=sp.symbols('delta',positive=True)
af=tau+(v-1)*(sp.sqrt(tau**2+d**2)-d)
print("(3) note's smoothing family: a(0)=",sp.simplify(af.subs(tau,0))," a'(0)=",sp.simplify(sp.diff(af,tau).subs(tau,0))," a''(0)=",sp.simplify(sp.diff(af,tau,2).subs(tau,0)))
