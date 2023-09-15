box0 = []
box1 = ['fish', 'cup', 'toy']
box2 = ['telescope', 'dress', 'fork', 'shark']
box3 = []
box4 = ['pot', 'swimsuit', 'razor', 'sun', 'soap']

# Swap the toy in Box 1 with the sun in Box 4
box1[2], box4[3] = box4[3], box1[2]

# Move the fish from Box 1 to Box 2
box2.append(box1.pop(0))

# Swap the toy in Box 4 with the fish in Box 2
box4[2], box2[3] = box2[3], box4[2]

# Move the razor from Box 4 to Box 0
box0.append(box4.pop(2))

# Remove the pot and the soap from Box 4
box4.remove('pot')
box4.remove('soap')

# Remove the shark from Box 2
box2.remove('shark')

# Remove the dress and the fork from Box 2
box2.remove('dress')
box2.remove('fork')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)