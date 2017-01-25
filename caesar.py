
def alphabet_position(letter):
    """ Assigns number vaule to letter using a list and index postition """
    alpha_upper_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alpha_lower_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    if letter in alpha_lower_list:
        number = alpha_lower_list.index(letter)
        return number
    else:
        number = alpha_upper_list.index(letter)
        return number

def rotate_character(char, rot):
    """ Assigns new character depending on number of rotation """
    alpha_upper_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alpha_lower_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    if char.isalpha()== True:
        char_numb = alphabet_position(char)
        rot_char_numb = (char_numb + rot ) % 26
        if char.isupper() == True:
            new_char = alpha_upper_list[rot_char_numb]
            return new_char
        elif char.islower() == True:
            new_char = alpha_lower_list[rot_char_numb]
            return new_char
    else:
        return char

def encrypt (text, rot):
    encrypted_text = ''
    for eachChar in text:
        newChar = rotate_character(eachChar, rot)
        encrypted_text = encrypted_text + newChar
    return encrypted_text
