import numpy as np, pickle
from scipy.integrate import solve_ivp, trapezoid, cumulative_trapezoid, quad
src=open('caps.py').read().split("res={}")[0]; exec(src)
# --- Riegert functional with the unit round S^4 as reference:
# Gamma[s] = (a/16pi^2) * Int sqrt(ghat) [ 24 s + 2 s (box^2 - 2 box) s ],  ghat = sech^2(eta)(d eta^2 + dOmega_3^2)
# For f(eta): box f = cosh^4(eta) d/deta( sech^2(eta) f' ),  sqrt(ghat) d^4x -> 2 pi^2 sech^4(eta) d eta
def box(f,eta):
    fp=np.gradient(f,eta); return np.cosh(eta)**4*np.gradient(np.cosh(eta)**-2*fp,eta)
def Gamma_over_a(s,eta):
    b=box(s,eta); b2=box(b,eta)
    integrand=np.cosh(eta)**-4*(24*s+2*s*(b2-2*b))
    return (1/(16*np.pi**2))*2*np.pi**2*trapezoid(integrand,eta)
# check 1: radius-r sphere -> 4 ln r
eta=np.linspace(-12,12,240001)
for r in (0.5,2.0):
    s=np.full_like(eta,np.log(r)); print(f"radius {r}: Gamma/a = {Gamma_over_a(s,eta):.6f}  expected 4 ln r = {4*np.log(r):.6f}")
# check 2: Moebius boost of S^4 (a conformal isometry): a(eta) = sech(eta - eta0) -> sigma = ln(cosh(eta)/cosh(eta-eta0)); Gamma must vanish
for eta0 in (0.5,1.5):
    s=np.log(np.cosh(eta))-np.log(np.cosh(eta-eta0)); print(f"Moebius shift {eta0}: Gamma/a = {Gamma_over_a(s,eta):.2e} (expected 0)")
# --- now the double bubble: build a(eta) from the tau solution, eta=0 at the neck
def pieces(e,c3):
    ex,cl,sol=run(c3,e,dense=True); tclose=sol.t_events[1][0]
    ts=np.linspace(sol.t[0],tclose,400001); Y=sol.sol(ts); A,A1,A2=Y[0],Y[1],Y[2]
    # local pieces in tau (per a_anom, times 2pi^2): EH and R^2 as in caps.py; anomaly LOCAL part 2 sigma''^2 kept separately
    sp1=A1; sp2=A*A2
    EH=2*np.pi**2*trapezoid((-(6/(16*np.pi**2))*A**2*(1+sp1**2))/A,ts)
    R2=2*np.pi**2*trapezoid((36*(-(3*e+1)/(288*np.pi**2))*(1-sp2-sp1**2)**2)/A,ts)
    # conformal time with eta=0 at the neck (second extremum) ; d eta = d tau / a
    tneck=ex[1][0] if len(ex)>=3 else ex[0][0]
    etas=cumulative_trapezoid(1/A,ts,initial=0); etas-=np.interp(tneck,ts,etas)
    # resample on a uniform eta grid within the resolved range
    m=(np.abs(etas)<11); eg=np.linspace(etas[m].min(),etas[m].max(),200001); Ag=np.interp(eg,etas,A)
    s=np.log(Ag*np.cosh(eg))
    G=Gamma_over_a(s,eg)
    return EH,R2,G,(ex[0][1],ex[1][1] if len(ex)>=3 else None)
# sphere pieces (c3=-1/6): EH=-2? per a: -(2 pi/G)/a = -2  ; R2 = -(4/3)(3e+1); Gamma=0 (reference)
for e,c3 in ((0.5,-0.354147),(1.0,-0.349489),(2.0,-0.342261),(5.0,-0.337009)):
    EHs,R2s,Gs,_=pieces(e,-1/6)
    EHd,R2d,Gd,(ap,an)=pieces(e,c3)
    dI=(EHd-EHs)+(R2d-R2s)+(Gd-Gs)
    print(f"eps={e}: sphere EH={EHs:+.4f} R2={R2s:+.4f} Gamma={Gs:+.2e} | DB EH={EHd:+.4f} R2={R2d:+.4f} Gamma={Gd:+.4f} | dI/a = {dI:+.4f}  (J-1 had {'-3.62' if e==0.5 else '-6.15' if e==1 else '-10.43' if e==2 else '-22.59'})")
