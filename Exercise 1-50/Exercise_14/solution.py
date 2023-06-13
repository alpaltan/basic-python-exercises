from datetime import date
baslangic_Tarihi = date(2014, 7, 2)
bitis_Tarihi = date(2014, 7, 11)
fark = bitis_Tarihi - baslangic_Tarihi
print("Aradaki fark :", fark.days, "Gun")
