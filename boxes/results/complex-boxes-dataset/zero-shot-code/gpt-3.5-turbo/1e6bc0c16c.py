box_0 = ['shorts', 'earring', 'mixer', 'battery']
box_1 = ['blender', 'planet']
box_2 = ['needle', 'rain', 'game', 'perfume']
box_3 = ['console', 'shark', 'island', 'controller', 'mountain']
box_4 = []
box_5 = []
box_6 = ['fork', 'boot', 'lamp']
box_7 = ['candle', 'umbrella', 'lion', 'lightning', 'ship']
box_8 = ['belt', 'piano']
box_9 = ['mirror', 'leaf']
box_10 = ['basket', 'glove', 'ocean']

# Remove the planet and the blender from Box 1
box_1.remove('planet')
box_1.remove('blender')

# Remove the basket and the glove from Box 10
box_10.remove('basket')
box_10.remove('glove')

# Put the plane into Box 4
box_4.append('plane')

# Swap the belt in Box 8 with the mirror in Box 9
box_8.remove('belt')
box_9.remove('mirror')
box_8.append('mirror')
box_9.append('belt')

# Empty Box 4
box_4 = []

# Empty Box 6
box_6 = []

# Remove the candle, ship, and umbrella from Box 7
box_7.remove('candle')
box_7.remove('umbrella')
box_7.remove('ship')

# Put the puzzle and the towel into Box 2
box_2.append('puzzle')
box_2.append('towel')

# Empty Box 7
box_7 = []

# Put the doll into Box 2
box_2.append('doll')

# Move the battery from Box 0 to Box 9
box_9.append(box_0.pop(box_0.index('battery')))

# Remove the piano from Box 8
box_8.remove('piano')

# Remove the battery and the belt from Box 9
box_9.remove('battery')
box_9.remove('belt')

# Remove the mixer from Box 0
box_0.remove('mixer')

# Replace the mountain and the controller with the glasses and the ocean in Box 3
box_3.remove('mountain')
box_3.remove('controller')
box_3.append('glasses')
box_3.append('ocean')

# Replace the glasses and the ocean with the perfume and the flower in Box 3
box_3.remove('glasses')
box_3.remove('ocean')
box_3.append('perfume')
box_3.append('flower')

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