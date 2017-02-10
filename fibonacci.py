f = [0,1]
n = int(raw_input("Number: "))
for i in range(2,n):
    f.append(f[i-2]+f[i-1])
print f[n-1]
print f
