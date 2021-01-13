##############################################
# DESCRIPTION : Format Based Steganography  #
#   Algorithm : Open space encoding         #
# Author      : Kishore                     #
##############################################

def to_ascii(charector):
    # a method to convert charector into ascii int
    assert type(charector) == str
    return ord(charector)

def to_str(ascii):
    # a method to convert ascii int into ascii char
    assert type(ascii) == int
    return chr(ascii)

def to_binary(ascii):
    # a method to convert ascii int into binary string value
    assert type(ascii) == int
    return "{0:08b}".format(ascii)

def to_int(binary):
    # a method to convert binary string value into ascii int
    assert type(binary) == str
    return int(binary, 2)

def encode_handling(file_name, binary, encoded_file_name = 'none'):
    # a method to take file name and binary string with opetional encoding file name
    # returns a binary string value and optional text file for encoding .

    opener = open(file_name)
    file = opener.read().splitlines()
    sentences = [file[i].split(' ') for i in range(len(file))] 
    words = ''
    count = 0
    length_of_binary = len(binary)
    for row in range(len(file)):
        for col in range(len(sentences[row])):
            try:
                words+=sentences[row][col]
                if count>=length_of_binary:
                    pass
                elif int(binary[count]) == 1:
                    words+='  '
                else:
                    words+=' ' 
                count+=1
            except:
                print(count, ' this is problem.',length_of_binary)
    opener.close()
    if encoded_file_name  != 'none':
        encoded_file = open(encoded_file_name, 'w')
        encoded_file.write(words)
        encoded_file.close()
    return binary

def decode_handling(encoded_file_name): 
    #  a method to open encoded file and return binary string value of hidden text
    file = open(encoded_file_name)
    read = file.read()
    binary = ''
    prev = False
    for i in range(1, len(read)-1):
        if read[i]==' ' and read[i+1]==' ':
            i+=1
            binary+='1'
            prev = True
            continue
        elif read[i]==' ':
            if prev:
                prev=False
                continue
            else:
                binary+='0'
        else:
                pass
    return binary

def encode():
    binary_sentence = ''
    ascii_sentence = []
    sentence = input('Enter the sentence you want to Encode : ')
    # sentence to ASCII
    for i in iter(sentence):
        ascii_sentence.append(to_ascii(i))
    assert type(ascii_sentence)==list

    # ASCII to Binary
    for i in ascii_sentence:
        binary_sentence+=to_binary(i)      
    
    # File Handling
    file_name = input(" Enter the file to encrypt : ")
    encoded_file_name = input("Enter the file name of encoded text to save as : ")
    encode_binary = encode_handling(file_name= file_name,binary=binary_sentence,encoded_file_name= encoded_file_name)

def decode():
    decoded_sentences = ''
    # decode Method Handling
    encoded_file_name = input('Enter the file name to decrypt : ')
    decode_binary = decode_handling(encoded_file_name= encoded_file_name)

    # Binary to ASCII
    int_sentence = []
    for i in range(0,len(decode_binary)-8,8):
        if to_int(decode_binary[i:i+8]) == 0:
            break
        else:
            int_sentence.append(to_int(decode_binary[i:i+8]))
    int_sentence.append(to_int(decode_binary[len(decode_binary)-8:]))

    # forming sentences
    for i in int_sentence:
        try:
            decoded_sentences+=to_str(i)
        except:
            print(int_sentence[1], ' is out of range for chr().')
            break
    print("output after decoding is ", decoded_sentences)

def main():
    session = input('Enter 1 to encode or 2 to decode : ')
    

    # call encode
    if session == '1':
        encode()
    elif session == '2':
        decode()
    else:
        main()

        
if __name__ == "__main__":
    main()
