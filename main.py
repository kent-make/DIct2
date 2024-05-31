meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "Rolf": "tanggapan terhadap lelucon",
            "AGGRO": "untuk menjadi agresif/marah",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "SHEESH": "sedikit ketidaksetujuan",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").upper()

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("kode tidak ditemukan")
