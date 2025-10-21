# 🧩 TWO-WAY ENCRYPTED COMMUNICATION  
### Implementasi Client-Server 
---

##  INFORMASI UMUM
| Keterangan | Detail |
|-------------|---------|
| **Nama File** | `crypto_communication.py` |
| **Deskripsi** | Program komunikasi dua arah (client-server)  menggunakan **Caesar**, **Vigenère**, atau **XOR Cipher** |
| **Bahasa Pemrograman** | Python 3 |
| **Mode Komunikasi** | Dua arah (bidirectional) |
| **Tipe Koneksi** | Socket TCP |
| **Default Host** | `127.0.0.1` |
| **Default Port** | `5555` |
| **Shared Key Default** | `SECURITY` |
---

##  KONFIGURASI CIPHER
| Cipher | Jenis | Deskripsi Singkat | Formula / Proses |
|---------|--------|-------------------|------------------|
| **Caesar Cipher** | Substitution | Menggeser setiap huruf sejauh 3 posisi | `C = (P + 3) mod 26` |
| **Vigenère Cipher** | Polyalphabetic | Menggunakan kunci berulang untuk enkripsi | `Ci = (Pi + Ki) mod 26` |
| **XOR Cipher** | Simulasi Block Cipher | XOR antara plaintext dan key (base64 encoded) | `C = P ⊕ K` |
---

##  KEAMANAN YANG DICAPAI
| Aspek | Deskripsi |
|--------|------------|
| **Confidentiality** | Pesan terenkripsi, tidak bisa dibaca pihak ketiga |
| **Integrity** | Pesan tidak berubah saat transmisi |
| **Authentication** | Kedua device menggunakan **shared key** yang sama |
| **Non-repudiation** | Riwayat komunikasi bisa direkam/dilihat di terminal |
---

##  CARA MENJALANKAN PROGRAM
```bash
1. Pastikan Python 3.x sudah terinstall
2. Simpan file dengan nama crypto_communication.py
3. Buka 2 terminal (CMD / PowerShell / Terminal Linux)
4. Jalankan server di terminal pertama:
   python crypto_communication.py server
5. Jalankan client di terminal kedua:
   python crypto_communication.py client
6. Ketik pesan bolak-balik antara kedua terminal
7. Ketik 'exit' untuk keluar dari program

## KONFIGURASI TAMBAHAN
# Pilih cipher yang ingin digunakan
CIPHER_TYPE = "caesar"  # opsi: "caesar", "vigenere", "xor"

# Ganti shared key jika ingin berbeda
SHARED_KEY = "SECURITY"

# Ubah alamat dan port jika diperlukan
HOST = '127.0.0.1'
PORT = 5555
