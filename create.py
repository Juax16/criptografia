import rc2 as a 
#rc4.py debe estar en el mismo directorio que este archivo

key = 'estaEsUnaLLave'
#key up to 128 bytes
plain_text_msg = 'mi mensaje a encriptar'

rc2 = a.RC2(bytearray(key, 'ascii'))
msg = bytearray(plain_text_msg , 'ascii')
encrypted = rc2.encrypt(msg, 0) # 0 -> ECB   1-> CBC

f = open("index.html", "w+")

f.write('<p>Este sitio contiene un mensaje secreto</p>\n')
f.write('<div class="rc2" id="'+ str(encrypted) +'"></div>\n')
f.write('<div class="key" id="'+ key +'"></div>')


