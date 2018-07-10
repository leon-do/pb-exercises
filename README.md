# Pre-Requisites

Install python 3.5 or above on your machine:

 * Windows: https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64.exe
 * Mac OS X: https://www.python.org/ftp/python/3.6.2/python-3.6.2-macosx10.6.pkg
 * Linux: see your distro docs

Install pip:

Download this script: https://bootstrap.pypa.io/get-pip.py

Run (you may need to specify python3 if you also have python2 installed)

    $ python get-pip.py

Install git:

https://git-scm.com/downloads

Install virtualenv:

    $ pip install virtualenv

# Download pb-exercises requirements

    $ git clone https://github.com/jimmysong/pb-exercises
    $ cd pb-exercises
    $ virtualenv -p python3 .venv

Linux/OSX:

    $ . .venv/bin/activate
    (.venv) $ pip install -r requirements.txt

Windows:

    > .venv\Scripts\activate.bat
    > pip install -r requirements.txt

# Run jupyter notebook

    (.venv) $ jupyter notebook


# Notes
- BTC ec equation
    - G = (x,y)
    - y**2 = x**3 + 7
    - p = 2**256 - 2**32 - 977
    - y**2 % p == (x**3 + 7) % p
- Fermat's Little Theorm
- secp256k1 is the ec used for btc
- calculate 3rd point intercept
    - ec equation: y**2 = x**3 + ax + b
    - given (x1, y1) and (x2, y2), find (x3, y3)
    - x3 = s**2 - x1 - x2
    - y3 = s * (x1-x3) - y1
- if point is tangent to ec
    - ec equation: y**2 = x**3 + ax + b
    - derive equation to get slope: s = (3x**2 + a)/y
    - x3 = s**2 - 2x
- pubkey to address
    - from helper import encode_base58, hash160, double_sha256
    - sec = bytes.fromhex('025CBDF0646E5DB4EAA398F365F2EA7A0E3D419B7E0330E39CE92BDDEDCAC4F9BC')
        - this is the pub key with 02 prefix
        - 02 prefix means the x coordinate is even
    - h160 = hash160(sec)
    - raw = b"\x00" + h160
    - raw = raw + double_sha256(raw)[:4]
    - addr = encode_base58(raw)
    - print(addr)
