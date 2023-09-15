box_0 = ['octopus', 'car']
box_1 = ['pillow', 'toy', 'bear']
box_2 = ['shampoo', 'toothpaste']
box_3 = ['glasses', 'cloud', 'starfish', 'chair']
box_4 = ['charger', 'ship', 'laptop', 'toaster']
box_5 = ['usb']
box_6 = ['grinder', 'button', 'harmonica', 'mirror']
box_7 = ['microwave', 'shorts', 'glove', 'thunder', 'jacket']
box_8 = ['island', 'coat']
box_9 = ['grass', 'pants']
box_10 = ['lion', 'seaweed', 'tape', 'bird']

# Remove usb from Box 5
box_5.remove('usb')

# Swap harmonica in Box 6 with seaweed in Box 10
box_6.remove('harmonica')
box_10.remove('seaweed')
box_6.append('seaweed')
box_10.append('harmonica')

# Empty Box 10
box_10 = []

# Empty Box 1
box_1 = []

# Replace island and coat with cat and perfume in Box 8
box_8.remove('island')
box_8.remove('coat')
box_8.append('cat')
box_8.append('perfume')

# Replace glasses, cloud, and chair with vase, shoes, and wig in Box 3
box_3.remove('glasses')
box_3.remove('cloud')
box_3.remove('chair')
box_3.append('vase')
box_3.append('shoes')
box_3.append('wig')

# Swap shoes in Box 3 with toaster in Box 4
box_3.remove('shoes')
box_4.remove('toaster')
box_3.append('toaster')
box_4.append('shoes')

# Swap grinder in Box 6 with octopus in Box 0
box_6.remove('grinder')
box_0.remove('octopus')
box_6.append('octopus')
box_0.append('grinder')

# Swap grass in Box 9 with car in Box 0
box_9.remove('grass')
box_0.remove('car')
box_9.append('car')
box_0.append('grass')

# Swap mirror in Box 6 with cat in Box 8
box_6.remove('mirror')
box_8.remove('cat')
box_6.append('cat')
box_8.append('mirror')

# Remove starfish and wig from Box 3
box_3.remove('starfish')
box_3.remove('wig')

# Swap grinder in Box 0 with vase in Box 3
box_0.remove('grinder')
box_3.remove('vase')
box_0.append('vase')
box_3.append('grinder')

# Put mirror, dice, and earring into Box 2
box_2.append('mirror')
box_2.append('dice')
box_2.append('earring')

# Replace jacket with controller in Box 7
box_7.remove('jacket')
box_7.append('controller')

# Put pen and glasses into Box 0
box_0.append('pen')
box_0.append('glasses')

# Move mirror from Box 8 to Box 7
box_8.remove('mirror')
box_7.append('mirror')

# Replace perfume with tie in Box 8
box_8.remove('perfume')
box_8.append('tie')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)