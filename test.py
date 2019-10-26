import AES256,base64
def H_To_Str(h):
    string = ""
    for i in h:
        string += chr(i)
    return string

key = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
key = bytearray.fromhex(key)
msg = '00112233445566778899aabbccddeeff'
msg = bytearray.fromhex(msg)
print("msg: ", msg)

cipher = AES256.encrypt(msg,key,"ECB","")
print ("cipher: ",cipher)
AES256.test(cipher)

plain = AES256.decrypt(cipher,key,"ECB","")
#print("plain: ",H_To_Str(plain))
AES256.test(plain)