#ikinci dereceden denklemin köklerini bulan program
#ax^2+bx^+c=0
#17.11.2020 salı

import math         #karekök alma fonkisiyonuna ihtiyacımız var

#denklem katsayılarının kullanıcıdan alınması
a=eval(input("a katsayısını giriniz:"))
b=eval(input("b katsayısını giriniz:"))
c=eval(input("c katsayısını giriniz:"))

#diskriminant hesabı
d=  b*b-(4*a*c)

if d<0:                                                                                 #if elif else olarakta devam edebilirdik 
    print("denklemin reel kökleri yoktur")                         #eğer öyle devam etseydi hangisine uyuyosa
                                                                                          #ondan sonrasını kontrol etme gereği duymaz 
if d==0:                                                                             #program performansı artar
    print ("denkelmin kökleri çakışıktır")
    x=-b/(2*a)
    print("x1=x2=",x)

if d>0:
    print("denklemin iki farklı kökü vardır")
    x1=(-b- math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print("x1=",x1)
    print("x2=",x2)

print("program sonlandı")
