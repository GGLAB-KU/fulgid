box_0 = ['polish', 'tape', 'elephant', 'mirror']
box_1 = ['desert', 'headphone', 'bag', 'sock', 'branch']
box_2 = ['violin', 'dress', 'dog', 'cloud', 'toaster']
box_3 = ['sculpture']

# Remove mirror and polish from box 0
box_0.remove('mirror')
box_0.remove('polish')

# Swap dress in box 2 with sculpture in box 3
box_2.remove('dress')
box_3.remove('sculpture')
box_2.append('sculpture')
box_3.append('dress')

# Put cat into box 2
box_2.append('cat')

# Remove tape from box 0
box_0.remove('tape')

# Put wallet into box 1
box_1.append('wallet')

# Move cat and sculpture from box 2 to box 0
box_0.append(box_2.pop())
box_0.append(box_2.pop())

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)