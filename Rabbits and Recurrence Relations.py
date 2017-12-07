def Fibonaaci_Rabits(n,k):
    if n==1: return 1
    if n==2: return k
    oneGen = Fibonaaci_Rabits(n-1,k)
    secGen = Fibonaaci_Rabits(n-2,k)
    if n<=4: return oneGen+secGen
    return (oneGen + secGen*k)



print(Fibonaaci_Rabits(34,3))