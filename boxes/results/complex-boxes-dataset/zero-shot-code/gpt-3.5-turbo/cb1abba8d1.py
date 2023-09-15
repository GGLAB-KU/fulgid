box0 = ['fish', 'drum']
box1 = ['tie']
box2 = ['battery', 'shampoo', 'book', 'soap']
box3 = ['blanket', 'umbrella', 'submarine', 'wig', 'whistle']
box4 = []

# Move the soap and the battery from Box 2 to Box 1
box1.extend(box2.pop(box2.index('soap')))
box1.extend(box2.pop(box2.index('battery')))

# Move the wig from Box 3 to Box 2
box2.extend(box3.pop(box3.index('wig')))

# Remove the shampoo and the book from Box 2
box2.remove('shampoo')
box2.remove('book')

# Remove the wig from Box 2
box2.remove('wig')

# Empty Box 1
box1 = []

# Put the comet into Box 0
box0.append('comet')

# Put the button and the rock and the glasses into Box 0
box0.extend(['button', 'rock', 'glasses'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)