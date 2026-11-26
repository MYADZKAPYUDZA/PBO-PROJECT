TOTAL_RONDE = 5
NAMA_PILIHAN = {
  1: "Gunting",
  2: "Batu",
  3: "Kertas",
}

PESAN_HASIL = {
  "seri": "SERI",
  "pemain": "ANDA MENANG",
  "komputer": "KOMPUTER MENANG",
}

def buat_skor_awal():
    """Mengembalikan dictionary skor awal permainan."""
    return {"pemain": 0, "komputer": 0, "seri": 0}
