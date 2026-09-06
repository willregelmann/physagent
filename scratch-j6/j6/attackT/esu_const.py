# Attack check: ESU-frame lapse-gauge Lagrangian with anomaly bracket (2 s''^2 + 8 s'^2 + C), C in {-8, 0, +8}.
# Question: for which C does the round sphere q = sin^2(tau(t)) solve the fixed-N q-equation, and for which C
# does the lapse constraint dL_t/dN vanish on it?  Position T says "J-1's Lagrangian (with 8(s'^2-1)) has the sphere
# as a fixed-N solution only after adding (a/2pi^2) per unit eta" -- i.e. C = -8 -> C = 0.  Check that.
import sympy as sp
t=sp.symbols('t'); N=sp.symbols('N_E'); aa,epsl=sp.symbols('a_anom epsilon'); G=sp.pi/aa
q=sp.Function('q')(t); X0,X1,X2=sp.symbols('X0 X1 X2')
kap=-aa*(3*epsl+1)/(288*sp.pi**2)
def build(C):
    L_eta=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)+(aa/(16*sp.pi**2))*(2*X2**2+8*X1**2+C)+36*kap*(1-X2-X1**2)**2
    sig=sp.log(q)/2; s1=(q/N)*sp.diff(sig,t); s2=(q/N)*sp.diff(s1,t)
    Lt=sp.expand(sp.simplify((N/q)*L_eta.subs({X0:sig,X1:s1,X2:s2})))
    qd=[q]+[sp.diff(q,t,k) for k in range(1,5)]; Q=sp.symbols('Q0:5')
    fwd={qd[k]:Q[k] for k in range(4,-1,-1)}; back={Q[k]:qd[k] for k in range(5)}
    Lq=Lt.subs(fwd)
    EL=(sp.diff(Lq,Q[0]).subs(back)-sp.diff(sp.diff(Lq,Q[1]).subs(back),t)+sp.diff(sp.diff(Lq,Q[2]).subs(back),t,2)).doit()
    return Lt,EL
# sphere in lapse gauge with constant N: tau(t) = acos(1 - N t), q = sin^2 tau = 1-(1-Nt)^2
Nv=sp.Rational(1,2); qs=1-(1-Nv*t)**2
# Ostrogradsky energy per unit eta on the sphere (check of the position's H_eta = a/(2 pi^2) for C=0)
tau=sp.symbols('tau')
for C in (-8,0,8):
    Lt,EL=build(C)
    ELs=sp.simplify(EL.subs(q,qs).doit().subs({N:Nv,epsl:sp.Rational(3,2),aa:1}))
    dLdN=sp.simplify(sp.diff(Lt,N).subs(q,qs).doit().subs({N:Nv,epsl:sp.Rational(3,2),aa:1}))
    # integrated constraint over t in [0,1] (T = pi/2 half sphere for N=1/2? tau(1)=acos(1/2)=pi/3)
    integ=sp.integrate(dLdN,(t,sp.Rational(1,100),sp.Rational(9,10)))
    print(f"C={C:+d}: EL_q(sphere, fixed N) = {ELs}")
    print(f"        dL_t/dN on sphere = {sp.simplify(dLdN)}")
    print(f"        int_{0.01}^{0.9} dL/dN dt = {sp.N(integ,6)}")
# Ostrogradsky energy in eta of L_eta for each C on the sphere (sigma' = cos tau, sigma''=-sin^2 tau, sigma'''=-2 sin^2 cos)
s,s1v,s2v,s3v=sp.symbols('s s1 s2 s3')
for C in (-8,0,8):
    L=-(sp.Integer(6)/(16*sp.pi**2))*sp.exp(2*s)*(1+s1v**2)+(1/(16*sp.pi**2))*(2*s2v**2+8*s1v**2+C)+36*(-(3*epsl+1)/(288*sp.pi**2))*(1-s2v-s1v**2)**2
    p2=sp.diff(L,s2v); p1=sp.diff(L,s1v)
    # H = s1 p1 + s2 p2 - s1 (d/deta p2) - L ; d/deta p2 = dp2/ds1 * s2 + dp2/ds2 * s3
    dp2=sp.diff(p2,s1v)*s2v+sp.diff(p2,s2v)*s3v
    H=sp.simplify(s1v*p1+s2v*p2-s1v*dp2-L)
    Hs=sp.simplify(H.subs({s:sp.log(sp.sin(tau)),s1v:sp.cos(tau),s2v:-sp.sin(tau)**2,s3v:-2*sp.sin(tau)**2*sp.cos(tau)}))
    print(f"C={C:+d}: Ostrogradsky H_eta on sphere (per a, per 2pi^2) = {Hs}   [a/(2pi^2) = {sp.N(1/(2*sp.pi**2),6)}]")
