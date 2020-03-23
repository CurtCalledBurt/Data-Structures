# Print out all of the numbers in the following array that are divisible by 3:
arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 8
# 27
# 99
# 63
# 42

for elem in arr:
    if elem % 3 == 0:
        print(elem)


# Print out all of the strings in the following array that represent a number divisible by 3:
arr2 = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen",
]
# The expected output for the above input is:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve