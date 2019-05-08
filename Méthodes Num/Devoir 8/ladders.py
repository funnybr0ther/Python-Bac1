from scipy.linalg import norm,solve

def laddersIterate(geometry,xy):
  a,b,c = geometry
  x,y = list(xy)
  matrix =     [[(c**2+y**2)**(1/2),x*y/((c**2+y**2)**(1/2))+(c**2+y**2)**(1/2)+(y**2)/(c**2+y**2)**(1/2)-a], 
  [x*y/((c**2+x**2)**(1/2))+(c**2+x**2)**(1/2)+(x**2)/(c**2+x**2)**(1/2)-b,(c**2+x**2)**(1/2)]]
  right = [x*(c**2+y**2)**(1/2)+y*(c**2+y**2)**(1/2)-a*y,x*(c**2+x**2)**(1/2)+y*(c**2+x**2)**(1/2)-x*b]
  delta = - solve(matrix,right)
  return xy + delta
def laddersSolve(geometry,tol,nmax):
  try:
    a,b,c = geometry
    n = 0; delta = tol+1
    x = ([(a-c)/2, (b-c)/2])
    while (norm(delta) > tol and n < nmax):
      xold = x
      x = laddersIterate(geometry,xold)
      delta = x-xold; n = n+1
  except:
    return [-1,-1]
  if delta[0]>=tol or delta[1]>= tol:
    return [-1,-1]
  return x
  