import sympy as sp
tau,chi,th,ph=sp.symbols('tau chi theta phi')
a=sp.Function('a')(tau)
x=[tau,chi,th,ph]
g=sp.diag(1,a**2,a**2*sp.sin(chi)**2,a**2*sp.sin(chi)**2*sp.sin(th)**2)
ginv=g.inv()
n=4
Gam=[[[sp.simplify(sum(ginv[i,l]*(sp.diff(g[l,j],x[k])+sp.diff(g[l,k],x[j])-sp.diff(g[j,k],x[l])) for l in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]
def Riem(i,j,k,l):  # R^i_{jkl}
    e=sp.diff(Gam[i][j][l],x[k])-sp.diff(Gam[i][j][k],x[l])
    e+=sum(Gam[i][k][m]*Gam[m][j][l]-Gam[i][l][m]*Gam[m][j][k] for m in range(n))
    return sp.simplify(e)
Ric=sp.Matrix(n,n,lambda j,l: sp.simplify(sum(Riem(i,j,i,l) for i in range(n))))
R=sp.simplify(sum(ginv[j,l]*Ric[j,l] for j in range(n) for l in range(n)))
Ric2=sp.simplify(sum(Ric[j,l]*Ric[m,p]*ginv[j,m]*ginv[l,p] for j in range(n) for l in range(n) for m in range(n) for p in range(n)))
# Riemann squared
Rdown={}
for i in range(n):
  for j in range(n):
    for k in range(n):
      for l in range(n):
        Rdown[(i,j,k,l)]=sp.simplify(sum(g[i,m]*Riem(m,j,k,l) for m in range(n)))
Riem2=0
for i in range(n):
  for j in range(n):
    for k in range(n):
      for l in range(n):
        Riem2+=Rdown[(i,j,k,l)]**2*ginv[i,i]*ginv[j,j]*ginv[k,k]*ginv[l,l]
Riem2=sp.simplify(Riem2)
E4=sp.simplify(Riem2-4*Ric2+R**2)
C2=sp.simplify(Riem2-2*Ric2+R**2/3)
boxR=sp.simplify(sp.diff(a**3*sp.diff(R,tau),tau)/a**3)
print("R      =",sp.factor(R))
print("Ric^2  =",sp.factor(Ric2))
print("E4     =",sp.factor(E4))
print("Weyl^2 =",C2)
print("boxR   =",sp.factor(boxR))
# checks on the round S^4: a = sin(H tau)/H
H=sp.symbols('H',positive=True)
sub={a:sp.sin(H*tau)/H}
def ev(e): return sp.simplify(e.subs(a,sp.sin(H*tau)/H).doit())
print("S4 check: R=",ev(R)," E4=",ev(E4)," boxR=",ev(boxR))
import pickle; pickle.dump({'R':R,'E4':E4,'boxR':boxR,'Ric2':Ric2},open('curv.pkl','wb'))
