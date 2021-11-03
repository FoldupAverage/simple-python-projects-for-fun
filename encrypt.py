from cryptography.fernet import Fernet
 
message = 'A very secret message from jcchouinard.com'

# key for encryption and decryption
key = Fernet.generate_key()
fernet = Fernet(key)
 
encrypted = fernet.encrypt(message.encode())
 
print('Message: ', message)
print("Encrypted: ", encrypted)
 

decrypted = fernet.decrypt(encrypted).decode()

print('Decrypted: ', decrypted)