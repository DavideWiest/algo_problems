from string import ascii_lowercase

with open("data/codedtrianglenumbers_words.txt", "r") as f:
    words = [word[1:-1].lower() for word in f.read().split(",")]

triangleNums = [ 0.5 * n * (n+1) for n in range(100) ]

count = len([
    word for word in words if sum(ascii_lowercase.index(char)+1 for char in word) in triangleNums
    ])

print(count)