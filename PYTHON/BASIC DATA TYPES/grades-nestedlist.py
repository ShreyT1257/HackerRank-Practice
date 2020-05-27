# Harry   Berry  Tina  Akriti  Harsh
# 37.21   37.21  37.2    41     39
'''
n=int(input())
arr=[[input(), float(input())] for _ in range(0,n)]
arr.sort(key=lambda x:(x[1],x[0]))
name=[i[0] for i in arr]
score=[i[1] for i in arr]
lowest=min(score)
while(score[0] == lowest):
    score.remove(score[0])
    name.remove(name[0])
for x in range(0,len(score)):
    if(score[x] == min(score)):
        print(name[x])
'''

marksheet = []
scorelist = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet = [[name, score]]
    scorelist += [score]

scorelist = list(dict.fromkeys(scorelist))
b = sorted(scorelist)[1]
for a,c in sorted(marksheet):
    if c == b:
        print(a)
