def main():
  book = open("books/frankenstein.txt", "r")
  totalWords = 0
  charDict = generateCharDict()
  for line in book:
    totalWords += len(line.split())
    #for char in line:
    for letter in line.lower():
      if letter.isalpha():
        charDict[letter] += 1
  for letterCount in charDict:
    print(f"The '{letterCount}' character was found {charDict[letterCount]} times")

def generateCharDict():
  charDict = {}
  alphabet = list(map(chr, range(97, 123)))
  for letter in alphabet:
    charDict[letter] = 0
  return charDict

if __name__ == "__main__":
  main()