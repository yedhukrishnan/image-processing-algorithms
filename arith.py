# Arthmetic Coding

word = raw_input('Enter the string to encode and decode: ')

unique_letters = list(set(list(word)))
unique_letters.sort()

count = {}
for letter in word:
    if letter not in count.keys():
        count.update({ letter: 1 })
    else:
        count[letter] += 1

length = float(len(word))
probabilities = {}

for letter in unique_letters:
    probabilities.update({ letter: count[letter] / length })

first_letter = unique_letters[0]
cdf = { first_letter: probabilities[first_letter] }

for i in range(1, len(unique_letters)):
    letter = unique_letters[i]
    previous_letter = unique_letters[i - 1]
    cdf_value = probabilities[letter] + cdf[previous_letter]
    cdf.update({ letter: cdf_value })

previous_l, previous_u = 0, 1

for current_letter in word:
    current_letter_index = unique_letters.index(current_letter)
    previous_letter_cdf_value = 0
    if current_letter_index > 0:
        previous_letter = unique_letters[current_letter_index - 1]
        previous_letter_cdf_value = cdf[previous_letter]

    l = previous_l + (previous_u - previous_l) * previous_letter_cdf_value
    u = previous_l + (previous_u - previous_l) * cdf[current_letter]

    previous_l, previous_u = l, u

tag = (l + u) / 2.0

print "Cumulative Density: ", cdf
print "Tag: ", tag

# Decoding

print "Decoded Letters: "

previous_l, previous_u = 0, 1
for i in range(len(word)):
    new_tag = (tag - previous_l) / (previous_u - previous_l)

    if new_tag <= cdf[unique_letters[0]]:
        letter = unique_letters[0]
        print letter
    else:
        for j in range(1, len(unique_letters)):
            if cdf[unique_letters[j - 1]] <= new_tag <= cdf[unique_letters[j]]:
                letter = unique_letters[j]
                print letter
                break

    letter_index = unique_letters.index(letter)	
    if letter_index > 0:
        previous_letter = unique_letters[letter_index - 1]
        previous_letter_cdf = cdf[previous_letter]
    else:
        previous_letter_cdf = 0

    current_letter_cdf = cdf[letter]
    l = previous_l + (previous_u - previous_l) * previous_letter_cdf
    u = previous_l + (previous_u - previous_l) * current_letter_cdf
    previous_l, previous_u = l, u
	
