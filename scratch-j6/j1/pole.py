import sympy as sp, pickle
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']
eps=sp.symbols('epsilon')            # B in units H0=1 (coeff = 1/2 so that S^4 of radius 1 solves it)
ode=sp.simplify(R-sp.Rational(1,2)*E4-eps*boxR)   # trace equation, Euclidean, H0=1
# check S^4 radius 1 solves for any eps
print("S4(radius1) residual:",sp.simplify(ode.subs(a,sp.sin(tau)).doit()))
# pole series a = tau + c3 tau^3 + c5 tau^5 + c7 tau^7 + c9 tau^9
c3,c5,c7,c9=sp.symbols('c3 c5 c7 c9')
ser=tau+c3*tau**3+c5*tau**5+c7*tau**7+c9*tau**9
expr=sp.simplify(ode.subs(a,ser).doit())
num=sp.numer(sp.together(expr))
p=sp.Poly(sp.expand(num),tau)
coeffs=p.all_coeffs()[::-1]   # ascending
for k,cf in enumerate(coeffs[:8]):
    cf=sp.factor(cf)
    if cf!=0: print(f"tau^{k}:",cf)
# solve order by order
sol5=sp.solve(coeffs[[k for k,cf in enumerate(coeffs) if sp.expand(cf)!=0][0]],c5); print("c5 =",sol5)
