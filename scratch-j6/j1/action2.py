import sympy as sp, pickle
eta=sp.symbols('eta'); s=sp.Function('sigma')(eta)
G,aa,kap,s1=sp.symbols('G a_anom kappa s1'); epsl=sp.symbols('epsilon')
sd=sp.diff(s,eta); sdd=sp.diff(s,eta,2)
X0,X1,X2=sp.symbols('X0 X1 X2')
L_EH=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)
L_an=s1*(aa/(16*sp.pi**2))*(2*X2**2+8*X1**2)
L_R2=36*kap*(1-X2-X1**2)**2
L=L_EH+L_an+L_R2
back={X0:s,X1:sd,X2:sdd}
EL=sp.diff(L,X0).subs(back)-sp.diff(sp.diff(L,X1).subs(back),eta)+sp.diff(sp.diff(L,X2).subs(back),eta,2)
EL=sp.expand(EL.doit())
# identity check: e^{4 sigma}(E4 - 2/3 box R) == 4 Delta4bar sigma on the ESU frame?
Rg=sp.exp(-2*s)*(6-6*sdd-6*sd**2)
boxRg=sp.exp(-4*s)*sp.diff(sp.exp(2*s)*sp.diff(Rg,eta),eta)
# get E4 honestly from the tau-frame invariants via the chain rule: use pickled E4 in terms of a(tau), convert with a(tau)=e^{sigma(eta)}, d/dtau = e^{-sigma} d/deta
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
A=[sp.exp(s)]
for k in range(4): A.append(sp.exp(-s)*sp.diff(A[-1],eta))   # A[k] = d^k a/dtau^k expressed in eta
rep={sp.Derivative(a,(tau,4)):A[4],sp.Derivative(a,(tau,3)):A[3],sp.Derivative(a,(tau,2)):A[2],sp.Derivative(a,tau):A[1]}
E4g=sp.simplify(d['E4'].subs(rep).subs(a,A[0]))
Rchk=sp.simplify(d['R'].subs(rep).subs(a,A[0])-Rg); print("R consistency (tau->eta):",Rchk)
boxchk=sp.simplify(d['boxR'].subs(rep).subs(a,A[0])-boxRg); print("boxR consistency:",boxchk)
ident=sp.simplify(sp.exp(4*s)*(E4g-sp.Rational(2,3)*boxRg)-4*(sp.diff(s,eta,4)-4*sdd)); print("Riegert identity residual:",ident)
TR=sp.expand(sp.simplify(sp.exp(4*s)*(Rg-sp.Rational(1,2)*E4g-epsl*boxRg)))   # trace equation * sqrt(g), H0=1 units (G a_anom = pi)
ELs=sp.expand(EL.subs(G,sp.pi/aa))
# match: EL = mu * TR. Compare coefficients of sigma'''' and of the no-derivative term
zero={sp.diff(s,eta,4):0,sp.diff(s,eta,3):0,sdd:0,sd:0}
mu=sp.simplify(ELs.subs(zero)/TR.subs(zero)); print("mu from no-derivative terms:",mu)
c4=sp.simplify(ELs.coeff(sp.diff(s,eta,4))/TR.coeff(sp.diff(s,eta,4))); print("ratio of sigma'''' coefficients:",c4)
sol=sp.solve([sp.Eq(c4,mu)],[kap],dict=True); print("kappa(eps,s1):",sol)
for S1 in (1,-1):
    for so in sol:
        resid=sp.simplify((ELs-mu*TR).subs(so).subs(s1,S1))
        print("s1=",S1," full residual:",resid)
pickle.dump({'L':L,'mu':mu,'sol':sol},open('action2.pkl','wb'))
