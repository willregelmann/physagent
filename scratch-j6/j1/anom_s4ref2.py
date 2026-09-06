import numpy as np
from scipy.integrate import trapezoid, cumulative_trapezoid
src=open('caps.py').read().split("res={}")[0]; exec(src)
# Gamma[s;S^4]/a = (1/16pi^2) * 2pi^2 * Int sech^4(eta) [24 s + 2 (box s)^2 + 4 cosh^2(eta) s'^2] d eta
#   with box s = cosh^2 s'' - 2 cosh sinh s'   (Paneitz on unit S^4 = box^2 - 2 box, integrated by parts)
# => Gamma/a = (1/8) Int [ 24 sech^4 s + 2 (s'' - 2 tanh s')^2 + 4 sech^2 s'^2 ] d eta
def Gamma_over_a(s,s1,s2,eta):
    return 0.125*trapezoid(24*np.cosh(eta)**-4*s + 2*(s2-2*np.tanh(eta)*s1)**2 + 4*np.cosh(eta)**-2*s1**2, eta)
# checks
eta=np.linspace(-15,15,300001)
for r in (0.5,2.0): print(f"radius {r}: {Gamma_over_a(np.full_like(eta,np.log(r)),0*eta,0*eta,eta):.6f} vs 4 ln r = {4*np.log(r):.6f}")
for e0 in (0.5,1.5):
    s=np.log(np.cosh(eta))-np.log(np.cosh(eta-e0)); s1=np.tanh(eta)-np.tanh(eta-e0); s2=np.cosh(eta)**-2-np.cosh(eta-e0)**-2
    print(f"Moebius {e0}: {Gamma_over_a(s,s1,s2,eta):.2e} (expect 0)")
def cap_pieces(e,c3):
    ex,cl,sol=run(c3,e,dense=True); tclose=sol.t_events[1][0]
    ts=np.linspace(sol.t[0],tclose,600001); Y=sol.sol(ts); A,A1,A2=Y[0],Y[1],Y[2]
    EH=2*np.pi**2*trapezoid((-(6/(16*np.pi**2))*A**2*(1+A1**2))/A,ts)
    R2=2*np.pi**2*trapezoid((36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2-A1**2)**2)/A,ts)
    tneck=ex[1][0] if len(ex)>=3 else ex[0][0]
    eta=cumulative_trapezoid(1/A,ts,initial=0); eta-=np.interp(tneck,ts,eta)
    s=np.log(A)+np.log(np.cosh(eta)); s1=A1+np.tanh(eta); s2=A*A2+np.cosh(eta)**-2   # d/d eta = a d/d tau
    # integrate in tau: d eta = d tau / A
    integrand=(24*np.cosh(eta)**-4*s + 2*(s2-2*np.tanh(eta)*s1)**2 + 4*np.cosh(eta)**-2*s1**2)/A
    G=0.125*trapezoid(integrand,ts)
    return EH,R2,G,ex
print("sphere by ODE (c3=-1/6):")
for e in (0.5,1.0):
    EH,R2,G,ex=cap_pieces(e,-1/6); print(f"  eps={e}: EH={EH:+.5f} (exp -2) R2={R2:+.5f} (exp {-(4/3)*(3*e+1):+.5f}) Gamma={G:+.2e} (exp 0)")
print("double bubble:")
J1={0.36:-2.709,0.40:-2.991,0.45:-3.319,0.5:-3.625,1.0:-6.152,2.0:-10.430,5.0:-22.590,10.0:-42.638}
H={0.36:-0.122,0.40:-0.166,0.45:-0.228,0.5:-0.299,1.0:-1.314,2.0:-4.144,5.0:-14.43}
for e,c3 in ((0.36,-0.347204),(0.40,-0.350687),(0.45,-0.353077),(0.5,-0.354147),(1.0,-0.349489),(2.0,-0.342261),(5.0,-0.337009),(10.0,-0.335180)):
    EH,R2,G,ex=cap_pieces(e,c3); dEH=EH+2; dR2=R2+(4/3)*(3*e+1); dI=dEH+dR2+G
    print(f"  eps={e:5.2f}: dEH={dEH:+.4f} dR2={dR2:+.4f} dGamma={G:+.4f}  =>  dI/a={dI:+.4f}   (J-1: {J1.get(e):+.3f}; position H: {H.get(e,float('nan')):+.3f})")
