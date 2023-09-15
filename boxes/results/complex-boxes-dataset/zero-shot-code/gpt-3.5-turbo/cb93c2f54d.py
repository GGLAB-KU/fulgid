box_0 = ['mask', 'star', 'toothbrush', 'shark']
box_1 = ['fridge']
box_2 = ['shoe', 'river']
box_3 = ['polish', 'lion', 'elephant']
box_4 = ['starfish', 'chair', 'gloves', 'comb']

# Swap the shoe in Box 2 with the fridge in Box 1
box_1[0], box_2[0] = box_2[0], box_1[0]

# Remove the comb and the gloves from Box 4
box_4.remove('comb')
box_4.remove('gloves')

# Replace the chair with the forest in Box 4
box_4[1] = 'forest'

# Put the fish and the note into Box 2
box_2.extend(['fish', 'note'])

# Replace the forest and the starfish with the seaweed and the wallet in Box 4
box_4[1] = 'seaweed'
box_4[0] = 'wallet'

# Remove the shoe from Box 1
box_1.remove('shoe')

# Replace the seaweed with the lion in Box 4
box_4[1] = 'lion'

# Put the keyboard and the sandals and the freezer into Box 4
box_4.extend(['keyboard', 'sandals', 'freezer'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)