from numpy import *
from scipy.sparse import *
from scipy.sparse.linalg import spsolve
 
def poissonSolve(ncut):
  n = 2*ncut + 1; m = n*n; h = 2/(n-1) 
  
  A = dok_matrix(eye(m)); B = zeros(m)
  for i in range(1,n-1):
    for j in range(1,n-1):
      if (j<ncut or i>ncut):
        index = i + j*n
        A[index,index] = 4
        A[index,index-1],A[index,index+1],A[index,index+n],A[index,index-n] = -1,-1,-1,-1
        B[index] = 1
      
  return spsolve(A/(h*h),B).reshape(n,n)
 