def listedesay(liste):
    adet = 0
    for sayi in liste:
        if sayi == 4:
            adet +=1
    return adet

print(listedesay([1,4,1,2,7,4,9,0,1,2,8,4]))
