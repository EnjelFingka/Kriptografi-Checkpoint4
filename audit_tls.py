
import ssl
import socket

website = "github.com"
port = 443

print("=== PENGUJIAN KEAMANAN TLS ===")
print("Website:", website)

pengaturan = ssl.create_default_context()

try:

    koneksi = socket.create_connection((website, port), timeout=10)

    koneksi_aman = pengaturan.wrap_socket(
        koneksi,
        server_hostname=website
    )

    versi_tls = koneksi_aman.version()
    cipher = koneksi_aman.cipher()
    sertifikat = koneksi_aman.getpeercert()

    print("\n=== HASIL PENGUJIAN ===")
    print("Versi TLS:", versi_tls)
    print("Cipher yang digunakan:", cipher[0])
    print("Verifikasi sertifikat: Berhasil")

    print("\n=== INFORMASI SERTIFIKAT ===")
    print("Nama website:", sertifikat.get("subject"))
    print("Penerbit sertifikat:", sertifikat.get("issuer"))
    print("Berlaku sampai:", sertifikat.get("notAfter"))

    print("\nKesimpulan:")
    print("Koneksi TLS berhasil dibuat dan sertifikat valid.")

    koneksi_aman.close()

except Exception as error:
    print("\nPengujian gagal.")
    print("Penyebab:", error)
