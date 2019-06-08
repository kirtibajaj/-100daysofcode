#s->String
s=input()
#q->queries
first=[]
q=int(input())
for i in range(q):
  direc,mag=input().split()
  if direc=='L' or direc=='l':
    s=s[int(mag):]+s[:int(mag)]
  elif direc=='R' or direc=='r':
    s=s[len(s)-int(mag):]+s[:len(s)-int(mag)]
  first.append(s[0])
x=[]
for i in range(len(s)-len(first)+1):
  x.append([har for har in s[i:i+len(first)]])
  x[i].sort()
  first.sort()
  if x[i]==first:
    print("YES")
    break
else:
  print("NO")

