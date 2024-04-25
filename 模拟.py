import random
import matplotlib.pyplot as plt

def mod_mup(q):
    alist = []

    blist = []
    for i in range(q):
        alist.append(i)
        blist.append(0)

    
    
    
    for a in range(q):
        for b in range(q):
            ab = (a * b) % q
            #print(ab)
            
            blist[ab] = blist[ab] + 1/(q**2)

    sum_blist = 0
    for i in range(q):

        sum_blist = sum_blist + blist[i]
    #print(sum_blist)
    
    for i in range(q):
        blist[i] = blist[i]/sum_blist
    return alist, blist


def mod_add(q, llist):
    alist = []

    blist = []
    for i in range(q):
        alist.append(i)
        blist.append(0)

    
    
    
    for a in range(q):
        for b in range(q):
            ab = (a + b) % q
            #print(ab)
            blist[ab] = blist[ab] + llist[b] * llist[a]
            #print(a,b,ab,llist[b], llist[a],blist[ab])

    sum_blist = 0
    for i in range(q):

        sum_blist = sum_blist + blist[i]
    #print(sum_blist)
    
    for i in range(q):
        blist[i] = blist[i]/sum_blist
    return alist, blist



q = 1000
n = 3
print('实际安全参数n:',2**n)
print('模数q:',q)
#llist = [0.75,0.25]
##alist, blist = mod_mup(q)
alist, blist = mod_mup(q)
for i in range(n):
       
   alist, blist = mod_add(q,blist)


for i in range(q):
    blist[i] = abs(blist[i] - 1/q)

#print(alist, blist)
print(max(blist))


plt.plot(alist, blist, marker='o')
plt.title('List of Numbers')
plt.xlabel('Index')
plt.ylabel('Value')

# 显示图表
plt.show()