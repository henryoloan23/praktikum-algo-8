def penjumlahan_rekursif(n, jumlah=0):
    
    if n == 0:
        return jumlah
    else:
        
        angka = int(input(f"Masukkan angka ke-{n}: "))
        
        return penjumlahan_rekursif(n - 1, jumlah + angka)


def utama():
    
    jumlah_bilangan = int(input("Masukkan Jumlah: "))
    
    hasil = penjumlahan_rekursif(jumlah_bilangan)
    print(f"Hasil penjumlahan: {hasil}")


utama()
