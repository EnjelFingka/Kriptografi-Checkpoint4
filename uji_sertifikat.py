
import ssl
import socket

website = "self-signed.badssl.com"
port = 443

print("=== PENGUJIAN SERTIFIKAT TLS ===")
print("Website:", website)

pengaturan = ssl.create_default_context()

try:

    koneksi = socket.create_connection((website, port), timeout=10)

    with pengaturan.wrap_socket(
        koneksi,
        server_hostname=website
    ) as koneksi_aman:

        print("Koneksi berhasil")
        print("Versi TLS:", koneksi_aman.version())
        print("Sertifikat berhasil diverifikasi")

except ssl.SSLCertVerificationError as error:
    print("\nSertifikat ditolak oleh Python")
    print("Alasan:", error)
    print("Hasil: Pemeriksaan sertifikat bekerja")

except Exception as error:
    print("\nPengujian tidak berhasil diselesaikan")
    print("Alasan:", error)
