import numpy as np
from scipy.integrate import trapezoid, cumulative_trapezoid
src=open('caps.py').read().split("res={}")[0]; exec(src)
def half_pieces(e,c3):
    ex,cl,sol=run(c3,e,dense=True)
    tsym=ex[1][0] if len(ex)>=3 else ex[0][0]          # neck for DB, equator for sphere
    ts=np.linspace(sol.t[0],tsym,400001); Y=sol.sol(ts); A,A1,A2=Y[0],Y[1],Y[2]
    EH=2*2*np.pi**2*trapezoid((-(6/(16*np.pi**2))*A**2*(1+A1**2))/A,ts)
    R2=2*2*np.pi**2*trapezoid((36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2-A1**2)**2)/A,ts)
    eta=cumulative_trapezoid(1/A,ts,initial=0); eta-=eta[-1]                       # eta=0 at the symmetric point
    s=np.log(A)+np.log(np.cosh(eta)); s1=A1+np.tanh(eta); s2=A*A2+np.cosh(eta)**-2
    G=2*0.125*trapezoid((24*np.cosh(eta)**-4*s + 2*(s2-2*np.tanh(eta)*s1)**2 + 4*np.cosh(eta)**-2*s1**2)/A,ts)
    # symmetry check at the symmetric point: a''' there
    return EH,R2,G,(ex[0][1], ex[1][1] if len(ex)>=3 else None, ex[1][4] if len(ex)>=3 else ex[0][4])
H={0.36:-0.122,0.40:-0.166,0.45:-0.228,0.5:-0.299,1.0:-1.314,2.0:-4.144,5.0:-14.43}
print("sphere half*2:",[f"{x:+.5f}" for x in half_pieces(1.0,-1/6)[:3]])
for e,c3 in ((0.36,-0.347204),(0.40,-0.350687),(0.45,-0.353077),(0.5,-0.354147),(1.0,-0.349489),(2.0,-0.342261),(5.0,-0.337009),(10.0,-0.335180)):
    EH,R2,G,(ap,an,a3)=half_pieces(e,c3); dI=(EH+2)+(R2+(4/3)*(3*e+1))+G
    print(f"eps={e:5.2f}: dEH={EH+2:+.2e} dR2={R2+(4/3)*(3*e+1):+.4f} dGamma={G:+.4f} => dI/a={dI:+.4f}  (H: {H.get(e,float('nan')):+.3f})  [a_peak={ap:.4f} a_neck={an:.4f} a'''_neck={a3:+.1e}]")
