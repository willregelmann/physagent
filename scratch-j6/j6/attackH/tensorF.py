# Tensor quadratic form on the round S^4 in the anomaly + R^2 theory, from Hawking-Hertog-Reall (2001) eq. (3.77),(3.82):
#   F(p,alpha,beta) = p^2+3p+6 + Psi(p) + 2 beta p(p+1)(p+2)(p+3) - 4 alpha p(p+3),   p = 2,3,...
#   Psi(p) = p(p+1)(p+2)(p+3)[psi(p/2+5/2)+psi(p/2+2)-psi(2)-psi(1)] + p^4+2p^3-5p^2-10p-6
# Map to J-1 variables: HHR alpha = -eps/2 (derived in position-T.md, sec. 2.2).
import numpy as np
from scipy.special import digamma as psi
def Psi(p):
    return p*(p+1)*(p+2)*(p+3)*(psi(p/2+2.5)+psi(p/2+2)-psi(2)-psi(1)) + p**4+2*p**3-5*p**2-10*p-6
def F(p,eps,beta):
    alpha=-eps/2
    return p**2+3*p+6 + Psi(p) + 2*beta*p*(p+1)*(p+2)*(p+3) - 4*alpha*p*(p+3)
def Einstein(p): return p**2+3*p+6
print("Psi(p) and ratio F/Einstein at beta=0, eps=1:")
for p in (2,3,4,6,10,20,40,100,1000):
    print(f"p={p:5d}  Einstein={Einstein(p):10.1f}  Psi={Psi(p):14.1f}  Psi/(2p^4 ln(p/2))={Psi(p)/(2*p**4*np.log(p/2)) if p>2 else float('nan'):7.3f}  F(eps=1,b=0)/E={F(p,1,0)/Einstein(p):9.2f}")
print("\nSign of F(p) for p in [2,200] over the local-Weyl coefficient beta (HHR flat-space stability needs beta > ln2-1 = %.3f):"%(np.log(2)-1))
ps=np.arange(2,201)
for beta in (1.0,0.0,np.log(2)-1,-0.5,-1,-2,-3,-4,-5,-6):
    for eps in (0.0,1.0,5.0):
        vals=F(ps,eps,beta); neg=ps[vals<0]
        s=f"none" if len(neg)==0 else f"F<0 for p in [{neg.min()},{neg.max()}]  (p_* = {neg.max()+1})"
        print(f"beta={beta:+6.3f} eps={eps:4.1f}: negative modes: {s}")
# window needed to cover trans-Planckian cutoff p_* ~ M_P/H0 = sqrt(a2/(180 pi))
for a2 in (1e6,1e7):
    print(f"a2={a2:.0e}: M_P/H0 = {np.sqrt(a2/(180*np.pi)):.1f}")
