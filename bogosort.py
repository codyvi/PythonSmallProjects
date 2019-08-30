from random import randint,shuffle

def create_array(size=10, max=50):
    return[randint(0,max) for _ in range(size)]

def is_sorted(a):
    for i in range(1,len(a)):
        if a[i]<a[i-1]: return False
    return True

def bogo_sort(a):
    ct=0
    while not is_sorted(a):
        shuffle(a)
        ct+=1
    return ct,a

a=create_array(7,7)
print ("Unsorted:",a)
ct,s=bogo_sort(a)
print ("Sorted:",s)
print ("Number of iterations: %d"%ct)

#Printing how much it would take to sort arrays from greater size
#times ={}
#cutoff = 20
#from time import time 
#for i in range(2,100):
#    a=create_array(i,i)
#    t0=time()
#    ct,s=bogo_sort(a)
#    dur=time()-t0
#    times[i]=dur
#    if dur >=cutoff: break

#print ("\tBogosort Duration (s)")
#print (30*"_")
#for n,dur in times.items():
#    print("%d\t%0.5f"%(n,dur))