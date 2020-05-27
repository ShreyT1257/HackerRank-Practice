import re
n = int(input())
st = []
for i in range(n):
    st.append(input())
    result = True
    try:
        reg = re.compile(st[i])
    except re.error:
        result = False
    print(result)

#--------------------------------------------------------
'''
import re
for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except:
        print("False")
'''
