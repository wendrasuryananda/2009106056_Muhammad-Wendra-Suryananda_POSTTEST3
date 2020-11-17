print("======================")
print("=== Selamat Datang ===")
print("======================")

n = int(input("Masukkan Nilai Yang Anda Mau :"))
for x in range(n):
    if(10 ** x > n):
        break
    else:
        print("POSTTEST3")
    print("Nilai yang terkecil dari 10^x > n adalah", 10 ** x)
