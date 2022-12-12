# ====================================================================
# Ülesanne
# Autor: Kevin Kiho
# Kuupäev: 12/12/2022
# ====================================================================
# Koosta programm, mis aitab lastel treenida liitmist. Programm peaks pakkuma välja juhuslike
# arvudega liitmistehteid ning ootama kasutajalt vastust. Kui vastus on õige, kiitma kasutajat,
# kui aga vale, andma õige vastuse ja esitama uue tehte. Järjest esitatavate tehete hulk võib
# olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid, kui suuri arve
# kasutajalt küsitakse (näiteks 1 kuni 50). Programm peaks pidama arvestust ka õigete vastuste
# üle ning väljastama pärast viimast tehet tulemuse.
#
# Muutke programmi selliselt, et kasutajalt küsitakse ka teisi tehteid (lahutamine, korrutamine,
# jagamine). Tehte võite küsida kasutajalt või lasta arvutil genereerida erinevad tehted iga
# arvutuse kohta.
#
# Muutke programmi nii, et esitavate arvude piirid saab kasutaja ette anda – nii maksimumi kui
# ka miinimumi.
# ====================================================================

# Liitmise treenimine
import random
while(True):
    rand1=random.randint(1,50)
    rand2=random.randint(1,50)
    ans=int(input('Mis on '+str(rand1)+'+'+str(rand2)+'?\n'))
    if( ans == (rand1+rand2)):
        print("Õige, tubli")
    else:
        print("Vale, õige vastus on")




