import ascii_art

print(ascii_art.logo)

def encoder(message, shift_num):
    modified_message = ""
    for ch in message:
        if (ord(ch)>=65 and ord(ch)<=90):
            modified_message += chr(ord(ch)+shift_num) if ord(ch)+shift_num<=90 else chr(ord(ch)+shift_num-26)
        elif (ord(ch)>=97 and ord(ch)<=122):
            modified_message += chr(ord(ch)+shift_num) if ord(ch)+shift_num<=122 else chr(ord(ch)+shift_num-26)
        else:
            modified_message+=ch
    return modified_message
    


def decoder(message, shift_num):
    modified_message = ""
    for ch in message:
        if (ord(ch)>=65 and ord(ch)<=90):
            modified_message += chr(ord(ch)-shift_num) if ord(ch)-shift_num>=65 else chr(ord(ch)-shift_num+26)
        elif (ord(ch)>=97 and ord(ch)<=122):
            modified_message += chr(ord(ch)-shift_num) if ord(ch)-shift_num>=97 else chr(ord(ch)-shift_num+26)
        else:   
            modified_message+=ch
    return modified_message

ask = "Yes"

while ask.lower() == "yes" or ask.lower() == "y":
    func = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ")
    shift_num = int(input("Type the shift number: "))%26
    modified_message = ""
    if func.lower() == "encode" or func.lower() == "e":
        print("Here's the encoded result: ",encoder(message, shift_num))
    elif func.lower() == "decode" or func.lower() == "d":
        print("Here's the decoded result: ",decoder(message,shift_num))
    else:
        print("No such functionality available")
    ask = input("Type 'yes' if you would want to go again. Otherwise type'no': ")


