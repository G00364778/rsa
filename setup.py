import os
from setuptools import setup

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

#requirements = read('requirements.txt').splitlines()

setup(name='pyRSAImplementation',
      version='0.0.1',
      description='Python RSA Implementation Library: Feature Key Creation, Key Reading, Message encryption and decryption',
      url='https://github.com/g00364778/rsa',
      author='Jattie van der Linde',
      author_email='g00364778@gmit.ie',
      license='Apache License, Version 2.0',
      packages=['lib_rsa.py','rsa_lib.py','keyRSA.pri','keyRSA.pub','msg.bin','msg.txt'],
      #package_data={
      #  'pyAudioAnalysis': ['data/models/*']
      #},
      zip_safe=False,
      #install_requires=requirements,
      )