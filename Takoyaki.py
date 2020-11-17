total1=0
total2=0
totalsemua=0
jenis1=""
jenis2=""

stop = False
while(not stop):


    print("=====================================================")
    print("================ Toko Kue Takoyaki ==================")
    print("=====================================================")
    nama = input("Masukkan nama Konsumen: ")
    print ("Nama Konsumen :", nama)
    print("")
    print("Pilihan varian takoyaki")

    def pilihan(i):
        switcher={
                1:'----varian 1 Rp.2000----',
                2:'----varian 2 Rp.2500----',
                
        }
        return switcher.get(i,"Masukan Pilihan yang Benar!")
        


    print("1. varian 1")
    print("2. varian 2")
    nomor=int(input("Masukan Pilihan varian: "))
    menu=pilihan(nomor)
    print (menu)
    porsi1= int(input("Berapa Porsi: "))

    if nomor==1:
        total1=total1+porsi1*2000
        print ("Hasilnya = :Rp.", total1)
        jenis1=("takoyaki varian 1")
        if porsi1 > 10:
            print("Selamat anda mendapatkan diskon 10%")
            diskon = 10/100 * total1
            print("Rp.", diskon)
            setelah_diskon = total1 - diskon
            print("Yang harus di bayar Rp.", setelah_diskon)
        else :
            print("Maaf anda tidak mendapat diskon")

    elif nomor==2:
        total2=total2+porsi1*2500
        print ("Hasilnya = :Rp.", total2)
        jenis1=("takoyaki varian 2")
        if porsi1 > 8:
            print("Selamat anda mendapatkan diskon 8%")
            diskon = 8/100 * total2
            print("Rp.", diskon)
            setelah_diskon = total2 - diskon
            print("Yang harus di bayar Rp.", setelah_diskon)
    else :
        print("Menu pilihan takoyaki tidak ada")
    ulang = input('Apakah Kamu ingin membeli takoyaki lagi ? ya/tidak :')
    if (ulang == 'tidak'):
        stop = True

print("====== Terima Kasih Telah beli kue takoyaki di sini ======")