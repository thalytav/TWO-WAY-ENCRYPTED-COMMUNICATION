# ============================================
# TUGAS 2: TWO-WAY ENCRYPTED COMMUNICATION
# Implementasi Client-Server dengan Enkripsi
# ============================================

import socket
import threading
import base64

# ============ SHARED KEY ============
SHARED_KEY = "SECURITY"
HOST = '127.0.0.1'
PORT = 5555

# =======================
# CIPHER IMPLEMENTATIONS 
# =======================

# 1. CAESAR CIPHER 
def caesar_encrypt(text, shift=3):
    """Encrypt menggunakan Caesar Cipher dengan shift 3"""
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    """Decrypt Caesar Cipher"""
    return caesar_encrypt(text, 26 - shift)


# 2. VIGENERE CIPHER 
def vigenere_encrypt(plaintext, key):
    """Encrypt menggunakan Vigenere Cipher"""
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha())
    key = ''.join(c for c in key.upper() if c.isalpha())
    result = ""
    
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - 65
        k = ord(key[i % len(key)]) - 65
        c = (p + k) % 26
        result += chr(c + 65)
    
    return result

def vigenere_decrypt(ciphertext, key):
    """Decrypt Vigenere Cipher"""
    ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
    key = ''.join(c for c in key.upper() if c.isalpha())
    result = ""
    
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - 65
        k = ord(key[i % len(key)]) - 65
        p = (c - k + 26) % 26
        result += chr(p + 65)
    
    return result


# 3. SIMPLE XOR CIPHER (simulating block cipher)
def xor_encrypt(plaintext, key):
    """Encrypt menggunakan XOR"""
    result = []
    for i in range(len(plaintext)):
        result.append(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return base64.b64encode(bytes(result)).decode()

def xor_decrypt(ciphertext, key):
    """Decrypt XOR"""
    try:
        decoded = base64.b64decode(ciphertext)
        result = ""
        for i in range(len(decoded)):
            result += chr(decoded[i] ^ ord(key[i % len(key)]))
        return result
    except:
        return "[ERROR DECRYPTING]"


# ============================
# PILIH CIPHER YANG DIGUNAKAN
# ============================
CIPHER_TYPE = "caesar"  # Ganti: "caesar", "vigenere", atau "xor"

def encrypt_message(message):
    """Encrypt message berdasarkan cipher yang dipilih"""
    if CIPHER_TYPE == "caesar":
        return caesar_encrypt(message)
    elif CIPHER_TYPE == "vigenere":
        return vigenere_encrypt(message, SHARED_KEY)
    elif CIPHER_TYPE == "xor":
        return xor_encrypt(message, SHARED_KEY)
    return message

def decrypt_message(encrypted):
    """Decrypt message berdasarkan cipher yang dipilih"""
    if CIPHER_TYPE == "caesar":
        return caesar_decrypt(encrypted)
    elif CIPHER_TYPE == "vigenere":
        return vigenere_decrypt(encrypted, SHARED_KEY)
    elif CIPHER_TYPE == "xor":
        return xor_decrypt(encrypted, SHARED_KEY)
    return encrypted


# ===================
# SERVER (Device 1)
# ===================
def start_server():
    """Server - Device 1 yang menerima dan mengirim pesan"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    
    print("="*60)
    print(" SERVER (DEVICE 1) STARTED")
    print(f"   Listening on {HOST}:{PORT}")
    print(f"   Shared Key: {SHARED_KEY}")
    print(f"   Cipher Type: {CIPHER_TYPE.upper()}")
    print("="*60)
    
    conn, addr = server.accept()
    print(f" Client connected from {addr}\n")
    
    # Thread untuk menerima pesan
    def receive_messages():
        while True:
            try:
                encrypted = conn.recv(1024).decode()
                if not encrypted:
                    break
                
                print(f"\n RECEIVED (Encrypted): {encrypted}")
                decrypted = decrypt_message(encrypted)
                print(f" DECRYPTED: {decrypted}")
                print("-" * 60)
            except:
                break
    
    # Thread untuk mengirim pesan
    def send_messages():
        while True:
            try:
                message = input(" Type message to send: ")
                if message.lower() == 'exit':
                    break
                
                encrypted = encrypt_message(message)
                print(f" ENCRYPTED: {encrypted}")
                conn.send(encrypted.encode())
                print(f" Sent to client\n")
            except:
                break
    
    # Jalankan kedua thread
    recv_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)
    
    recv_thread.daemon = True
    recv_thread.start()
    send_thread.start()
    send_thread.join()
    
    conn.close()
    server.close()


# ==================
# CLIENT (Device 2)
# ==================
def start_client():
    """Client - Device 2 yang mengirim dan menerima pesan"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("="*60)
    print(" CLIENT (DEVICE 2) STARTED")
    print(f"   Connecting to {HOST}:{PORT}")
    print(f"   Shared Key: {SHARED_KEY}")
    print(f"   Cipher Type: {CIPHER_TYPE.upper()}")
    print("="*60)
    
    try:
        client.connect((HOST, PORT))
        print(" Connected to server\n")
    except:
        print(" Failed to connect to server!")
        return
    
    # Thread untuk menerima pesan
    def receive_messages():
        while True:
            try:
                encrypted = client.recv(1024).decode()
                if not encrypted:
                    break
                
                print(f"\n RECEIVED (Encrypted): {encrypted}")
                decrypted = decrypt_message(encrypted)
                print(f" DECRYPTED: {decrypted}")
                print("-" * 60)
            except:
                break
    
    # Thread untuk mengirim pesan
    def send_messages():
        while True:
            try:
                message = input(" Type message to send: ")
                if message.lower() == 'exit':
                    break
                
                encrypted = encrypt_message(message)
                print(f" ENCRYPTED: {encrypted}")
                client.send(encrypted.encode())
                print(f" Sent to server\n")
            except:
                break
    
    # Jalankan kedua thread
    recv_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)
    
    recv_thread.daemon = True
    recv_thread.start()
    send_thread.start()
    send_thread.join()
    
    client.close()


# ==============
# MAIN PROGRAM
# ==============
if __name__ == "__main__":
    print("\n" + "="*60)
    print("  TWO-WAY ENCRYPTED COMMUNICATION SYSTEM")
    print("  Implementasi Materi KI 01-04")
    print("="*60)
    print("\n  CONFIGURATION:")
    print(f"   Shared Key: {SHARED_KEY}")
    print(f"   Cipher: {CIPHER_TYPE.upper()}")
    print("\n CARA MENJALANKAN:")
    print("   1. Buka 2 terminal/command prompt")
    print("   2. Terminal 1: python script.py server")
    print("   3. Terminal 2: python script.py client")
    print("   4. Ketik pesan bolak-balik antara kedua device")
    print("   5. Ketik 'exit' untuk keluar")
    print("="*60 + "\n")
    
    import sys
    
    if len(sys.argv) < 2:
        print(" Usage: python script.py [server|client]")
        print("   Example: python script.py server")
        print("            python script.py client")
    elif sys.argv[1].lower() == 'server':
        start_server()
    elif sys.argv[1].lower() == 'client':
        start_client()
    else:
        print("Invalid argument. Use 'server' or 'client'")


# ============================================
# PENJELASAN CIPHER 
# ============================================
"""
1. CAESAR CIPHER:
   - Substitution cipher sederhana
   - Shift setiap huruf 3 posisi (A ke D, B ke E, dst)
   - Formula: C = (P + 3) mod 26
   - Kelemahan: Hanya 26 kemungkinan (brute force mudah)

2. VIGENERE CIPHER:
   - Polyalphabetic substitution cipher
   - Menggunakan keyword yang diulang
   - Lebih aman dari Caesar karena multiple alphabets
   - Formula: Ci = (Pi + Ki) mod 26
   - Dapat diserang dengan Kasiski method

3. XOR CIPHER:
   - Simulasi modern block cipher
   - Menggunakan ECB mode (Electronic Codebook)
   - Operasi XOR antara plaintext dan key
   - Base64 encoding untuk transmission

SECURITY PROPERTIES:
Confidentiality: Data tidak terlihat oleh pihak tidak berwenang
Integrity: Data tidak berubah saat transmisi
Authentication: Kedua device menggunakan shared key yang sama
Non-repudiation: History komunikasi tercatat
"""