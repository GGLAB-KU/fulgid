box_0 = ['ship', 'shoe', 'lipstick', 'piano', 'magnet']
box_1 = ['table', 'mountain']
box_2 = []
box_3 = ['guitar', 'octopus', 'fish', 'dress', 'helmet']
box_4 = ['dog', 'boot', 'coin', 'horn', 'coral']
box_5 = ['motorcycle', 'tiger', 'plate', 'island']
box_6 = ['gloves', 'comb', 'starfish']
box_7 = ['camera', 'microwave', 'lion', 'leaf', 'razor']

# Replace the clock and the shampoo with the comb and the starfish in Box 6
box_6.remove('clock')
box_6.remove('shampoo')
box_6.append('comb')
box_6.append('starfish')

# Swap the dog in Box 4 with the table in Box 1
box_1.remove('table')
box_4.remove('dog')
box_1.append('dog')
box_4.append('table')

# Move the ship and the shoe and the magnet from Box 0 to Box 6
box_0.remove('ship')
box_0.remove('shoe')
box_0.remove('magnet')
box_6.append('ship')
box_6.append('shoe')
box_6.append('magnet')

# Put the rock and the river and the storm into Box 1
box_1.append('rock')
box_1.append('river')
box_1.append('storm')

# Remove the camera and the razor and the leaf from Box 7
box_7.remove('camera')
box_7.remove('razor')
box_7.remove('leaf')

# Swap the starfish in Box 6 with the guitar in Box 3
box_6.remove('starfish')
box_3.remove('guitar')
box_6.append('guitar')
box_3.append('starfish')

# Replace the ship with the plane in Box 6
box_6.remove('ship')
box_6.append('plane')

# Remove the storm from Box 1
box_1.remove('storm')

# Put the puzzle into Box 4
box_4.append('puzzle')

# Replace the coral with the coin in Box 4
box_4.remove('coral')
box_4.append('coin')

# Put the shoes and the lightning into Box 5
box_5.append('shoes')
box_5.append('lightning')

# Move the plate and the island from Box 5 to Box 4
box_5.remove('plate')
box_5.remove('island')
box_4.append('plate')
box_4.append('island')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)