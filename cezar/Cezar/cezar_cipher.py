import string

def encrypt_3(text):
    """Cezar cipher (classic version) """
    text = text.upper()
    result = ''
    for i in range(len(text)):
        if text[i] in list(string.ascii_uppercase):
            result += ''.join(chr((65+(ord(text[i])-62)%26)))
        elif text[i] == ' ':
            result += ''.join(text[i])
        else:
            raise ValueError('Right now encrypt allow only letters (A-Z)' \
                              ' please provide one.') 
    return result
 
def decrypt_3(text):
    """Cezar cipher classic decryptor"""
    text = text.upper()
    result = ''
    for i in range(len(text)):
        if text[i] in list(string.ascii_uppercase):
            result += ''.join(chr((65+(ord(text[i])-42)%26)))
        elif text[i] == ' ':
            result += ''.join(text[i])
        else:
            raise ValueError('Right now encrypt allow only letters (A-Z)' \
                              ' please provide one.') 
    return result
        
def encrypt_13(text):
    """Cezar cipher with ROT13"""
    text = text.upper()
    result = ''
    for i in range(len(text)):
        if text[i] in list(string.ascii_uppercase):
            result += ''.join(chr((65+(ord(text[i])-52)%26)))
        elif text[i] == ' ':
            result += ''.join(text[i])
        else:
            raise ValueError('Right now encrypt allow only letters (A-Z)' \
                              ' please provide one.') 
    return result


