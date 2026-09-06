# Feldbrugge-Lehners-Turok Einstein-Lambda check: S(N) = 2 pi^2 [N^3 Lambda^2/36 + N(3 - Lambda q1/2) - 3 q1^2/(4N)], saddles N = (3/Lambda)(+-i +- sqrt(Lambda q1/3 - 1)).
import numpy as np
Lam=3.0; q1=9.0; y=np.sqrt(Lam*q1/3-1)
S=lambda N: 2*np.pi**2*(N**3*Lam**2/36+N*(3-Lam*q1/2)-3*q1**2/(4*N))
for s1 in (1,-1):
    for s2 in (1,-1):
        N=(3/Lam)*(s1*1j+s2*y); iS=1j*S(N)
        print(f"N_s = {N:.4f}: Re(iS) = {iS.real:+.4f} = {iS.real/np.pi**2:+.3f} pi^2   (HH: +12pi^2/Lambda = {12*np.pi**2/Lam:.3f}; tunneling: -{12*np.pi**2/Lam:.3f})")
