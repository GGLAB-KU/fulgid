box_0 = ['camera', 'hat', 'starfish']
box_1 = ['blender', 'table', 'dice', 'pen']
box_2 = ['frame', 'glove', 'comb', 'scissors']
box_3 = ['helmet', 'flute']
box_4 = ['tape', 'headphone', 'moon', 'tie', 'perfume']
box_5 = []
box_6 = ['planet']
box_7 = ['cloud']
box_8 = ['towel', 'dress']

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)

# Move the towel and the dress from Box 8 to Box 4
box_4.extend(box_8)
box_8.clear()

# Remove the towel from Box 4
box_4.remove('towel')

# Remove the flute from Box 3
box_3.remove('flute')

# Replace the helmet with the star in Box 3
box_3.append('star')

# Remove the tie and the headphone from Box 4
box_4.remove('tie')
box_4.remove('headphone')

# Remove the dice and the blender from Box 1
box_1.remove('dice')
box_1.remove('blender')

# Replace the table and the pen with the pants and the cat in Box 1
box_1.extend(['pants', 'cat'])
box_1.remove('table')
box_1.remove('pen')

# Swap the perfume in Box 4 with the starfish in Box 0
box_0.remove('starfish')
box_4.remove('perfume')
box_0.append('perfume')
box_4.append('starfish')

# Remove the pants from Box 1
box_1.remove('pants')

# Swap the dress in Box 4 with the cloud in Box 7
box_4.remove('dress')
box_7.remove('cloud')
box_4.append('cloud')
box_7.append('dress')

# Move the planet from Box 6 to Box 2
box_2.append('planet')
box_6.remove('planet')

# Remove the tape and the starfish and the cloud from Box 4
box_4.remove('tape')
box_4.remove('starfish')
box_4.remove('cloud')

# Move the star from Box 3 to Box 2
box_2.append('star')
box_3.remove('star')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)