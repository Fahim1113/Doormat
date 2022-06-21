A = input().split()
N = int(A[0])
M = int(A[1])

if M == N*3:
  for i in range(1, int((N-1)/2)+1):
    print('---'*int((N-(2*i-1))/2) + '.|.'*(2*i-1)+'---'*int((N-(2*i-1))/2))
  print('-'*int((M-7)/2)+'WELCOME'+'-'*int((M-7)/2))
  for j in range(1, int((N-1)/2)+1):
    print('---'*j + '.|.'*(N-2*j) + '---'*j)

else:
  print('M must be 3 times N')