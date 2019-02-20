s=input()
n=int(input())
r=""
for c in s:
    k=ord(c)
    if (k>=65 and k<=90):
        k+=n
        if k>90:
            k=k-26
    elif (k>=97 and k<=122):
        k+=n
        if k>122:
            k=k-26 
    elif (k>=48 and k<=57):
        k+=n
        if k>57:
            k=k-10
    r=r+chr(k)
print(r)
