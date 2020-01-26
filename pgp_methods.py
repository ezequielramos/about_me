import os
import gnupg
from dotenv import load_dotenv

load_dotenv()

gpg = gnupg.GPG(gnupghome=os.getenv("GNUPGHOME"))
passphrase = os.getenv("PASSPHRASE")


def generate_keys():
    global gpg, passphrase

    input_data = gpg.gen_key_input(
        name_email="ezequielmr94@gmail.com", passphrase=passphrase, Key_Length=4096
    )
    key = gpg.gen_key(input_data)
    print(key)
    key_string = key.__str__()

    ascii_armored_public_keys = gpg.export_keys(key_string)
    ascii_armored_private_keys = gpg.export_keys(
        key_string, True, passphrase=passphrase
    )
    with open("mykeyfile.asc", "w") as f:
        f.write(ascii_armored_public_keys)
        f.write(ascii_armored_private_keys)
    with open("public_key.asc", "w") as f:
        f.write(ascii_armored_public_keys)


def import_keys():
    global gpg
    key_data = open("public_key.asc").read()
    import_result = gpg.import_keys(key_data)
    print(import_result.results)


def list_keys():
    global gpg
    public_keys = gpg.list_keys()
    private_keys = gpg.list_keys(True)
    print("public keys:")
    print(public_keys)
    print("private keys:")
    print(private_keys)


def encrypt_string(unencrypted_string):
    global gpg

    encrypted_data = gpg.encrypt(unencrypted_string, "ezequielmr94@gmail.com")
    encrypted_string = str(encrypted_data)
    print("ok: ", encrypted_data.ok)
    print("status: ", encrypted_data.status)
    print("stderr: ", encrypted_data.stderr)
    print("unencrypted_string: ", unencrypted_string)
    print("encrypted_string: ", encrypted_string)
    return encrypted_string


def decrypt_string(encrypted_string):
    global gpg, passphrase

    decrypted_data = gpg.decrypt(encrypted_string, passphrase=passphrase)

    print("ok: ", decrypted_data.ok)
    print("status: ", decrypted_data.status)
    print("stderr: ", decrypted_data.stderr)
    print("decrypted string: ", decrypted_data.data)


def encrypt_file(file_path):
    global gpg

    with open(file_path, "rb") as f:
        status = gpg.encrypt_file(
            f, recipients=["ezequielmr94@gmail.com"], output="my-encrypted.txt.gpg"
        )

    print("ok: ", status.ok)
    print("status: ", status.status)
    print("stderr: ", status.stderr)


def decrypt_file(file_path):
    global gpg, passphrase

    with open(file_path, "rb") as f:
        status = gpg.decrypt_file(f, passphrase=passphrase, output="my-decrypted.txt")

    print("ok: ", status.ok)
    print("status: ", status.status)
    print("stderr: ", status.stderr)
