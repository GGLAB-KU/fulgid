box_0 = ['branch', 'bracelet', 'fish', 'pan', 'pants']
box_1 = ['rain', 'storm', 'mixer', 'keyboard', 'phone']
box_2 = ['plane', 'piano', 'zipper']
box_3 = ['console']
box_4 = ['doll']
box_5 = ['key', 'freezer', 'wig', 'butterfly', 'starfish']
box_6 = []

# Remove the doll from Box 4
box_4.remove('doll')

# Put the river and the island and the pot into Box 1
box_1.extend(['river', 'island', 'pot'])

# Move the key and the starfish from Box 5 to Box 2
box_2.extend(['key', 'starfish'])
box_5.remove('key')
box_5.remove('starfish')

# Move the storm and the pot and the rain from Box 1 to Box 2
box_2.extend(['storm', 'pot', 'rain'])
box_1.remove('storm')
box_1.remove('pot')
box_1.remove('rain')

# Move the wig and the butterfly from Box 5 to Box 6
box_6.extend(['wig', 'butterfly'])
box_5.remove('wig')
box_5.remove('butterfly')

# Replace the mixer and the river with the key and the chair in Box 1
box_1.remove('mixer')
box_1.remove('river')
box_1.extend(['key', 'chair'])

# Replace the console with the car in Box 3
box_3.remove('console')
box_3.append('car')

# Replace the pants and the fish with the lion and the glove in Box 0
box_0.remove('pants')
box_0.remove('fish')
box_0.extend(['lion', 'glove'])

# Remove the wig and the butterfly from Box 6
box_6.remove('wig')
box_6.remove('butterfly')

# Replace the freezer with the gloves in Box 5
box_5.remove('freezer')
box_5.append('gloves')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)