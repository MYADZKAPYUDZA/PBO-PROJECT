import random

#Menampilkan pilihan angka 1/2/3 kepada pemain untuk diinputkan, mengembalikan nilai integer dari inputan pemain dan none jika salah input
def ambil_pilihan_pemain():
    pilihan = input("Pilihan Anda (1/2/3): ")
    match pilihan:
        case "1" | "2" | "3":
            return int(pilihan)
        case _:
            print("Pilihan tidak ada, ulangi kembali")
            return None

#Komputer memilih angka antara 1-3 secara acak
def pilihan_komputer():
    return random.randint(1, 3)