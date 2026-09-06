# Does the round sphere satisfy the position's lapse-gauge (ESU-form, J-1 regularized) equations: EL_q at fixed N, and dL/dN (constraint)?
import sympy as sp, pickle
d=pickle.load(open('lapse.pkl','rb'))   # written by lapse_setup.py rerun in this directory
t=sp.symbols('t'); q=sp.Function('q')(t); N,eps=sp.symbols('N epsilon')
Q0,Q1,Q2,Q3,Q4=sp.symbols('Q0 Q1 Q2 Q3 Q4')
print("keys:",list(d.keys()))
EL=d['EL']; H=d['H']; Lt=d['Lt']
qs=2*N*t-N**2*t**2   # unit sphere, tau = arccos(1-Nt)
ELs=sp.simplify(EL.subs(q,qs).doit())
print("EL_q (fixed N) on the sphere:",sp.factor(ELs))
Hs=sp.simplify(H.subs({Q0:qs,Q1:sp.diff(qs,t),Q2:sp.diff(qs,t,2)}))
print("dL_t/dN on the sphere:",sp.factor(Hs))
# what about the same with the '8(s1^2 - sub)' term for sub=0 and sub=-1 ? rebuild L_t quickly
a=sp.sqrt(Q0); at=Q1/(2*N); att=sp.sqrt(Q0)*Q2/(2*N**2); s1=at; s2=a*att
kap=-(3*eps+1)/(288*sp.pi**2)
for sub in (1,0,-1):
    L_eta=-(sp.Integer(6)/(16*sp.pi**2))*a**2*(1+s1**2)+(1/(16*sp.pi**2))*(2*s2**2+8*(s1**2-sub))+36*kap*(1-s2-s1**2)**2
    L=sp.expand(sp.simplify(L_eta/a*N/sp.sqrt(Q0)))
    Hn=sp.simplify(sp.diff(L,N).subs({Q0:qs,Q1:sp.diff(qs,t),Q2:sp.diff(qs,t,2)}))
    back={Q0:q,Q1:sp.diff(q,t),Q2:sp.diff(q,t,2)}
    ELn=sp.diff(L,Q0).subs(back)-sp.diff(sp.diff(L,Q1).subs(back),t)+sp.diff(sp.diff(L,Q2).subs(back),t,2)
    ELn=sp.simplify(ELn.doit().subs(q,qs).doit())
    print(f"sub={sub:+d}: dL/dN on sphere = {sp.factor(Hn)} ;  EL_q on sphere = {sp.factor(ELn)}")
