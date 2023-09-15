box_0 = ['comb', 'puzzle', 'sock', 'boat', 'glasses']
box_1 = ['chair', 'dog']
box_2 = ['razor', 'fork', 'controller']
box_3 = ['scarf', 'star', 'gloves', 'forest']
box_4 = ['soap', 'ship', 'pillow']
box_5 = []
box_6 = ['bowl', 'butterfly', 'clock']
box_7 = ['charger', 'violin']
box_8 = []
box_9 = ['umbrella', 'ring']
box_10 = []
box_11 = ['branch', 'pen', 'basket', 'skirt', 'grinder']
box_12 = ['tie']

# Remove the scarf from Box 3
box_3.remove('scarf')

# Swap the violin in Box 7 with the controller in Box 2
box_7.remove('violin')
box_2.remove('controller')
box_7.append('controller')
box_2.append('violin')

# Empty Box 6
box_6.clear()

# Replace the fork with the pillow in Box 2
box_2.remove('fork')
box_4.remove('pillow')
box_2.append('pillow')
box_4.append('fork')

# Put the cow and the usb and the candle into Box 0
box_0.extend(['cow', 'usb', 'candle'])

# Move the ship and the soap from Box 4 to Box 6
box_4.remove('ship')
box_4.remove('soap')
box_6.extend(['ship', 'soap'])

# Replace the basket and the branch with the cloud and the sun in Box 11
box_11.remove('basket')
box_11.remove('branch')
box_11.extend(['cloud', 'sun'])

# Move the pillow from Box 4 to Box 0
box_4.remove('pillow')
box_0.append('pillow')

# Swap the chair in Box 1 with the star in Box 3
box_1.remove('chair')
box_3.remove('star')
box_1.append('star')
box_3.append('chair')

# Move the gloves and the forest from Box 3 to Box 8
box_3.remove('gloves')
box_3.remove('forest')
box_8.extend(['gloves', 'forest'])

# Remove the ring from Box 9
box_9.remove('ring')

# Swap the umbrella in Box 9 with the charger in Box 7
box_9.remove('umbrella')
box_7.remove('charger')
box_9.append('charger')
box_7.append('umbrella')

# Swap the gloves in Box 8 with the skirt in Box 11
box_8.remove('gloves')
box_11.remove('skirt')
box_8.append('skirt')
box_11.append('gloves')

# Move the ship and the soap from Box 6 to Box 5
box_6.remove('ship')
box_6.remove('soap')
box_5.extend(['ship', 'soap'])

# Empty Box 12
box_12.clear()

# Replace the grinder with the blender in Box 11
box_11.remove('grinder')
box_11.append('blender')

# Put the necklace and the soap and the jacket into Box 6
box_6.extend(['necklace', 'soap', 'jacket'])

# Put the book into Box 8
box_8.append('book')

# Replace the controller and the umbrella with the jungle and the charger in Box 7
box_7.remove('controller')
box_7.remove('umbrella')
box_7.append('jungle')
box_7.append('charger')

# Swap the dog in Box 1 with the ship in Box 5
box_1.remove('dog')
box_5.remove('ship')
box_1.append('ship')
box_5.append('dog')

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
print("Box 11:", box_11)
print("Box 12:", box_12)