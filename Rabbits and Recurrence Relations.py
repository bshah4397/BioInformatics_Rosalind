import time

def Fibonaaci_Rabits(n,k):
    if n==1: return 1
    if n==2: return k
    oneGen = Fibonaaci_Rabits(n-1,k)
    secGen = Fibonaaci_Rabits(n-2,k)
    if n<=4: return oneGen+secGen
    return (oneGen + secGen*k)

def Rabbits(n,k):
    rabbits = [1,1]
    for i in range(2,n):
        newRabbits = rabbits[i-2] * k
        rabbits.append(newRabbits + rabbits[i-1])
    return rabbits[n-1]
start = time.time()
print(Fibonaaci_Rabits(7,3))
end = time.time()
print(end - start)

start = time.time()
print(Rabbits(7,3))
end = time.time()
print(end - start)