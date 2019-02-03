# Huffman Encoding

def huffman(probabilities):
    if(len(probabilities) == 2):
        return dict(zip(probabilities.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_copy = probabilities.copy()
    a1, a2 = lowest_prob_pair(probabilities)
    p1, p2 = p_copy.pop(a1), p_copy.pop(a2)
    p_copy[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_copy)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(probabilities):
    sorted_p = sorted(probabilities.items(), key=lambda (i,pi): pi)
    return sorted_p[0][0], sorted_p[1][0]

ex2 = { 'a': 0.25, 'b': 0.25, 'c': 0.2, 'd': 0.15, 'e': 0.15 }
print('Input: ')
print(ex2)
print('Output: ')
print huffman(ex2)  # => {'a': '01', 'c': '00', 'b': '10', 'e': '110', 'd': '111'}
