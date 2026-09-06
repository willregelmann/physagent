import sympy as sp, pickle
eta=sp.symbols('eta'); s=sp.Function('sigma')(eta)
G,aa,kap,s1=sp.symbols('G a_anom kappa s1')   # aa = Duff-normalized a (=a2/180); G a_anom = pi at H0=1
# Minisuperspace Lagrangian per Vol(S^3)=2pi^2, metric g = e^{2 sigma} (d eta^2 + dOmega_3^2)
L_EH=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*s)*(1+sp.diff(s,eta)**2)
L_an=s1*(aa/(16*sp.pi**2))*(2*sp.diff(s,eta,2)**2+8*sp.diff(s,eta)**2)   # from 2 sigma Delta4 sigma on ESU, by parts
L_R2=36*kap*(1-sp.diff(s,eta,2)-sp.diff(s,eta)**2)**2
L=L_EH+L_an+L_R2
# Euler-Lagrange for 4th-order: dL/ds - d/deta dL/ds' + d^2/deta^2 dL/ds''
sd=sp.diff(s,eta); sdd=sp.diff(s,eta,2)
X0,X1,X2=sp.symbols('X0 X1 X2')
Lx=L.subs({sdd:X2}).subs({sd:X1}).subs({s:X0})
EL=sp.diff(Lx,X0)-sp.diff(sp.diff(Lx,X1),eta)+sp.diff(sp.diff(Lx,X2),eta,2)
EL=EL.subs({X0:s,X1:sd,X2:sdd}).doit()
EL=sp.simplify(EL)
# Now the trace equation in eta-time: compute curvature for metric a(eta)^2 (d eta^2 + dOmega^2) via conformal transformation formulas
# For g = e^{2 sigma} gbar, gbar=ESU (Rbar=6): R = e^{-2 sigma}(6 - 6 sigma'' - 6 sigma'^2);
# box R = e^{-2sigma} (Rbar-box-ish): for f(eta) on g: box_g f = e^{-4 sigma} d/deta ( e^{2 sigma} f' )  [since sqrt g = e^{4 sigma}, g^{eta eta}=e^{-2 sigma}]
Rg=sp.exp(-2*s)*(6-6*sdd-6*sd**2)
boxRg=sp.exp(-4*s)*sp.diff(sp.exp(2*s)*sp.diff(Rg,eta),eta)
# E4 on conformally flat: E4 = (2/3)R^2 - 2 Ric^2 ; get Ric^2 from the tau-frame result by converting? simpler: use identity sqrt(g)(E4 - 2/3 box R) = sqrt(gbar)(Ebar4 - 2/3 boxbar Rbar + 4 Delta4bar sigma), Ebar4=0 on ESU
Delta4s=sp.diff(s,eta,4)-4*sdd
E4g=sp.exp(-4*s)*4*Delta4s+sp.Rational(2,3)*boxRg
# trace equation (H0=1, G a_anom = pi): R - (1/2) E4 - eps box R = 0 ; multiply by sqrt(g)=e^{4 sigma}
epsl=sp.symbols('epsilon')
TR=sp.simplify(sp.exp(4*s)*(Rg-sp.Rational(1,2)*E4g-epsl*boxRg))
# match: EL should be proportional to TR. Solve for s1, kappa by comparing coefficients of the highest derivatives
ratio=sp.simplify(EL/TR)
print("EL/TR simplified:",ratio)
# if not constant, solve coefficient matching on sigma'''' and sigma^2-free terms
ELs=sp.expand(EL.subs(G,sp.pi/aa)); TRs=sp.expand(TR)
c_EL4=ELs.coeff(sp.diff(s,eta,4)); c_TR4=TRs.coeff(sp.diff(s,eta,4))
print("coeff of sigma'''' : EL",sp.factor(c_EL4)," TR",sp.factor(c_TR4))
# terms with no derivatives: set derivatives to zero
zero={sp.diff(s,eta,4):0,sp.diff(s,eta,3):0,sdd:0,sd:0}
print("no-derivative terms: EL",sp.simplify(ELs.subs(zero))," TR",sp.simplify(TRs.subs(zero)))
pickle.dump({'L':L,'EL':EL,'TR':TR},open('action.pkl','wb'))
