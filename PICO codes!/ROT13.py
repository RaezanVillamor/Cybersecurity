# cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}
# ROT13 just wraps back around after 13 letters

def ROT13(word):
    lowerLet = 'abcdefghijklmnopqrstuvwxyz'
    captialLet =  'ABCDEFGHIJKLMONOPQRSTUVWXYZ'
    deciphered = ''
    for i in range(len(word)):
        if word[i].islower():
            print(i)
            print("-")
            print(i % len(word))
        



def main():
    # print("hello")
    ROT13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}")

main()