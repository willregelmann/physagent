import sympy as sp, pickle, numpy as np
t=sp.symbols('t'); N=sp.symbols('N_E'); aa,epsl=sp.symbols('a_anom epsilon'); G=sp.pi/aa
q=sp.Function('q')(t); X0,X1,X2=sp.symbols('X0 X1 X2')
kap=-aa*(3*epsl+1)/(288*sp.pi**2)
L_eta=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)+(aa/(16*sp.pi**2))*(2*X2**2+8*X1**2)+36*kap*(1-X2-X1**2)**2
sig=sp.log(q)/2; s1=(q/N)*sp.diff(sig,t); s2=(q/N)*sp.diff(s1,t)
Lt=sp.expand(sp.simplify((N/q)*L_eta.subs({X0:sig,X1:s1,X2:s2})))
qd=[q]+[sp.diff(q,t,k) for k in range(1,5)]; Q=sp.symbols('Q0:5')
fwd={qd[k]:Q[k] for k in range(4,-1,-1)}; back={Q[k]:qd[k] for k in range(5)}
Lq=Lt.subs(fwd)
EL=(sp.diff(Lq,Q[0]).subs(back)-sp.diff(sp.diff(Lq,Q[1]).subs(back),t)+sp.diff(sp.diff(Lq,Q[2]).subs(back),t,2)).doit()
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
A=[sp.sqrt(q)]
for k in range(4): A.append((sp.sqrt(q)/N)*sp.diff(A[-1],t))
rep={sp.Derivative(a,(tau,4)):A[4],sp.Derivative(a,(tau,3)):A[3],sp.Derivative(a,(tau,2)):A[2],sp.Derivative(a,tau):A[1]}
TR=((d['R']-sp.Rational(1,2)*d['E4']-epsl*d['boxR']).subs(rep).subs(a,A[0])).doit()
ELn=sp.lambdify((Q[0],Q[1],Q[2],Q[3],Q[4],N,aa,epsl),EL.subs(fwd)); TRn=sp.lambdify((Q[0],Q[1],Q[2],Q[3],Q[4],N,aa,epsl),TR.subs(fwd))
rng=np.random.default_rng(1)
for k in range(5):
    v=rng.uniform(0.3,2.0,5); Nv=rng.uniform(0.5,2); e=rng.uniform(-1,3)
    r=ELn(*v,Nv,1.0,e)/TRn(*v,Nv,1.0,e)
    print(f"random point {k}: EL/TR = {r:+.8f}   -N/(16 pi^2) = {-Nv/(16*np.pi**2):+.8f}   ratio/that = {r/(-Nv/(16*np.pi**2)):.8f}")
# Lorentzian continuation N_E = i N with q real: is L_t(iN) = i * real ?
qr=sp.Function('u',real=True)(t); NL=sp.symbols('N',positive=True)
LtL=sp.expand(Lt.subs(q,qr).doit().subs(N,sp.I*NL))
print("Re L_t(N_E=iN) with real q:",sp.simplify(sp.re(LtL)))
