from secrets import choice

def toplam (a , b):
   cevap = a + b
   print (str(a) + "+" + str(b) + "=" + str(cevap) + "\n")

def cikarma (a , b):
    cevap = a - b
    print (str(a) + "-" + str(b) + "=" + str(cevap) + "\n")

def bolme (a , b):
    cevap = a / b
    print (str(a) + "/" + str(b) + "=" + str(cevap) + "\n")

def carpma (a , b):
    cevap = a * b
    print (str(a) + "*" + str(b) + "=" + str(cevap) + "\n")

while  True:
    print ("A. Toplama işlemi")
    print ("B. Çıkarma İŞlemi")
    print ("C. Bölme işlemi")
    print ("D. Çarpma İŞlemi")
    print ("E. Programdan çık")

    choice = input("Yapmak İstediğiniz İŞlemi Seçiniz ?")

    if choice == "a" or choice == "A" :
            print ("Toplama")
            a = int(input("birinci sayıyı giriniz"))
            b = int(input("ikinci sayıyı giriniz"))
            toplam (a, b)
    elif choice == "b" or choice == "B" :
            print ("Çıkarma işlemi")
            a = int(input("birinci sayıyı giriniz"))
            b = int(input("ikinci sayıyı giriniz"))
            cikarma (a ,b)
    elif choice == "c" or choice == "C" :
            print ("bölme işlemi")
            a = int(input("birinci sayıyı giriniz"))
            b = int(input("ikinci sayıyı giriniz"))
            bolme (a , b)
    elif choice == "d" or choice == "D" :
            print ("Çarpma işlemi")
            a = int(input("birinci sayıyı giriniz"))
            b = int(input("ikinci sayıyı giriniz"))
            carpma (a , b)
    elif choice == "e" or choice == "E" :
            print ("program sonlandırılıyor")
            quit()