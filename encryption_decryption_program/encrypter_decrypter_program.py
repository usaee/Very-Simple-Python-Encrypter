
L = []
L2 = {':':30 , '\\':31 , '/':32 , '-':33 , '_':34 , '.':35 , ' ':80 , '!':81 , '\'':82}
for i in range(10):
    k = str(i)
    L2[k] = (i + 36)

alpha = 'a'
for i in range(0, 26): 
    L2[alpha] = (i+3)
    alpha = chr(ord(alpha) + 1)

alpha2 = 'A'
for i in range(40, 66): 
    L2[alpha2] = (i+3)
    alpha2 = chr(ord(alpha2) + 1)

##########################################################################
# Encryption
##########################################################################
def e():
    global L2
    newL = str()
    f = open('decrypted.txt','r')
    rfl = f.readlines()
    f.close()

    if rfl:
        f = open('encrypted.txt','a')
        
        for dx, i in enumerate(rfl):
            j = str(i)
            for ch in j:
                k = ch
                newL += (str((L2.get(k))) + ' ')
            newL = newL.split('None')[0]
            f.write(newL + '\n')
            newL = str()

        f.close()
        f = open('decrypted.txt','w') # Clears all un-encrypted data
        f.close()
    else:
        print("Nothing to encrypt")
        input("Press the Enter key to exit . . .")

##########################################################################
# Decryption
##########################################################################
def d():
    global L2
    newL = str()
    new_line2 = str()
    f = open('encrypted.txt','r')
    rfl = f.readlines()
    f.close()
    if rfl:
        f = open('decrypted.txt','a')

        for dx, i in enumerate(rfl):
            j = i
            try:
                j = j.split('\n')[0]
            except:
                pass

            new_line = j.split()
            for ch in new_line:
                ch2 = int(ch)
                for j2 in L2.items():
                    if int(j2[1]) == ch2:
                        new_line2 += j2[0]
            f.write(new_line2 + '\n')
            new_line2 = str()

        f.close()
        f = open('encrypted.txt','w') # Clears all encrypted data
        f.close()
    else:
        print('Nothing to decrypt')
        input("Press the Enter key to exit . . .")

##########################################################################
# User Input
##########################################################################
enc_dec = input('Encrypt (OR) Decrypt (e/d): ')
if enc_dec == 'e':
    e()
else:
    d()




























