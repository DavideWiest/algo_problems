
bits = "abcdef"

def reversebits(bits):
    rev = [bits[len(bits)-index-1] for index in range(len(bits))]
    return "".join(rev)

print(reversebits(bits))