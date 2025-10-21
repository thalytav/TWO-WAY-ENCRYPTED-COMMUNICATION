# TWO-WAY-ENCRYPTED-COMMUNICATION
# TWO-WAY ENCRYPTED COMMUNICATION

Program komunikasi dua arah (client-server) dengan enkripsi simetris menggunakan berbagai jenis cipher (Caesar, Vigenère, XOR).

---

## 1. PERSIAPAN

### 1.1 Instalasi Python
Pastikan **Python 3.x** sudah terpasang di komputer.  
- Jika belum, unduh dari [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Pastikan Python dapat dijalankan melalui Command Prompt atau Terminal.

### 1.2 Instalasi Git (Opsional)
Jika ingin melakukan clone repository:
- Unduh Git dari [https://git-scm.com/downloads](https://git-scm.com/downloads)

### 1.3 Clone Repository
```bash
git clone https://github.com/aqilazn/TWO-WAY-ENCRYPTED-COMMUNICATION.git
1.4 Masuk ke Direktori Proyek
bash
Salin kode
cd TWO-WAY-ENCRYPTED-COMMUNICATION
2. MENJALANKAN SERVER (DEVICE 1)
2.1 Buka Terminal Pertama
Pastikan sudah berada di dalam folder proyek.

2.2 Jalankan Server
bash
Salin kode
python crypto_communication.py server
2.3 Contoh Output
markdown
Salin kode
============================================================
SERVER (DEVICE 1) STARTED
Listening on 127.0.0.1:5555
Shared Key: SECRETKEY
Cipher Type: VIGENERE
============================================================
3. MENJALANKAN CLIENT (DEVICE 2)
3.1 Buka Terminal Kedua
Buka terminal baru di lokasi yang sama.

3.2 Jalankan Client
bash
Salin kode
python crypto_communication.py client
3.3 Contoh Output
vbnet
Salin kode
============================================================
CLIENT (DEVICE 2) STARTED
Connecting to 127.0.0.1:5555
Shared Key: SECRETKEY
Cipher Type: VIGENERE
============================================================
Connected to server
4. KOMUNIKASI DUA ARAH
4.1 Contoh: Server Mengirim ke Client
Terminal 1 (Server):

pgsql
Salin kode
Type message to send: Hello from Device 1
ENCRYPTED: DITSYJVCKQHGMEZI
Sent to client
Terminal 2 (Client):

pgsql
Salin kode
RECEIVED (Encrypted): DITSYJVCKQHGMEZI
DECRYPTED: HELLOFROMDEVICE
------------------------------------------------------------
4.2 Contoh: Client Mengirim ke Server
Terminal 2 (Client):

pgsql
Salin kode
Type message to send: Hi Device 1, message received
ENCRYPTED: DESPWGMLIRQWEKMGXMZMGML
Sent to server
Terminal 1 (Server):

pgsql
Salin kode
RECEIVED (Encrypted): DESPWGMLIRQWEKMGXMZMGML
DECRYPTED: HIDEVICEMESSAGERECEIVED
------------------------------------------------------------
5. KONFIGURASI CIPHER
5.1 Pengaturan Cipher
Edit bagian berikut di dalam file crypto_communication.py:

python
Salin kode
CIPHER_TYPE = "vigenere"  # Pilihan: "caesar", "vigenere", "xor"
SHARED_KEY = "SECRETKEY"  # Ganti sesuai kebutuhan
5.2 Pilihan Cipher
Jenis Cipher	Deskripsi
caesar	Cipher klasik dengan pergeseran 3 karakter
vigenere	Cipher berbasis kata kunci (polyalphabetic)
xor	Cipher berbasis operasi XOR sederhana (ECB mode)

6. TROUBLESHOOTING
Masalah	Penyebab	Solusi
Address already in use	Port 5555 masih digunakan	Tutup terminal sebelumnya atau tunggu ±30 detik
Connection refused	Server belum dijalankan	Jalankan server terlebih dahulu sebelum client
Module not found	Modul Python tidak ditemukan	Semua modul sudah bawaan Python, tidak perlu instalasi tambahan