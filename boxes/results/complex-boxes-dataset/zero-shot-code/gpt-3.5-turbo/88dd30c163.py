box0 = ['oven']
box1 = ['speaker', 'soap', 'bracelet']
box2 = ['tape', 'forest', 'basket', 'elephant', 'butterfly']
box3 = ['note', 'cloud', 'comet', 'fish']
box4 = []

# Replace fish with branch in Box 3
box3.remove('fish')
box3.append('branch')

# Move oven from Box 0 to Box 3
box0.remove('oven')
box3.append('oven')

# Empty Box 3
box3 = []

# Replace basket and forest with helmet and pants in Box 2
box2.remove('basket')
box2.remove('forest')
box2.append('helmet')
box2.append('pants')

# Move soap, bracelet, and speaker from Box 1 to Box 4
box4.extend(box1)
box1 = []

# Move pants, helmet, and elephant from Box 2 to Box 3
box3.extend(box2[2:])
box2 = box2[:2]

# Move pants and helmet from Box 3 to Box 2
box2.extend(box3[:2])
box3 = box3[2:]

# Put shoes and blender into Box 3
box3.extend(['shoes', 'blender'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)