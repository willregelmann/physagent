# Off-shell check: action of a smoothed cone a(tau) = v*tau smoothed at scale delta near the pole, in the ESU-frame Lagrangian (C=8),
# local part only (EH+R2) plus the Riegert ESU density; expect I ~ coeff(v,eps) * ln(1/delta) with coeff -> -3 eps (v-1)^2 near v=1.
import numpy as np
from scipy.integrate import quad
def L(a,v,w,e):
    C=8; kap=-(3*e+1)/(288*np.pi**2)
    return 2*np.pi**2*(-(6/(16*np.pi**2))*a**2*(1+v**2)+(1/(16*np.pi**2))*(2*a**2*w**2+8*v**2+C)+36*kap*(1-a*w-v**2)**2)/a
def cone(vv,d,e,tau1=1.0):
    # a(tau)=sqrt(tau^2 + d^2 (vv^2-1)... ) : use a = vv*sqrt(tau^2+d^2) - (vv-1)*d  -> a'(0)=0? no. Use a = sqrt((vv tau)^2 + d^2) - d + tau*0 ... need a(0)=0,a'(0)=1 and a~vv*tau for tau>>d:
    # a(tau) = tau + (vv-1)*(sqrt(tau^2+d^2)-d)  -> a(0)=0, a'(0)=1, a''(0)=(vv-1)/d, a -> vv*tau for tau>>d.
    f=lambda t: t+(vv-1)*(np.sqrt(t*t+d*d)-d)
    fp=lambda t: 1+(vv-1)*t/np.sqrt(t*t+d*d)
    fpp=lambda t: (vv-1)*d*d/(t*t+d*d)**1.5
    val,err=quad(lambda t: L(f(t),fp(t),fpp(t),e),1e-9,tau1,limit=400,points=[d,10*d])
    return val
for e in (0.3,1.0):
    for vv in (0.8,0.9,1.1,1.2,2.0):
        Is=[cone(vv,d,e) for d in (1e-2,1e-3,1e-4)]
        slope=(Is[2]-Is[1])/np.log(10)   # dI/d ln(1/delta)
        pred=-(vv-1)**2*(3*e*vv**2+6*e*vv+3*e+vv**2+2*vv-3)/(4*vv)
        print(f"eps={e} v={vv}: I(d=1e-2,1e-3,1e-4)={Is[0]:+.4f},{Is[1]:+.4f},{Is[2]:+.4f}  dI/dln(1/d)={slope:+.4f}  sharp-cone log coeff (sympy)={pred:+.4f}")
