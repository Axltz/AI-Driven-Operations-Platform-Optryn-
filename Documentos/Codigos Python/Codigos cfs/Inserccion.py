A = [2, 6, 3, 8, 4, 9, 14]

for i in range( len(A)):
     posicion = A[i]
     j = i - 1
     while j >= 0 and posicion < A[j]:
       A[j + 1] = A[j]
       j -= 1
       A[j + 1] = posicion      
print(A)