# Python RSA implementation

## Disclaimer

The RSA key samples in this repository are compromised. Do not use these in you applications, please generate new ones.  

## Files

This repository contains two RSA style encryption/decription implementations using puthon and standard puthon libraries.

  - rsa_lib.py - procedural implementation with working examples
  - lib_rsa.py - object oriented implementation 
  - mac.py - extract all the ip and mac addresses on the local server/pc

The repository also cantains a key pair, a public key and a private key. Public keys are used for encryption and private keys are require for decryption. The public key is a subset of the private key. 

  - keyRSA.pub - the public key
  - keyRSA.pri - the private key
  
There aro also two test messages, one encrypted and one decrypted or plain text, the encrypted messages can only be decrypted with the existing private key.

  - msg.txt - a plain text unencrypted message
  - msg.bin -  a binary file format encrypted message, can be viewed in a plian text format to see encryption.
  
## Installation and removal

pip install git+https://github.com/g00364778/rsa.git#egg=telmsRSA
conda install git+https://github.com/g00364778/rsa.git#egg=telmsRSA

pip uninstall telmsrsa
conda uninstall telmsrsa


## Usage
  
rsa_lib.py can simply be copied and run as is in a python environment. 
  
lib_rsa.py must be instantiated and then manipulated.

```python
In [1]: import lib_rsa as l

In [2]: k=l.rsa()

In [3]: print(k)

Objects:
        <_RSAobj @0x1f4472ddf08 n(1024),e,d,p,q,u,private>
        <_RSAobj @0x1f4472efa88 n(1024),e>
Strings:
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoQsAzm88drFjEHUZukF4bvLuD
QmUJM0kj4xdOO8ws6E3CrHU45tLRYfus2gcwUvCsuvy8VN8y5lbNST2wvpRgiRVC
HL2tb07gzbez0k2+gBYEe/8pJ8bLL8qtuC498SDN8TX1VDifzvlIugNIH2xIOYbQ
ZK6c/AOPY6sEGgKnowIDAQAB
-----END PUBLIC KEY-----
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCoQsAzm88drFjEHUZukF4bvLuDQmUJM0kj4xdOO8ws6E3CrHU4
5tLRYfus2gcwUvCsuvy8VN8y5lbNST2wvpRgiRVCHL2tb07gzbez0k2+gBYEe/8p
J8bLL8qtuC498SDN8TX1VDifzvlIugNIH2xIOYbQZK6c/AOPY6sEGgKnowIDAQAB
AoGAbAQuDvN/SrVRZtTEWkYjo/rNBb6hzf42fetTEs4gjNO017yOpDDKNdCJGLX+
127nQnvns59oieyE3NSf3c76wNIY8NIYdqOPe2PKJc99n2crkrpPXgTvANtJXJt3
oDNsKZ4KzXpGFedt8T4bn1dS8bedJ1U7LNojkVLjGAaQNgECQQC5hV6Cy3HZFpI6
6INwd3Le3KrYP6EFpOrLTOMUTSuQVOEb8VAKWrMsZF+Hi0Zo6jNkVBDc/TgHvkdx
Kc3rNylDAkEA6C7B/qd1S4KMRyEa566UnkkDWHqA85CuoRUiLu2C2wBrI+fX1aZV
HTpdaqmsmuS/C7mYCY1DI5VifIerDLfyIQJAIdSnUnSlEzBhhCqIZYbyxJ867GpW
A8B6LI6dzkLwUcaYsk7ECM9XYx3+qaoFMfabXo1R8eqfQBI71vAHpAAQHwJBANy/
H9gilEVfcElsMy1U8Z3wIwsrJZDs3OrvsdlWHZRkOHkhwzYw9zlbtVdkzGNT2kOm
h+OE9/FL5SAqyLjF5qECQA6Owb1DiFENLuJ5hwFEvBtT2SHv+zKB4825A10cZbSs
raB/7YWm+YfnKrywhPuAFmnYp0TwgTsrvVEiWtqqdM4=
-----END RSA PRIVATE KEY-----

In [4]: k.readfile('msg.bin')

In [5]: k.decrypt()
Decrypted message: The rain in Spain falls mainly in the plane.
```

