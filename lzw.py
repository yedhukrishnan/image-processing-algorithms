# sentence = "wabba wabba wabba wabba woo woo woo"
# sentence = 'a bar array by barryar bay'
# sentence = 'woo woo'

sentence = raw_input('Enter string to encode and decode: ')

dictionary = [0]

print 'Index\tEntry\tEncoded Symbol'

for letter in sentence:
    if letter not in dictionary:
        dictionary.append(letter)
        print dictionary.index(letter), "\t", letter

dictionary.sort()

initial_dictionary = dictionary[:]

# Encoding

encoded = []

i = 0
while i < len(sentence):
    letter = sentence[i]

    if i <= len(sentence) - 1:
        j = i + 1

    combined = letter
    i = i + 1
    while j < len(sentence):
        next_letter = sentence[j]
        combined = combined + next_letter
        j = j + 1
        if combined not in dictionary:
            dictionary.append(combined)
            print dictionary.index(combined), "\t", combined,
            i = j - 1
            break;

    word = combined[0:len(combined)-1]
    if word in dictionary:
        encoded.append(dictionary.index(word))
        print "\t", dictionary.index(word)

# Encode the last remaining symbol
encoded.append(dictionary.index(combined[-1]))
print "\t\t", dictionary.index(combined[-1])

print "Encoded string: ", encoded

# Decoding

dictionary = initial_dictionary[:]
decoded_string = ''

previous_decoded = ''
for code in encoded:
    decoded = dictionary[code]

    decoded_string += decoded

    combined = previous_decoded + decoded[0]

    if combined not in dictionary:
        dictionary.append(combined)

    previous_decoded = decoded

print "Decoded String: ", decoded_string
