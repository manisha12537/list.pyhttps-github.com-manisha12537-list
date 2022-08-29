# i=1
# sum=0
# while i<=4:
#     j=1
#     while j<=i:
#         sum=sum+1
#         print(sum,end="")
#         j=j+1
#     print()
#     i=i+1


# n=int(input("enter a number"))
# if n%2==0:
#     i=1
#     while i<=n:
#         if n%2==0:
#             print(n)
#         i=i+1
# else:
#         a=n/2
#         c=int(a)
#         i=1
#         while i<=c:
#             if n%2!=0:
#                 print(n)
#             i=i+1





a={"developer":{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti","rohit"]}}
b={}
for i,j in a.items():
    for k in j:
        if(type(j[k])==list):
            b[i]=j[k]
print(b)


 