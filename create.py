import rc2 as a

key = '645267556B58703272357538782F413F4428472B4B6250655368566D5971337436763979244226452948404D635166546A576E5A7234753778217A25432A462D4A614E645267556B58703273357638792F423F4428472B4B6250655368566D597133743677397A244326462948404D635166546A576E5A723475377821412544'
#key up to 128 bytes
plain_text_msg = 'esto esta encriptadodddddddddddddd sdagdsh sagjd saj s a jhsda dsja dsa'


rc2 = a.RC2(bytearray(key, 'ascii'))
msg = bytearray(plain_text_msg , 'ascii')
encrypted = rc2.encrypt(msg, 0) # 0 -> ECB   1-> CBC

print(encrypted)

f = open("t.html", "w+")

f.write('<p>Este sitio contiene un mensaje secreto</p>\n')
f.write('<div class="rc2" id="'+ str(encrypted) +'"></div>\n')
f.write('<div class="key" id="'+ key +'"></div>')


