"""
n=int(input())
arr=list(map(int, input().split()))
z=max(arr)
while(max(arr) == z):
    arr.remove(max(arr))
print(max(arr))
"""



n = int(input())
arr = map(int, input().split())
new_list = []
for i in arr:
    if i not in new_list:
        new_list.append(i)
new_list.sort(reverse = True)
print(new_list[1])


