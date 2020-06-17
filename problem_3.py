import sys
global huffman

def huffman_encoding(data):
    huffman = {}
    huffmantree = {}
    for str in data:
        huffman[str] = huffman.get(str, 0) + 1
    sub = '1'
    for item in sorted(huffman.items(), key = lambda x: x[1]):
        huffmantree[item[0]] = sub
        sub = '0' + sub
    encoded = ''
    for str in data:
        encoded += huffmantree[str]
    return  encoded, huffmantree



def huffman_decoding(data,tree):
    huffman = {}
    for node in tree:
        huffman[tree[node]] = node
    sub = ''
    decoded = ''
    for str in data:
        if str != '1':
            sub +=str
        else:
            decoded += huffman[sub+str]
            sub = ''
    return decoded

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))