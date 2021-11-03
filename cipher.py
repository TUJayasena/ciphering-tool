alphabet = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5","f":"6","g":"7", "h":"8", "i":"9", "j":"10", "k":"11","l":"12", "m":"13", "n":"14","o":"15", "p":"16", "q":"17", "r":"18", "s":"19", "t":"20", "u":"21", "v":"22", "w":"23","x":"24","y":"25","z":"26" }
numbers ={"1":"a", "2":"b", "3":"c", "4":"d", "5":"e","6":"f","7":"g", "8":"h", "9":"i", "10":"j", "11":"k","12":"l", "13":"m", "14":"n","15":"o", "16":"p", "17":"q", "18":"r", "19":"s", "20":"t", "21":"u", "22":"v", "23":"w","24":"x","25":"y","0":"z" }

sentence = input("what do you want to cipher").lower()
cipher_factor = -1
len_sent= len(sentence)
ciphered_sent = ""


for  letter in sentence:
    if int(alphabet.get(letter, '0')) > 0:
         l1= int(alphabet.get(letter))
         l_cipher = str((l1 + cipher_factor)%26)
         new_letter = numbers.get(l_cipher)
    else:
        new_letter = letter
    ciphered_sent = f'{ciphered_sent}{new_letter}'

print(ciphered_sent)