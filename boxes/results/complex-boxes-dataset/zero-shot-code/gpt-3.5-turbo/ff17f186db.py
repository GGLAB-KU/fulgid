box0 = []
box1 = ['coral', 'cup']
box2 = []
box3 = ['bracelet', 'key', 'lock', 'bowl']

# Move the river from Box 1 to Box 0
box0.append('river')
box1.remove('coral')
box1.remove('cup')

# Put the toy into Box 0
box0.append('toy')

# Put the boot and the watch and the bus into Box 3
box3.extend(['boot', 'watch', 'bus'])

# Put the fish and the beach and the fridge into Box 2
box2.extend(['fish', 'beach', 'fridge'])

# Replace the cup and the coral with the toothbrush and the coat in Box 1
box1.remove('cup')
box1.remove('coral')
box1.extend(['toothbrush', 'coat'])

# Put the dress and the crown into Box 1
box1.extend(['dress', 'crown'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)