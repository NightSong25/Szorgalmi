#Először kérjétek be a felhasználó nevét.
bekert_nev = input("Add meg a neved ")
#Felhasználótól meg kell kérdezni,hogy milyen autót szeretne bérelni,(BMW,Ford,Audi),legyen különbség az autók ára között a bérlés szempontjából
auto = input("Add meg milyen autót szeretnél bérelni (BMW,Ford,Audi): ")
nap = int(input("Hány napra szeretnéd bérelni?: "))

if auto == "BMW":
    ar = 15000*nap 
elif auto == "Ford":
    ar = 10000*nap
elif auto == "Audi":
    ar = 20000*nap
print(f"A bérlő neve: {bekert_nev}, az autó, amit bérel: {auto}, a fitezendő ár: {ar} Ft.")