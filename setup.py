import os
from setuptools import setup, find_packages
import pathlib


def read(fname):
  try:
    with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
      return fh.read()
  except IOError:
    return ''

#requirements = read('requirements.txt').splitlines()
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')



setup(name='telmsRSA',
  version='0.0.1',
  description='Python RSA Implementation Library: Feature Key Creation, Key Reading, Message encryption and decryption',
  url='https://github.com/g00364778/rsa',
  author='Jattie van der Linde',
  author_email='g00364778@gmit.ie',
  license='Apache License, Version 2.0',
  packages=find_packages(where='.', exclude=(), include=('*',)), # find_packages(where='rsa'),
  package_data={  # Optional
    'rsa': ['msg.txt','msg.bin','keyRSA.pri','keyRSA.pub'],
  },
  #py_modules=['lib_rsa','rsa_lib','mac'],
  #data_files=[('lib/site-packages', ['msg.txt'])],  # Optional
  #packages=['lib_rsa','rsa_lib'],
  #package_data={
  #  '': ['lib_rsa.py','rsa_lib.py','keyRSA.pri','keyRSA.pub','msg.bin','msg.txt']
  #},
  zip_safe=False,
  python_requires='>=3.5, <4',
  #install_requires=requirements,
  )