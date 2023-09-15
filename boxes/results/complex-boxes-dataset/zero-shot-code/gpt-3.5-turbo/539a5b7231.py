box_0 = ['bell', 'violin', 'bus', 'coin']
box_1 = ['sculpture', 'belt', 'microwave', 'rock', 'seaweed']
box_2 = ['controller']
box_3 = ['storm']
box_4 = ['magnet', 'thunder', 'blanket', 'dice', 'truck']
box_5 = ['river', 'forest', 'rocket', 'comet']
box_6 = ['pillow']

# Swap the comet in Box 5 with the rock in Box 1
box_1.remove('rock')
box_1.append('comet')
box_5.remove('comet')
box_5.append('rock')

# Remove the river and the forest from Box 5
box_5.remove('river')
box_5.remove('forest')

# Remove the controller from Box 2
box_2.remove('controller')

# Swap the pillow in Box 6 with the truck in Box 4
box_4.remove('truck')
box_4.append('pillow')
box_6.remove('pillow')
box_6.append('truck')

# Replace the bus and the coin and the bell with the plate and the ship and the headphone in Box 0
box_0.remove('bus')
box_0.remove('coin')
box_0.remove('bell')
box_0.append('plate')
box_0.append('ship')
box_0.append('headphone')

# Replace the rock with the comet in Box 5
box_5.remove('rock')
box_5.append('comet')

# Move the dice and the magnet from Box 4 to Box 0
box_4.remove('dice')
box_4.remove('magnet')
box_0.append('dice')
box_0.append('magnet')

# Put the puzzle into Box 4
box_4.append('puzzle')

# Swap the storm in Box 3 with the comet in Box 5
box_3.remove('storm')
box_3.append('comet')
box_5.remove('comet')
box_5.append('storm')

# Put the laptop into Box 3
box_3.append('laptop')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)