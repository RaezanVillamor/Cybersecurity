# cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}
# ROT13 just wraps back around after 13 letters
from collections import Counter # Helpful class, see documentation or help(Counter)
import re
def ROT13(ciphertext):
    dictionary = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}
    
    deciphered = ''
    for i in range(len(ciphertext)):
        if ciphertext[i].isupper():
            upperLetter = ciphertext[i]
            upperLetter =upperLetter.lower()
            print(upperLetter)
            getLetter = dictionary[upperLetter]
            deciphered += getLetter.upper()
        elif ciphertext[i].islower():
            getLetter =dictionary[ciphertext[i]]
            deciphered += getLetter
        else:
            deciphered += ciphertext[i]
    print(deciphered)



def main():
    # print("hello")
    ROT13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}")

main()