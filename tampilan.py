#Menampilkan judul permainan dan daftar pilihan 
def tampilkan_intro(TOTAL_RONDE):
        print("        GUNTING BATU KERTAS              ")
        print("=========================================")
        print(f"Jumlah ronde : {TOTAL_RONDE}")
        print("-----------------------------------------")
        print("[1] Gunting [2] Batu [3] Kertas")

#Menampilkan ronde ke berapa yang sedang berlangsung
def tampilan_header_ronde(ronde_ke, TOTAL_RONDE):
        print(f"[ RONDE {ronde_ke} / {TOTAL_RONDE} ]")
        print("-----------------------------------------")