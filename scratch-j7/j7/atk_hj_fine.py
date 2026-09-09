# ATTACK: is the 2.6e-3 discrepancy at the (4,12) recontracting cap (hjcheck row 2) a finite-difference artifact?
# Re-run the dc3 displacement with smaller steps, and add a third (mixed) displacement to over-determine (P,Q).
import numpy as np, sys
src=open('hjcheck.py').read().split("e=1.0\ncheck(")[0]
exec(src)
def check2(c3,tau1,e,label,h=1e-4,dcs=(1e-4,1e-5,1e-6,1e-7)):
    I0,a0,v0,w0,x0,R0=Iinv_data(c3,e,pathof(tau1))
    Qth=(e/4)*a0**2*R0; Pth=paf(a0,v0,w0,x0,e); pvE=pvf(a0,v0,w0,e)
    print(f"{label}: a1={a0:.5f} v1={v0:.5f} R1={R0:.5f} | Q_th={Qth:.6f} P_th={Pth:.6f} p_v^ESU={pvE:.6f}")
    # tau1 displacement
    Ip,ap,vp,_,_,_=Iinv_data(c3,e,pathof(tau1+h)); Im,am,vm,_,_,_=Iinv_data(c3,e,pathof(tau1-h))
    dI_t=(Ip-Im)/2; da_t=(ap-am)/2; dv_t=(vp-vm)/2
    print(f"   dtau1 (h={h:.0e}): dI={dI_t:.8e} pred={Pth*da_t+Qth*dv_t:.8e} rel={abs(dI_t-(Pth*da_t+Qth*dv_t))/abs(dI_t):.2e}")
    for dc in dcs:
        Ip,ap,vp,_,_,_=Iinv_data(c3+dc,e,pathof(tau1)); Im,am,vm,_,_,_=Iinv_data(c3-dc,e,pathof(tau1))
        dI=(Ip-Im)/2; da=(ap-am)/2; dv=(vp-vm)/2
        pred=Pth*da+Qth*dv
        M=np.array([[da_t,dv_t],[da,dv]]); b=np.array([dI_t,dI]); Pn,Qn=np.linalg.solve(M,b)
        print(f"   dc3={dc:.0e}: da={da:.3e} dv={dv:.3e} dI={dI:.8e} pred={pred:.8e} rel={abs(dI-pred)/abs(dI):.2e} | solved (P,Q)=({Pn:.6f},{Qn:.6f})  dP={abs(Pn-Pth):.1e} dQ={abs(Qn-Qth):.1e}")
    # third, mixed displacement: dc3 and dtau1 together, at the finest step
    dc=1e-6
    Ip,ap,vp,_,_,_=Iinv_data(c3+dc,e,pathof(tau1+h)); Im,am,vm,_,_,_=Iinv_data(c3-dc,e,pathof(tau1-h))
    dI=(Ip-Im)/2; da=(ap-am)/2; dv=(vp-vm)/2; pred=Pth*da+Qth*dv
    print(f"   mixed (dc3=1e-6,h=1e-4): dI={dI:.8e} pred={pred:.8e} rel={abs(dI-pred)/abs(dI):.2e}")
e=1.0
check2(-0.004475,5.70887,e,"eps=1 recontracting cap at (4,12)")
check2(-0.004475,3.0,e,"eps=1 recontracting cap, expanding side tau=3")
e=0.3
check2(-0.008064,3.29029,e,"eps=0.3 recontracting cap at (4,12)")
