import base64

_test_message = "Xanarto's_0wn_C1ph3r_T0_3ncrypt_Stuff_H1ms3lf!,.EH7sg"

def encrypt(message : str):
    z = ([ord("z")] + [ord(str(x)) for x in base64.b64encode(message.encode('utf-8')).decode('utf-8')])[::-1]
    return "".join(map(str,[chr(x * 2) for x in [int(str(x) + str(y)) for (x,y) in (zip(z[::2], z[1::2]))]]))

if __main__ == "__name__":
    print(encrypt(test_message))
