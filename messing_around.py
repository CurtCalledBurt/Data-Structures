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

# for elem in arr:
#     if elem % 3 == 0:
#         print(elem)


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
# # twelve

# {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
# "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, }









class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

count = 0
pointer = node1
middle = node1

while pointer.next:
  if count % 2 == 1:
    middle = middle.next
  pointer = pointer.next
  count += 1

print(middle.value)



print("\n\n")



pointer = node1

prev_n = None
while pointer:
  next_n = pointer.next
  pointer.next = prev_n
  prev_n = pointer
  pointer = next_n
  if prev_n.next:
    print(prev_n.value, " Next: ", prev_n.next.value)
  else:
    print(prev_n.value, " Next: ", prev_n.next)



# pointer = node1
# while pointer:
#   if pointer is node1:
#     old_node = pointer
#     pointer.next = None
#   else:
#     pointer.next = old_node.next
#     old_node = pointer
#   pointer = old_node.next

# while pointer:
#   print(pointer.value)
#   pointer = pointer.next


# node = node1
# pre = None
# while node != None:
#   temp = node.next
#   node.next = pre
#   pre = node
#   node = temp
#   print(pre.value)