# this script is going to decrypt caesar cipher by brute force
# ---- Limitations
# ---- encrypted text is received as input
# ---- Works only for A to Z
# ---- Key space size is fixed at 26

def decrypt(text, key):
    msg = ""
    for ele in text:
        if ele == " ":
            msg = msg + ele
        else:
            if ele.isupper():
                a = (((ord(ele) - 65) + 26 - key) % 26) + 65
            else:
                a = (((ord(ele) - 97) + 26 - key) % 26) + 97
            msg = msg + chr(a)
    return msg


cipher_text = raw_input("Enter cipher text: ")
print("Given cipher text : " + cipher_text)
n = 26
while n > 0:
    ans = decrypt(cipher_text, n)
    print("Plain text maybe : " + ans)
    n = n - 1
