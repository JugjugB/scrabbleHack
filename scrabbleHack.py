with open("legalWords.txt") as f:
  lines = f.read().splitlines()
userLetters = ['s', 'q', 'u', 'a', 'r', 'e']
for i in range(len(userLetters)):
  tempLetters = userLetters[:i+1]

