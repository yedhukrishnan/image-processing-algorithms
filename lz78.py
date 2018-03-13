# LZ78 encoding

def codeword(letter):
    # Return the ASCII value of the letter
    return ord(letter)

def decode(code):
    # Return the letter corresponding to the ASCII value
    return chr(code)

# sentence = 'wabba wabba wabba wabba woo woo woo'
sentence = raw_input('Enter the string to encode and decode: ')

# Encoding

# Define an empty dictionary with empty string at index position 1
# Our dictionary index starts from 1
dictionary = ['']

encoded = []

print "\n"
print "Code \t\tIndex \tEntry"
print "-----------------------------"

i = 0
while i < len(sentence):
    j = i
    i = i + 1

    # If this is the last letter, just encode the letter
    if j == len(sentence) - 1:
        encoded.append((0, codeword(sentence[j])))

    combined = ''
    while j < len(sentence):
        next_letter = sentence[j]
        if combined + next_letter not in dictionary:
            dictionary.append(combined + next_letter)
            encoded.append((dictionary.index(combined), codeword(next_letter)))

            print dictionary.index(combined), "\t", codeword(next_letter), "\t",
            print dictionary.index(combined + next_letter), "\t", (combined + next_letter)
            # Change i to j + 1 to start from the next letter
            i = j + 1
            break
        else:
            combined = combined + next_letter

        j = j + 1


print "\n"
print "Encoded String: ", encoded

# Decoding

dictionary = ['']

decoded = ''

for (code, codeword) in encoded:
    string = dictionary[code] + decode(codeword)
    dictionary.append(string)
    decoded += string

print decoded
