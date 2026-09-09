# J-7a: Hamilton-Jacobi check of steelman-H's frame-invariant action I_inv (theta_1 = pi/2 gauge, HHJ boundary term).
# Claim: on the 2-parameter family of regular caps, dI_inv = P da1 + Q dv1 with Q = (eps/4) a1^2 R1  (R^2-type GHY momentum),
# i.e. the anomaly part (KS bulk + HHJ -v^3/3) contributes nothing to the v-momentum at theta_1 = pi/2, and
# P = p_a^{ESU} = (dL/dv - d p_v/dtau)_{ESU} (the ESU-frame Ostrogradsky a-momentum, which has F_a = 0 for F = -v/2 + v^3/6).
import numpy as np, sys
sys.path.insert(0,'.')
src=open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0]
exec(src)
import sympy as sp
# ESU-frame Lagrangian per a, per dtau (C=8), Ostrogradsky momenta
A0,A1,A2,A3,ep=sp.symbols('A0 A1 A2 A3 epsilon')
C=8; kap=-(3*ep+1)/(288*sp.pi**2)
L=2*sp.pi**2*(-(sp.Integer(6)/(16*sp.pi**2))*A0**2*(1+A1**2)+(1/(16*sp.pi**2))*(2*A0**2*A2**2+8*A1**2+C)+36*kap*(1-A0*A2-A1**2)**2)/A0
pv=sp.diff(L,A2); dpv=sp.diff(pv,A0)*A1+sp.diff(pv,A1)*A2+sp.diff(pv,A2)*A3
pa=sp.simplify(sp.diff(L,A1)-dpv)
paf=sp.lambdify((A0,A1,A2,A3,ep),pa,'numpy'); pvf=sp.lambdify((A0,A1,A2,ep),pv,'numpy')
print("p_a^ESU =",pa)
def Iinv_data(c3,e,path):
    C=sym_C(c3,e,path); y=run_path(c3,e,path,C)
    A,A1_,A2_,A3_=y[0],y[1],y[2],y[3]
    Ilocp=y[5]+y[6]*3*e/(3*e+1); Ii=Ilocp+y[9]-(1/3)*A1_**3
    return Ii,A,A1_,A2_,A3_,Rf(A,A1_,A2_)
def check(c3,tau1,e,label,h=1e-4,dc=1e-4):
    # base
    I0,a0,v0,w0,x0,R0=Iinv_data(c3,e,pathof(tau1))
    Qth=(e/4)*a0**2*R0; Pth=paf(a0,v0,w0,x0,e); pvE=pvf(a0,v0,w0,e)
    # two independent displacements on the family: (i) tau1 -> tau1+h at fixed c3 ; (ii) c3 -> c3+dc at fixed tau1
    rows=[]
    for (dc3,dt,nm) in ((0,h,'dtau1'),(dc,0,'dc3')):
        Ip,ap,vp,_,_,_=Iinv_data(c3+dc3,e,pathof(tau1+dt)); Im,am,vm,_,_,_=Iinv_data(c3-dc3,e,pathof(tau1-dt))
        dI=(Ip-Im)/2; da=(ap-am)/2; dv=(vp-vm)/2
        pred=Pth*da+Qth*dv
        rows.append((nm,dI,pred,da,dv))
    print(f"{label}: a1={a0:.4f} v1={v0:.4f} R1={R0:.4f} | Q_theory=(eps/4)a^2R={Qth:.5f}  p_v^ESU={pvE:.5f}  P=p_a^ESU={Pth:.5f}")
    for nm,dI,pred,da,dv in rows:
        print(f"    {nm}: dI_inv={dI:.6e}  P da+Q dv={pred:.6e}  (da={da:.3e}, dv={dv:.3e})  rel.err={abs(dI-pred)/max(abs(dI),1e-300):.2e}")
    # solve for the actual (P,Q) from the two displacements and compare
    M=np.array([[rows[0][3],rows[0][4]],[rows[1][3],rows[1][4]]]); b=np.array([rows[0][1],rows[1][1]])
    Pn,Qn=np.linalg.solve(M,b)
    print(f"    numerical (P,Q)=({Pn:.5f},{Qn:.5f})  vs theory ({Pth:.5f},{Qth:.5f})  vs ESU p_v={pvE:.5f}")
def pathof(t1):
    t1=complex(t1)
    return [min(t1.real,1.185) if t1.real>0.05 else 0.05, t1] if abs(t1.imag)>1e-12 else [t1]
e=1.0
check(-0.004475,3.0,e,"eps=1 real recontracting cap (c3=-0.004475) cut at tau=3.0 (expanding side)")
check(-0.004475,5.70887,e,"eps=1 real recontracting cap at (4,12) cut (contracting side)")
check(-0.349489,1.6,e,"eps=1 double bubble cut at tau=1.6 (K<0)")
check(-1/6,1.2,e,"eps=1 round sphere cut at tau=1.2")
check(-1/6,np.pi/2+1j*np.arccosh(2.0),e,"eps=1 sphere dS continuation at (4,12) (complex cut)")
check(-0.885788-0.478724j,2.73251+1.13928j,e,"eps=1 complex pair at (4,12)")
e=0.3
check(-0.008064,3.29029,e,"eps=0.3 real recontracting cap at (4,12)")
check(-0.10,2.0,e,"eps=0.3 generic real cap c3=-0.10 cut at tau=2.0")
