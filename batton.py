X=20
while X>1:
    print("Le nombre restant : ",X)
    A=int(input("Le choix du premier joueur : "))
    while A<1 or A>3:
        A=int(input("Nombre entre 1 et 3 : "))
    X=X-A
    if X==1:
        print("Joueur 1 gagné")
    else:
       print("Le nombre restant : ",X)
       B=int(input("Le choix du deuxiéme : "))
       while B<1 or B>3:
           B=int(input("Nombre entre 1 et 3 : "))
       X=X-B
       if X==1:
         print("Joueur 2 gagné")