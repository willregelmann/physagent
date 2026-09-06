# Steelman analysis of the complex saddle set at the dS-history data (a1=3, K1=-i sqrt8), eps=1, J-1 scheme.
# (1) Sheet table: h = Re(iS) = -Re I on the a'(0)=+1 sheet, +Re I on the a'(0)=-1 sheet; FLT's bound says a relevant
#     saddle of the real-lapse contour has h <= 0, so at most one sheet per geometric saddle is a candidate and its
#     weight is e^{-|Re I|}.  Rank candidates by |Re I|.
# (2) Classicality (HHH): continue each low-|Re I| saddle along the dS data a1 -> 3.25, 3.5, 4, 5 (K1 = -i sqrt(a1^2-1)),
#     compare d Re I / d a1 with d Im I / d a1.  Also Im R(T) at the cut (momentum reality).
# (3) Path diagnostics: max|a| along the straight path, winding of a about 0, conformal length eta(T) = int dtau/a
#     (Re part sets the C=+8 vs C=-8 ESU-scheme shift 2a Re[eta_cap - eta_sphere]).
# (4) eps-continuation of the same saddles to eps = 0.5 and 2 at fixed data (3, -i sqrt8).
import numpy as np, sys
exec(open('complexcaps.py').read().split("e=1.0; a1=3.0")[0])
from scipy.integrate import solve_ivp
def shoot3(c3,T,e,s0=1e-3):
    C5,C7=c5f(c3,e),c7f(c3,e); t0=s0*T
    y0=np.array([t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4, 0.0, 0.0],dtype=complex)
    ss=np.linspace(1e-6,1,200)*t0; aa_=ss+c3*ss**3+C5*ss**5+C7*ss**7; a1_=1+3*c3*ss**2+5*C5*ss**4+7*C7*ss**6; a2_=6*c3*ss+20*C5*ss**3+42*C7*ss**5
    y0[4]=2*np.pi**2*np.trapz(Lreg(aa_,a1_,a2_,e)/aa_,ss)
    y0[5]=np.log(t0)      # eta ~ ln tau near the pole (universal divergence dropped: eta measured from tau=1 scale)
    def rhs(s,y):
        A,B,C,D,I,et=y
        return T*np.array([B,C,D,FE(A,B,C,D,e),2*np.pi**2*Lreg(A,B,C,e)/A,1/A],dtype=complex)
    small=lambda s,y: abs(y[0])-0.02; small.terminal=True; small.direction=-1
    big=lambda s,y: abs(y[0])-40.0; big.terminal=True
    sol=solve_ivp(rhs,(s0,1.0),y0,method='DOP853',rtol=1e-10,atol=1e-13,events=[small,big],dense_output=True)
    if sol.status!=0 or len(sol.t_events[0]) or len(sol.t_events[1]): return None,None
    return sol.y[:,-1],sol
def newton2(c3,T,e,a1,K1,it=60):
    z=np.array([c3,T],dtype=complex); y=None
    for k in range(it):
        y,_=shoot3(z[0],z[1],e)
        if y is None: return None
        F=np.array([y[0]-a1,y[1]-K1])
        if np.max(np.abs(F))<1e-11: return z,y
        h=1e-6; J=np.zeros((2,2),dtype=complex)
        for j in range(2):
            zp=z.copy(); zp[j]+=h; yp,_=shoot3(zp[0],zp[1],e)
            if yp is None: return None
            J[:,j]=(np.array([yp[0]-a1,yp[1]-K1])-F)/h
        try: dz=np.linalg.solve(J,F)
        except np.linalg.LinAlgError: return None
        m=np.max(np.abs(dz))
        if m>0.3: dz=dz*0.3/m
        z=z-dz
    return None
e=1.0; a1=3.0; K1=-1j*np.sqrt(8.0)
# the attack's 18 saddles (dS_search.out, dS_search2.out) plus the sphere
cands=[("sphere",-1/6,np.pi/2+1.762747j),
("A",-0.061078-0.074741j,0.958365-7.517934j),("B",-0.078012-0.080863j,3.646649-7.552073j),("C",0.011760-0.000057j,-6.007494-4.176755j),
("D",0.006200+0.006758j,4.931966+3.047997j),("E",-0.160805+0.117255j,-4.089197-8.820504j),("F",-0.024640+0.090852j,2.969438-8.244251j),
("G",-0.073135-0.070948j,2.275652-14.632213j),("H",-0.074380-0.093827j,0.233795+9.329840j),("I",-0.103854-0.087970j,-10.389552+3.304918j),
("J",-0.067485+0.073246j,4.536903+10.252188j),("K",-0.067834+0.076298j,-6.494782-10.376287j),("L",-0.041756-0.168680j,0.644368+8.539119j),
("M",-0.099604-0.091109j,11.524847-8.253794j),("N",-0.071493-0.074147j,3.927697-16.782805j),("O",-0.091483+0.095266j,-7.733206-8.265503j),
("P",0.038850+0.108716j,-1.880350+6.600720j),("Q",0.008517-0.001237j,9.342835+6.325672j),("S",-0.024619+0.074912j,-6.323142+10.106159j)]
print("=== (1) sheet table at (a1=3, K1=-i sqrt8), eps=1, J-1 scheme.  h(+sheet) = -Re I, h(-sheet) = +Re I; candidate sheet = the one with h<=0; weight e^{-|Re I| a}")
print("name  c3                      T                      Re I/a    Im I/a    candidate sheet   |Re I|   R(T)                  Im R/|R|   max|a|  wind  Re eta(T)")
rows={}
for name,c3,T in cands:
    r=newton2(c3,T,e,a1,K1)
    if r is None: print(name,"no convergence"); continue
    z,y=r; _,sol=shoot3(z[0],z[1],e)
    ss=np.linspace(1e-3,1,4000); Y=sol.sol(ss); A=Y[0]
    wind=np.sum(np.diff(np.unwrap(np.angle(A))))/(2*np.pi)
    ReI=y[4].real; Rv=Rf(y[0],y[1],y[2])
    sheet="+1 (HH-type, e^{-I})" if ReI>0 else "-1 (flipped, e^{+I})"
    rows[name]=(z[0],z[1],y[4],Rv)
    print(f"{name:6s} {z[0]:+.6f}   {z[1]:+.6f}   {ReI:+8.3f}  {y[4].imag:+8.3f}   {sheet:22s} {abs(ReI):7.3f}  {Rv:+.3f}   {Rv.imag/abs(Rv):+.3f}   {np.abs(A).max():6.2f}  {wind:+.2f}  {y[5].real-np.log(1e-3*abs(z[1])):+.3f}")
print("\nranking by |Re I| (least-suppressed candidate first):")
for name,(c3,T,I,Rv) in sorted(rows.items(),key=lambda kv: abs(kv[1][2].real)): print(f"  {name:6s} |Re I|/a = {abs(I.real):7.3f}   Re I = {I.real:+.3f}")
print("\n=== (2) classicality along the dS data: d(Re I)/da1 vs d(Im I)/da1 (K1 = -i sqrt(a1^2-1)); Im R(T)")
for name in ("sphere","E","D","B","J","N","P","A"):
    if name not in rows: continue
    c3,T,I,Rv=rows[name]; z=np.array([c3,T]); out=[]
    for A1 in (3.0,3.1,3.25,3.5,4.0,5.0):
        r=newton2(z[0],z[1],e,A1,-1j*np.sqrt(A1**2-1))
        if r is None: out.append((A1,None)); break
        z,y=r; out.append((A1,y[4],Rf(y[0],y[1],y[2]),z[0],z[1]))
    print(f"{name}:")
    prev=None
    for o in out:
        if o[1] is None: print(f"   a1={o[0]}: lost"); continue
        A1,I,Rv,c3v,Tv=o
        if prev is not None:
            dRe=(I.real-prev[1].real)/(A1-prev[0]); dIm=(I.imag-prev[1].imag)/(A1-prev[0])
            print(f"   a1={A1:4.2f}: I/a={I:+.4f}  R(T)={Rv:+.3f}  c3={c3v:+.5f} T={Tv:+.4f}   dReI/da1={dRe:+8.3f}  dImI/da1={dIm:+8.3f}  ratio={abs(dRe)/max(abs(dIm),1e-12):.3f}")
        else: print(f"   a1={A1:4.2f}: I/a={I:+.4f}  R(T)={Rv:+.3f}  c3={c3v:+.5f} T={Tv:+.4f}")
        prev=(A1,I)
print("\n=== (4) eps-continuation at fixed data (3, -i sqrt8): Re I/a of the same saddles at eps = 0.5, 0.75, 1, 1.5, 2")
for name in ("sphere","E","D","B","A","F","Q"):
    if name not in rows: continue
    c3,T,I,Rv=rows[name]; line=f"{name:6s}"
    for path in ((1.0,0.75,0.5),(1.0,1.5,2.0)):
        z=np.array([c3,T])
        for ee in path:
            r=newton2(z[0],z[1],ee,a1,K1)
            if r is None: line+=f"  eps={ee}: lost"; break
            z,y=r
            if ee!=1.0: line+=f"  eps={ee}: ReI={y[4].real:+.3f} (c3={z[0]:+.4f},T={z[1]:+.3f})"
    print(line)
print("DONE")
