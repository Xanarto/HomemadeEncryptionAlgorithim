import base64

e = "My_0wn_C1ph3r_T0_3ncrypt_Stuff_Mys3lf!,.EH7sg"

def encrypt(message : str):
    z = ([ord(str(x)) for x in base64.b64encode(message.encode('utf-8')).decode('utf-8')] + [ord("z")])[::-1]
    return "".join(map(str,[chr(x * 3) for x in [x + y for (x,y) in (zip(z[::2], z[1::2]))]]))

print(encrypt(e))