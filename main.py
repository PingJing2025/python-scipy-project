import scipy
import numpy as np

A=np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = scipy.linalg.eig(A)

print("eigenvalues:",eigenvalues)
print("eigenvalues:\n",eigenvectors)
