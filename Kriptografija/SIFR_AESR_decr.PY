# PROGRAMOS SIFR_AESS.PY KODAS
from Crypto.Cipher import AES
from binascii import unhexlify

def decrypt_aes_eax(ciphertext_hex, key, tag_hex, nonce_hex):
    # Konvertuojame šiuos duomenis iš šešioliktainės į baitų sekas
    ciphertext = unhexlify(ciphertext_hex)
    tag = unhexlify(tag_hex)
    nonce = unhexlify(nonce_hex)

    # Sukuriamas šifravimo objektas su pateiktu raktu ir nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
     
    # Bandoma iššifruoti tekstą ir patikrinti MAC su pateiktu tag'u
    try:
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode('utf-8')
    except ValueError:
        return "Užšifruotas tekstas buvo pažeistas. Iššifravimas nutrauktas."

def main():
    # Pateikti duomenys
    key = b"ThisIsASecretKey_32bytesLongAbCd"
    ciphertext_hex = "2151af1a1f3a491ff95ec6dcc9ff"
    tag_hex = "ba7b5ff88a2de48967d2a6b209954966"
    nonce_hex = "fd9655ff484ed75f6dc125cfe6dc74c9"

    decrypted_message = decrypt_aes_eax(ciphertext_hex, key, tag_hex, nonce_hex)
    print(f"Iššifruotas tekstas: {decrypted_message}")

if __name__ == '__main__':
    main()
