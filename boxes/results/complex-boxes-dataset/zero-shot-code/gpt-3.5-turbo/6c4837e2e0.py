box_0 = ['flower']
box_1 = ['meteor']
box_2 = ['needle', 'freezer', 'lipstick', 'octopus', 'glove']
box_3 = ['charger', 'table', 'comet']
box_4 = ['fork']
box_5 = ['camera', 'bracelet', 'car']
box_6 = ['laptop']

# Move the meteor from Box 1 to Box 2
box_2.append(box_1.pop(0))

# Remove the meteor and the freezer and the lipstick from Box 2
box_2.remove('meteor')
box_2.remove('freezer')
box_2.remove('lipstick')

# Replace the fork with the puzzle in Box 4
box_4.remove('fork')
box_4.append('puzzle')

# Swap the camera in Box 5 with the table in Box 3
box_5.remove('camera')
box_3.remove('table')
box_5.append('table')
box_3.append('camera')

# Move the flower from Box 0 to Box 1
box_1.append(box_0.pop(0))

# Put the shampoo into Box 2
box_2.append('shampoo')

# Swap the glove in Box 2 with the flower in Box 1
box_2.remove('glove')
box_1.remove('flower')
box_2.append('flower')
box_1.append('glove')

# Replace the glove with the skirt in Box 1
box_1.remove('glove')
box_1.append('skirt')

# Move the charger and the comet from Box 3 to Box 0
box_0.append(box_3.pop(0))
box_0.append(box_3.pop(0))

# Put the desert into Box 2
box_2.append('desert')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)