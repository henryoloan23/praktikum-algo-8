def perpangkatan(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * perpangkatan(a, b - 1)
    else:
        return 1 / perpangkatan(a, -b)


def userInput():
    while True:
        print('Ini merupakan program perpangkatan positif dan negatif')
        a = float(input("Masukkan angka awal: "))
        b = int(input("Masukkan pangkat: "))
        hasil = perpangkatan(a, b)
        
        print(f"Hasil {a} pangkat {b} adalah: {hasil}")
        
        ulang = input("Apakah Anda ingin menghitung lagi? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih telah menggunakan program ini.")
            break

userInput()
