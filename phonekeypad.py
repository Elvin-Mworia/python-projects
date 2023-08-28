MAPPING=('0', '1', 'ABC', 'DEF', 'GHI', 'lKL', 'llNO', 'PQRS', 'TUV', 'IJXYZ')
number=input("Enter a seven digit number from 0-9: ")
phone_number=number.strip()

if (not phone_number.isdigit()):
     print("not all numbers are valid digits")
     exit(-1)

def phone_mnemonic(phone_number) :
    def phone_mnemonic_helper (digit):
        if digit == len(phone_number):
        # All digits are processed, so add partial_nnenonic to mnenonics.
        # (We add a copy since subsequent calls nodify partial_mnenonic.)
            mnemonics.append("". join(partial_mnemonic))
        else:
        # Try all 77 possible characters for this digit
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit]= c
                phone_mnemonic_helper(digit + 1)
                
    mnemonics, partial_mnemonic = [] , [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

print(phone_mnemonic(phone_number))