# Steelman check (flaw 5 / 17): the FULL lapse Euler-Lagrange expression EL_N = dL/dN - d/dt(dL/dN') on the round
# sphere in the FLT gauge, for the ESU-frame anomaly constant C in {-8, 0, +8}.  The attack's esu_const.py and the
# position's lapse_action.py both printed only the partial derivative dL_t/dN, but sigma'' contains N-dot, so the
# constraint is EL_N, not dL/dN.  Also the reparametrization (Noether) identity: q-dot * EL_q - N * d/dt EL_N = 0.
import sympy as sp
t=sp.symbols('t'); aa,epsl=sp.symbols('a_anom epsilon',positive=True); G=sp.pi/aa
q=sp.Function('q')(t); Nf=sp.Function('N')(t)
X0,X1,X2=sp.symbols('X0 X1 X2')
kap=-aa*(3*epsl+1)/(288*sp.pi**2)
def build(C):
    L_eta=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)+(aa/(16*sp.pi**2))*(2*X2**2+8*X1**2+C)+36*kap*(1-X2-X1**2)**2
    sig=sp.log(q)/2; s1=(q/Nf)*sp.diff(sig,t); s2=(q/Nf)*sp.diff(s1,t)
    Lt=(Nf/q)*L_eta.subs({X0:sig,X1:s1,X2:s2})
    # generic EL for q and N via jet substitution
    Q=sp.symbols('Q0:5'); Nn=sp.symbols('n0:3')
    qd=[q]+[sp.diff(q,t,k) for k in range(1,5)]; Nd=[Nf]+[sp.diff(Nf,t,k) for k in range(1,3)]
    fwd={}
    for k in range(4,-1,-1): fwd[qd[k]]=Q[k]
    for k in range(2,-1,-1): fwd[Nd[k]]=Nn[k]
    back={Q[k]:qd[k] for k in range(5)}; back.update({Nn[k]:Nd[k] for k in range(3)})
    Lj=sp.expand(Lt.subs(fwd))
    ELq=(sp.diff(Lj,Q[0]).subs(back)-sp.diff(sp.diff(Lj,Q[1]).subs(back),t)+sp.diff(sp.diff(Lj,Q[2]).subs(back),t,2)).doit()
    ELN=(sp.diff(Lj,Nn[0]).subs(back)-sp.diff(sp.diff(Lj,Nn[1]).subs(back),t)+sp.diff(sp.diff(Lj,Nn[2]).subs(back),t,2)).doit()
    dLdN=sp.diff(Lj,Nn[0]).subs(back)
    return ELq,ELN,dLdN
Nv=sp.Rational(1,2); qs=1-(1-Nv*t)**2        # round sphere: q = sin^2 tau, tau = acos(1 - N t)
for C in (-8,0,8):
    ELq,ELN,dLdN=build(C)
    sub={q:qs,Nf:Nv}
    e_q=sp.simplify(ELq.subs(sub).doit())
    e_N=sp.simplify(ELN.subs(sub).doit())
    d_N=sp.simplify(dLdN.subs(sub).doit())
    print(f"C={C:+d}: EL_q(sphere) = {sp.factor(e_q)}")
    print(f"        partial dL_t/dN (sphere) = {sp.factor(d_N)}")
    print(f"        FULL EL_N = dL/dN - d/dt(dL/dNdot) (sphere) = {sp.factor(e_N)}")
# Noether identity check on a generic q, constant N, for C=+8
ELq,ELN,_=build(8)
qq=sp.Function('qq')(t)
ident=sp.simplify((sp.diff(q,t)*ELq - Nf*sp.diff(ELN,t)).subs(Nf,Nv).doit())
print("Noether identity  qdot*EL_q - N*d/dt(EL_N) on generic q at constant N (C=+8):",ident)
