'''
https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
https://docs.python.org/3/tutorial/modules.html
https://realpython.com/python3-object-oriented-programming/ 


This python function collection creates a working set of RSA function including:

  * Generating key pairs
  * Printing the key pairs in plain ascii formats
  * saving the key pairs to separate public and private files
  * reading the keys back from files for re-use
  * encrypting a message or string using the public key
  * decrypting the message using the private key

Sample use cases:

def test_encrypt_msg(msg):
  # assuming we have generated test keys and saved them using 
  # rsa_key_gen and rsa_key_save
  keyPub = rsa_key_read('keyRSA.pub') # read public key from file
  encrypted = message_encrypt(msg,keyPub)
  with open('msg.bin', 'wb') as msg:
    msg.write(encrypted)
  return encrypted
  
def test_decrypt_msg(filename='msg.bin'):
  keyPriv = rsa_key_read('keyRSA.priv')
  with open('msg.bin','rb') as msg:
    encrypted=msg.read()
  decrypted = message_decrypt(encrypted, keyPriv, verbose=False)
  print(f'{decrypted}')

'''


from Crypto.PublicKey import RSA as _rsa
from Crypto.Cipher import PKCS1_OAEP as _cipher
import binascii as _binascii

def rsa_keys_gen(size=1024):
  '''
  generate the RSA key data using the default size of 1024 if not specified

  Input: size in blocks of 1024 with 1-024 being the minimum
  Output: return the keypair object

  Note: size 2048 is military grade encryption in current PC processing speed standards.
  '''
  #generate the keys
  keyPair = _rsa.generate(size)
  return keyPair

def rsa_keys_print(keyPair):
  '''
  simply print the current keys in plain ascii tect formt when passing the keypair 
  object into this function.
  '''
  #get and print the publick key
  pubKey = keyPair.publickey()
  # print f - embed format literals inside string using {}
  #print(f"Public key:  (n = {hex(pubKey.n)}, e = {hex(pubKey.e)})\n") 
  pubKeyPEM = pubKey.exportKey().decode('ascii')
  print('\n{}\n'.format(pubKeyPEM))

  #print(f"Private key: (n = {hex(pubKey.n)}, d = {hex(keyPair.d)})")
  privKeyPEM = keyPair.exportKey().decode('ascii') 
  print('{}'.format(privKeyPEM))

def rsa_keys_save(keyPair):
  '''
  Save the RSA key pair object in two separate files.
  '''
  with open('keyRSA.pub','w') as pubKey:
    pubKey.write(keyPair.publickey().exportKey().decode('ascii')) 
  with open('keyRSA.priv','w') as privKey:
    privKey.write(keyPair.exportKey().decode('ascii'))

def rsa_key_read(filename='keyRSA.pub'):
  '''
  read the RSA keys back from file and return as an RSA object for further processsing
  using encryption and decryption functions
  '''
  print(f'Loading keyfile: {filename}')
  with open(filename) as keyfile:
    RSAkey=_rsa.importKey(keyfile.read())
  return RSAkey

def message_encrypt(message, pubKey, verbose=False):
  '''
  encrypt a message string using the public key and return the encrypted string.
  '''
  encryptor = _cipher.new(pubKey)
  encrypted = encryptor.encrypt(bytes(message,'ascii'))
  #if verbose: print('Message: {}'.format(message))
  if verbose: print("Encrypted:", _binascii.hexlify(encrypted).decode('ascii'))
  #print("Encrypted:", binascii.hexlify(encrypted).decode('ascii'))
  return encrypted

def message_decrypt(message, keyPriv, verbose=False):
  '''
  decrypt a previously encrypted message using the RSA private key
  and return the decrypted message
  '''
  decryptor = _cipher.new(keyPriv)
  decrypted = decryptor.decrypt(message).decode('ascii')
  if verbose: print('Decrypted: {}'.format(decrypted))
  return decrypted

def test_encrypt_msg(msg):
  # assuming we have generated test keys and saved them using 
  # rsa_key_gen and rsa_key_save
  keyPub = rsa_key_read('keyRSA.pub') # read public key from file
  encrypted = message_encrypt(msg,keyPub)
  with open('msg.bin', 'wb') as msg:
    msg.write(encrypted)
  return encrypted
  
def test_decrypt_msg(filename='msg.bin'):
  keyPriv = rsa_key_read('keyRSA.priv')
  with open('msg.bin','rb') as msg:
    encrypted=msg.read()
  decrypted = message_decrypt(encrypted, keyPriv, verbose=False)
  print(f'{decrypted}')

  if __name__ == '__main__':

  #keyPair=rsa_gen_keys()
  #rsa_keys_print(keyPair)
  #rsa_keys_save(keyPair)
  #test_encrypt_msg('The rain in Spain falls mainley in the plain.')
  test_decrypt_msg()