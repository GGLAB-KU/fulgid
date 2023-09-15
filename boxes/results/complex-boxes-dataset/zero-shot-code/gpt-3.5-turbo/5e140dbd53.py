box_0 = ['cat', 'fork', 'blender', 'microwave', 'toaster']
box_1 = ['helmet', 'starfish', 'comb']
box_2 = ['frame', 'pan']
box_3 = ['toothbrush', 'gloves', 'controller', 'bell', 'whistle']
box_4 = ['tree', 'plane', 'charger', 'coral', 'sun']
box_5 = ['scarf']
box_6 = ['rain', 'jungle', 'harmonica', 'camera', 'key']
box_7 = []
box_8 = ['wallet', 'button', 'thunder', 'fish']

# Remove the frame and the pan from Box 2
box_2.remove('frame')
box_2.remove('pan')

# Swap the plane in Box 4 with the microwave in Box 0
box_0.remove('microwave')
box_4.remove('plane')
box_0.append('plane')
box_4.append('microwave')

# Move the cat and the blender and the plane from Box 0 to Box 1
box_1.extend(['cat', 'blender', 'plane'])
box_0.remove('cat')
box_0.remove('blender')
box_0.remove('plane')

# Replace the charger with the pen in Box 4
box_4.remove('charger')
box_4.append('pen')

# Put the puzzle and the mountain into Box 5
box_5.extend(['puzzle', 'mountain'])

# Move the fork and the toaster from Box 0 to Box 8
box_8.extend(['fork', 'toaster'])
box_0.remove('fork')
box_0.remove('toaster')

# Move the thunder from Box 8 to Box 3
box_3.append('thunder')
box_8.remove('thunder')

# Remove the coral from Box 4
box_4.remove('coral')

# Move the puzzle and the mountain and the scarf from Box 5 to Box 8
box_8.extend(['puzzle', 'mountain', 'scarf'])
box_5.remove('puzzle')
box_5.remove('mountain')
box_5.remove('scarf')

# Move the camera and the rain and the jungle from Box 6 to Box 1
box_1.extend(['camera', 'rain', 'jungle'])
box_6.remove('camera')
box_6.remove('rain')
box_6.remove('jungle')

# Swap the pen in Box 4 with the fork in Box 8
box_4.remove('pen')
box_8.remove('fork')
box_4.append('fork')
box_8.append('pen')

# Move the microwave and the fork from Box 4 to Box 6
box_6.extend(['microwave', 'fork'])
box_4.remove('microwave')
box_4.remove('fork')

# Replace the gloves and the whistle with the plate and the mask in Box 3
box_3.remove('gloves')
box_3.remove('whistle')
box_3.extend(['plate', 'mask'])

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