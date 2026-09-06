# EL check in the FLT lapse gauge with the UNregularized anomaly term (the pole subtraction 8(sigma'^2-1) is a constant only per unit eta).
import sympy as sp, pickle
t=sp.symbols('t'); N=sp.symbols('N_E'); aa,epsl=sp.symbols('a_anom epsilon'); G=sp.pi/aa
q=sp.Function('q')(t); X0,X1,X2=sp.symbols('X0 X1 X2')
kap=-aa*(3*epsl+1)/(288*sp.pi**2)
L_eta=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)+(aa/(16*sp.pi**2))*(2*X2**2+8*X1**2)+36*kap*(1-X2-X1**2)**2
sig=sp.log(q)/2; s1=(q/N)*sp.diff(sig,t); s2=(q/N)*sp.diff(s1,t)
Lt=sp.expand(sp.simplify((N/q)*L_eta.subs({X0:sig,X1:s1,X2:s2})))
qd=[q]+[sp.diff(q,t,k) for k in range(1,5)]; Q=sp.symbols('Q0:5')
fwd={qd[k]:Q[k] for k in range(4,-1,-1)}; back={Q[k]:qd[k] for k in range(5)}
Lq=Lt.subs(fwd)
EL=sp.diff(Lq,Q[0]).subs(back)-sp.diff(sp.diff(Lq,Q[1]).subs(back),t)+sp.diff(sp.diff(Lq,Q[2]).subs(back),t,2)
EL=sp.simplify(EL.doit())
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
A=[sp.sqrt(q)]
for k in range(4): A.append((sp.sqrt(q)/N)*sp.diff(A[-1],t))
rep={sp.Derivative(a,(tau,4)):A[4],sp.Derivative(a,(tau,3)):A[3],sp.Derivative(a,(tau,2)):A[2],sp.Derivative(a,tau):A[1]}
TR=sp.simplify((d['R']-sp.Rational(1,2)*d['E4']-epsl*d['boxR']).subs(rep).subs(a,A[0]))
ratio=sp.simplify(EL/TR)
print("EL(q; fixed N_E)/(trace eq) =",ratio,"   expected -a N_E q/(16 pi^2)")
# Lorentzian continuation N_E -> i N: the Lagrangian per unit t
NL=sp.symbols('N',positive=True)
LtL=sp.simplify(Lt.subs(N,sp.I*NL))
print("L_t(N_E = iN) purely imaginary? ", sp.simplify(sp.re(sp.expand(LtL.subs({aa:1,epsl:1}).subs(q,sp.Function('u')(t))))) )
pickle.dump({'Lt':Lt},open('lapseL.pkl','wb'))
