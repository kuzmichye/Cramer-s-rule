import numpy as np
def calc(A,B,n):
    res = np.linalg.det(A)
    if res == 0:
        return "No custom solutions"
    else:
        s = []
        for i in range(n):
            Ai = np.copy(A)
            Ai[:,i]= B.flatten()
            s.append(np.linalg.det(Ai)/res)
        return np.array(s)

n = int(input("Enter the number of equations in your system of linear equations: "))
A = np.array([list(map(int,input("Enter the matrix A (your coefficients):").split())) for _ in range(n)],dtype = 'int64')
B = np.array([[int(input("Enter the matrix B:"))] for _ in range(n)],dtype = 'int64')

if A.shape[0] == A.shape[1]:
    res = calc(A,B,n)
    print(f"The results are:{res}")
else:
    print("The matrxi is not square")


