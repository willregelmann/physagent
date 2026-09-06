# Lapse-gauge Lagrangian with the ESU-form subtraction 8(s'^2 - sub): sub=+1 (position/J-1), sub=-1 (attack's fix).
import sympy as sp, numpy as np, sys
sys.path.insert(0,'..')
t=sp.symbols('t'); q=sp.Function('q')(t); N,eps=sp.symbols('N epsilon'); Q0,Q1,Q2,Q3=sp.symbols('Q0:4')
a=sp.sqrt(Q0); s1=Q1/(2*N); s2=a*sp.sqrt(Q0)*Q2/(2*N**2)
kap=-(3*eps+1)/(288*sp.pi**2)
def Lt(sub):
    L_eta=-(sp.Integer(6)/(16*sp.pi**2))*a**2*(1+s1**2)+(1/(16*sp.pi**2))*(2*s2**2+8*(s1**2-sub))+36*kap*(1-s2-s1**2)**2
    return sp.expand(sp.simplify(L_eta/a*N/sp.sqrt(Q0)))
back={Q0:q,Q1:sp.diff(q,t),Q2:sp.diff(q,t,2)}
qs=2*N*t-N**2*t**2
Hs={}
for sub in (1,-1):
    L=Lt(sub)
    EL=(sp.diff(L,Q0).subs(back)-sp.diff(sp.diff(L,Q1).subs(back),t)+sp.diff(sp.diff(L,Q2).subs(back),t,2)).doit()
    ELs=sp.factor(sp.simplify(EL.subs(q,qs).doit()))
    H=sp.diff(L,N); Hs[sub]=H
    Hsph=sp.factor(sp.simplify(H.subs({Q0:qs,Q1:sp.diff(qs,t),Q2:sp.diff(qs,t,2)})))
    pqd=sp.simplify(sp.diff(L,Q2))
    pq=sp.simplify(sp.diff(L,Q1)-sp.diff(sp.diff(L,Q2).subs(back),t).subs({sp.diff(q,t,3):Q3,sp.diff(q,t,2):Q2,sp.diff(q,t):Q1,q:Q0}))
    print(f"sub={sub:+d}:\n  EL_q(sphere, fixed N) = {ELs}\n  dL/dN(sphere)         = {Hsph}\n  p_qdot = {pqd}\n  p_q    = {pq}")
    print("  leading pole behaviour of p_q (q->0 with qdot=2N, qddot=12 c3 N^2, qdddot finite):",sp.series(pq.subs({Q1:2*N,Q2:12*sp.Symbol('c3')*N**2,Q3:sp.Symbol('d3')}),Q0,0,1))
print("difference L_t(sub=-1) - L_t(sub=+1) =",sp.simplify(Lt(-1)-Lt(1)),"  (a radiation-like N/q term: integrates to 2*int d eta per a, log-divergent at a regular pole)")
# numeric: the constraint dL/dN along a regular double-bubble cap (eps=1), both subs
from ccaps import integrate_path
e=1.0; c3=-0.349489; Nv=1.3
Hf={s:sp.lambdify((Q0,Q1,Q2,N,eps),Hs[s]) for s in (1,-1)}
print("constraint dL_t/dN along the eps=1 double bubble (N=1.3 arbitrary constant):")
for tv in (0.3,0.8,1.185,1.6,2.1059):
    y,_=integrate_path(c3,e,[tv]); A,A1,A2=y[0].real,y[1].real,y[2].real
    q0=A**2; q1=2*Nv*A*A1; q2=2*Nv**2*A2/A
    print(f"  tau={tv:.4f}: a={A:.4f}  dL/dN(sub=+1)={Hf[1](q0,q1,q2,Nv,e):+.3e}   dL/dN(sub=-1)={Hf[-1](q0,q1,q2,Nv,e):+.3e}")
