box_0 = ['bowl', 'keyboard']
box_1 = ['sandals']
box_2 = ['microscope', 'shelf', 'sun', 'coat', 'dog']
box_3 = ['rain']
box_4 = ['drum', 'headphone', 'plane', 'camera']
box_5 = []

# Put the toy into Box 2
box_2.append('toy')

# Put the polish and the cloud and the sock into Box 2
box_2.extend(['polish', 'cloud', 'sock'])

# Put the plane and the thread into Box 3
box_3.extend(['plane', 'thread'])

# Put the freezer and the bear and the umbrella into Box 0
box_0.extend(['freezer', 'bear', 'umbrella'])

# Swap the umbrella in Box 0 with the cloud in Box 2
box_0.remove('umbrella')
box_2.remove('cloud')
box_0.append('cloud')
box_2.append('umbrella')

# Replace the sandals with the necklace in Box 1
box_1.remove('sandals')
box_1.append('necklace')

# Swap the plane in Box 3 with the headphone in Box 4
box_3.remove('plane')
box_4.remove('headphone')
box_3.append('headphone')
box_4.append('plane')

# Put the octopus and the coral and the plate into Box 4
box_4.extend(['octopus', 'coral', 'plate'])

# Swap the coral in Box 4 with the necklace in Box 1
box_4.remove('coral')
box_1.remove('necklace')
box_4.append('necklace')
box_1.append('coral')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)