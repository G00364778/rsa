# https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
# https://docs.python.org/3/tutorial/modules.html
# https://realpython.com/python3-object-oriented-programming/ 


from Crypto.PublicKey import RSA as _rsa
from Crypto.Cipher import PKCS1_OAEP as _cipher
import binascii as _binascii
from os.path import splitext as _fext

class rsa:
  _val_keylen = 1024
  _val_oninit_newkeys = False
  _str_priv='keyRSA.pri'
  _str_pub='keyRSA.pub'
  _encrypted = None 
  _decrypted = None
  
  def __init__(self):
    if self._val_oninit_newkeys == True:
      self._keys =_rsa.generate(self._val_keylen)
    else:
      self._keyPub = self._rsa_key_read(self._str_pub)
      self._keys = self._rsa_key_read(self._str_priv)


  def __str__(self):
    #print('printing')
    keystr='Objects:\n\t{}\n\t{}\nStrings:\n{}\n{}'.format(self._keys,self._keys.publickey(),
      self._keys.publickey().exportKey().decode('ascii'), 
      self._keys.exportKey().decode('ascii'))
    return keystr
  
  def config(self,new_keylen=None,new_init=None,new_priv=None,new_pub=None):
    '''
    Show the configuration values and provide option to edit them.

      val_keylen         - default 1024 or multiples of 1024, i.e 2048 or 3072
      val_oninit_newkeys - default False, set to true generates a new kep pair on 
                         initialisation, set to false reads it from file.

      str_priv - the filename for the private key file 
      str_pub  - the file name for the public key file

    Calling config without values shows the current values. set new values by 
    passing paramater names and values into the function call
    
      new_keylen=2048
      new_init=True
      new_priv='keyname.pri'
      new_pub='keyname.pub'
      
    '''
    if new_keylen==None and new_init==None and new_priv==None and new_pub==None:
      print('        val_keylen: {}\
        \n_val_oninit_newkeys: {}\
        \n          _str_priv: {}\
        \n           _str_pub: {}\
        \n{}'.format(self._val_keylen,self._val_oninit_newkeys, 
        self._str_priv,self._str_pub,self))
    elif new_keylen is not None:
      if new_keylen%1024==0:
        self._val_keylen=new_keylen
        print(f'_val_keylen = {new_keylen}')
      else:
        return 'Error, value must be a multiple of 1024'
    if new_init is not None:
      if new_init == True:
        self._val_oninit_newkeys =True
        print(f'_val_oninit_newkeys = {new_init}')
      elif new_init == False:
        self._val_oninit_newkeys =False
        print(f'_val_oninit_newkeys = {new_init}')
      else:
        print(f'Error, value must be True or False, value {new_init} incorrect.')
    if new_priv is not None:
      self._str_priv=new_priv
      print(f'_str_priv = {new_priv}')
    if new_pub is not None:
      self._str_pub=new_pub
      print(f'_str_pub = {new_pub}')

  def new(self):
    '''
    Create new RSA keypairs using the current configuration. See config() for details.
    
    '''
    self._keys =_rsa.generate(self._val_keylen)
    self._keyPub = self._keys.publickey()

  def readfile(self,file='msg.bin'):
    '''
    Read an encrypted or decrypted message from file.

    readfile(file='filename.ext', format='rb'), omit b if not an encrypted binary file

    '''
    if _fext(file)[1][1:]=='txt': fmt='r'
    if _fext(file)[1][1:]=='bin': fmt='rb'
    else: fmt='r'

    with open(file,fmt) as msg:
      self._msg=msg.read()

  def save(self, filename='msg'):
    '''
    save the messages stored in _encrypted and _decrypted to msg.bin and msg.txt of using the 
    filename passed into the function call appending .msg and .bin if the variables are populated

    '''
    if self._encrypted is not None:
      with open(f'{filename}.bin', 'wb') as msg:
        msg.write(self._encrypted)
    if self._decrypted is not None:
      with open(f'{filename}.txt', 'w') as msg:
        msg.write(self._decrypted)

  def encrypt(self):
    '''
    Run the rsa encryption on the message loaded by readfile() routine.

    The file extensions determined the variable encoding, so it is important to define 
    
    '''
    encryptor = _cipher.new(self._keyPub)
    self._encrypted = encryptor.encrypt(bytes(self._msg,'ascii'))
    print(f'Encrypted message: {self._encrypted}')

  def decrypt(self):
    '''
    Run the rsa decryption on the message loaded by readfile() routine.

    The message is stored in ._decrypted variable

    '''
    decryptor = _cipher.new(self._keys)
    self._decrypted = decryptor.decrypt(self._msg).decode('ascii')
    print(f'Decrypted message: {self._decrypted}')
  
  def _rsa_key_read(self, filename):
    #internal key read function
    with open(filename) as keyfile:
      RSAkey=_rsa.importKey(keyfile.read())
    return RSAkey

if __name__ == '__main__':
  keys = rsa()