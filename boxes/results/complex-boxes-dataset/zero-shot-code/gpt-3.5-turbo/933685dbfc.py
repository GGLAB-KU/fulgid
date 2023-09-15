box0 = ['ship', 'pen', 'tie', 'snow', 'tiger']
box1 = ['violin', 'truck']
box2 = []
box3 = []
box4 = ['toothpaste', 'microwave', 'jungle', 'perfume']
box5 = ['blender', 'glove']

# Remove pen, snow, and tiger from box0
box0.remove('pen')
box0.remove('snow')
box0.remove('tiger')

# Move glove and blender from box5 to box4
box4.extend(box5)
box5.clear()

# Move tie from box0 to box5
box5.append('tie')
box0.remove('tie')

# Remove microwave, perfume, and jungle from box4
box4.remove('microwave')
box4.remove('perfume')
box4.remove('jungle')

# Move toothpaste from box4 to box5
box5.append('toothpaste')
box4.remove('toothpaste')

# Put charger and oven into box3
box3.extend(['charger', 'oven'])

# Move toothpaste from box5 to box1
box1.append('toothpaste')
box5.remove('toothpaste')

# Swap oven in box3 with glove in box4
box3[1], box4[1] = box4[1], box3[1]

# Move glove from box3 to box4
box4.append(box3.pop(1))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)