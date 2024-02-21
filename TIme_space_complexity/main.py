###### 0(1)
arr = [1, 2, 3, 4, 5]
print(f"{arr[1]}\n\n")

for i in range(1, 5):
    for j in range(1, i):
        print(f"{i * j}", end=",")
###### 0(n)
n_arr = [1, 2, 3, 4, 5]
for i in n_arr:
    if i == 6:
        print("bad array")
###### 0(n^2)
print(f"\n0(n^2)")
N = 5
for j in range(1, N):
    for x in range(1, N):
        print(j * x, end=",")
