N = int(input())
List1 = []
for i in range(N):
    command = input().split()
    if command[0] == "insert":
        List1.insert(int(command[1]),int(command[2]))
    if command[0] == "append":
        List1.append(int(command[1]))
    if command[0] == "remove":
        List1.remove(int(command[1]))
    if command[0] == "sort":
        List1.sort()
    if command[0] == "print":
        print(List1)
    if command[0] == "reverse":
        List1.reverse()
    if command[0] == "pop":
        List1.pop()

