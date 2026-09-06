import sympy as sp, pickle
tau=sp.symbols('tau'); a=sp.Function('a')(tau); eps=sp.symbols('epsilon'); t,N=sp.symbols('t N')
A0,A1,A2,A3=sp.symbols('A0 A1 A2 A3')
kap=-(3*eps+1)/(288*sp.pi**2)
def Ltau(sub):   # per a_anom; sub = constant subtracted from a'^2 in the 8(...) term
    return (-(sp.Integer(6)/(16*sp.pi**2))*A0**2*(1+A1**2)+(1/(16*sp.pi**2))*(2*(A0*A2)**2+8*(A1**2-sub))+36*kap*(1-A0*A2-A1**2)**2)/A0
def EL(L):
    back={A0:a,A1:sp.diff(a,tau),A2:sp.diff(a,tau,2)}
    return sp.expand((sp.diff(L,A0).subs(back)-sp.diff(sp.diff(L,A1).subs(back),tau)+sp.diff(sp.diff(L,A2).subs(back),tau,2)).doit())
def Ham(L):
    back={A0:a,A1:sp.diff(a,tau),A2:sp.diff(a,tau,2)}
    pa1=sp.diff(L,A2).subs(back); pa=sp.diff(L,A1).subs(back)-sp.diff(pa1,tau)
    return sp.simplify(pa*sp.diff(a,tau)+pa1*sp.diff(a,tau,2)-L.subs(back))
for sub,lab in ((1,'J-1 regularized 8(a\'^2-1)'),(0,'unsubtracted 8a\'^2')):
    L=Ltau(sub); e=EL(L); h=Ham(L)
    print("==",lab)
    print("  EL_tau on sphere a=sin(tau):",sp.simplify(e.subs(a,sp.sin(tau)).doit()))
    print("  Hamiltonian on sphere:",sp.simplify(h.subs(a,sp.sin(tau)).doit()))
    print("  Hamiltonian, general (times 16 pi^2 a):",sp.factor(sp.simplify(h*16*sp.pi**2*a)))
# also: does EL_tau of the unsubtracted L equal (factor) * trace equation?
d=pickle.load(open('curv.pkl','rb'))
TR=sp.expand(sp.simplify((d['R']-sp.Rational(1,2)*d['E4']-eps*d['boxR'])*a**3))
for sub,lab in ((1,'reg'),(0,'unsub')):
    e=EL(Ltau(sub)); r=sp.simplify(e/TR); print(lab,": EL_tau / (a^3 * TR) =",r)
