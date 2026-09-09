# J-7a: fixed-(a,v) saddles at (a1,v1)=(3,-i sqrt8), eps=1 (steelman T's 18-saddle census, J-1 scheme) re-evaluated with the
# frame-invariant (a,v)-action I_inv along the same straight pole->T path.  Plus the complex pair at (4,12) for eps=0.7,1.0.
import numpy as np, sys
exec(open('../j6/steelmanH/invariant.py').read().split("e=1.0; c3db=")[0])
sad={'sphere':(-0.166667-0.000000j,1.570796+1.762747j),'A':(-0.061078-0.074741j,0.958365-7.517934j),'B':(-0.078012-0.080863j,3.646649-7.552073j),
'C':(0.011760-0.000057j,-6.007494-4.176755j),'D':(0.006200+0.006758j,4.931966+3.047997j),'E':(-0.160805+0.117255j,-4.089197-8.820504j),
'F':(-0.024640+0.090852j,2.969438-8.244251j),'G':(-0.073135-0.070948j,2.275652-14.632213j),'H':(-0.074380-0.093827j,0.233795+9.329840j),
'I':(-0.103854-0.087970j,-10.389552+3.304918j),'J':(-0.067485+0.073246j,4.536903+10.252188j),'K':(-0.067834+0.076298j,-6.494782-10.376287j),
'L':(-0.041756-0.168680j,0.644368+8.539119j),'M':(-0.099604-0.091109j,11.524847-8.253794j),'N':(-0.071493-0.074147j,3.927697-16.782805j),
'O':(-0.091483+0.095266j,-7.733206-8.265503j),'P':(0.038850+0.108716j,-1.880350+6.600720j),'S':(-0.024619+0.074912j,-6.323142+10.106159j)}
e=1.0
print("=== (a1,v1)=(3,-i sqrt8), eps=1: straight path 0->T; I_inv = frame-invariant (a,v)-action ===")
out=[]
for nm,(c3,T) in sad.items():
    # re-polish the saddle with the straight path (a(T)=3, a'(T)=-i sqrt8) via Newton in (c3,T)
    def F(x):
        y=run_path(x[0],e,[x[1]],1.0); return np.array([y[0]-3.0,y[1]+1j*np.sqrt(8)]),y
    x=np.array([c3,T],dtype=complex)
    for it in range(30):
        f,y=F(x)
        if np.linalg.norm(f)<1e-10: break
        h=1e-7; J=np.zeros((2,2),complex)
        for k in range(2):
            xp=x.copy(); xp[k]+=h; fp,_=F(xp); J[:,k]=(fp-f)/h
        try: dx=np.linalg.solve(J,-f)
        except np.linalg.LinAlgError: break
        if np.linalg.norm(dx)>0.5: dx*=0.5/np.linalg.norm(dx)
        x=x+dx
    f,y=F(x)
    try:
        C=sym_C(x[0],e,[x[1]]); yy=run_path(x[0],e,[x[1]],C)
        Iinv=yy[5]+yy[6]*3*e/(3*e+1)+yy[9]-(1/3)*yy[1]**3; ok=abs(yy[4]-np.pi/2)<1e-6
    except Exception as ex: Iinv=np.nan; ok=False
    Iloc=y[5]+y[6]; R=Rf(y[0],y[1],y[2])
    print(f"{nm:7s} c3={x[0]:.6f} T={x[1]:.6f} resid={np.linalg.norm(f):.1e} R={R:.4f} | I_loc(bulk EH+R2)={Iloc:.4f} | I_inv={Iinv:.4f} Re={Iinv.real:+8.4f} gauge_ok={ok}",flush=True)
    out.append((nm,Iinv.real))
print("ranking by Re I_inv (HH sign e^{-I}: lowest first):")
for nm,r in sorted(out,key=lambda t:t[1]): print(f"   {nm:7s} Re I_inv={r:+.4f}")
# (complex-pair continuation moved to av_fix.py)
