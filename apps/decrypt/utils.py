import gnupg

def decrypt_message(passphrase, message):

    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    decrypted_data = gpg.decrypt(message, passphrase=passphrase)
    if decrypted_data.ok:
        return decrypted_data
    else:
        raise ValueError('Wrong value for passphrase or message')
