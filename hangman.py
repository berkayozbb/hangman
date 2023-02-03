data = [
  'Belarus',
  'Belgium',
  'Bhutan',
  'Brazil',
  'Brunei',
  'Chad',
  'Chile',
  'China',
  'Cuba',
  'Cyprus',
  'Denmark',
  'Ecuador',
  'Egypt',
  'Estonia',
  'France',
  'Gabon',
  'Georgia',
  'Germany',
  'Guinea',
  'Honduras',
  'Hungary',
  'Iceland',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jordan',
  'Kenya',
  'Korea',
  'Kuwait',
  'Laos',
  'Libya',
  'Maldives',
  'Mali',
  'Malta',
  'Mexico',
  'Mozambique',
  'Nepal',
  'Niger',
  'Norway',
  'Oman',
  'Peru',
  'Poland',
  'Portugal',
  'Singapore',
  'Slovenia',
  'Spain',
  'Sudan',
  'Suriname',
  'Switzerland',
  'Syria',
  'Tonga',
  'Turkey',
  'Ukraine',
  'Uzbekistan',
  'Vietnam',
]
usedLetters=[]
showScreen=False
kelime=[]
tahta=[]
ipucu=["It's a country ;)"]
import random
for q in range(len(data)):
    print("")
if q <=56:
    ipucu=ipucu[0]
randNum=random.randrange(0,q)
secilenKelime=data[randNum]
secilenKelime=secilenKelime.lower()
for i in range(len(secilenKelime)):
    harf=secilenKelime[i]
    kelime.append(harf)
    tahta.append(" _ ")
case=True
indexNo=-1
kalanHak=5
while case==True:
    if " _ " in tahta:
        print("")
    else:
        print(f"Doğru Kelime : \n**********\n{secilenKelime.upper()}\n**********")
        print("Kelimeyi doğru bildiniz!\nTEBRİKLER")
        case=False
        break
    print(tahta)
    print(f"Kalan haklar : {kalanHak}")
    harf=input("İçinde olabileceğini düşündüğünüz harfi giriniz : \n(Yalnızca harf ve 1 karakter olmalı)\n")
    usedLetters.append(harf)
    print(f"Alınan harfler : \n{usedLetters}")
    if len(harf)>1:
        print("Yalnızca 1 karakter uzunluğunda harf giriniz!")
        continue
    if harf in kelime:
        indexNo=kelime.index(harf)
        if tahta[indexNo]!=harf:
            tahta.pop(indexNo)
            tahta.insert(indexNo,harf)
        else:
            kalanHak-=1
        if kalanHak<2 and kalanHak!=0 and showScreen==False:
            ipucuSorgu=input("İpucu ister misin ?\n(Evet için : e )\n(Hayır için : h )")
            if ipucuSorgu=="e":
                print(f"\n**********\nCLUE : \n{ipucu}\n**********") 
                showScreen=True   
        if kalanHak==0:
            print("Game Over :( ")
            print(f"Doğru Kelime : \n**********\n{secilenKelime.upper()}\n**********")
            break
    else:
        kalanHak-=1
        if kalanHak<2 and kalanHak!=0 and showScreen==False:
            ipucuSorgu=input("İpucu ister misin ?\n(Evet için : e )\n(Hayır için : h )")
            if ipucuSorgu=="e":
                print(f"\n**********\nCLUE : \n{ipucu}\n**********")
                showScreen=True
        if kalanHak==0:
            print("Game Over :( ")
            print(f"Doğru Kelime : \n**********\n{secilenKelime.upper()}\n**********")
            break
