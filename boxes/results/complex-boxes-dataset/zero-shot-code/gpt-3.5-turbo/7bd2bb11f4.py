box_0 = ['bag']
box_1 = []
box_2 = ['boot', 'comet', 'lightning']
box_3 = []
box_4 = ['belt', 'jacket']
box_5 = ['controller', 'motorcycle', 'comb']
box_6 = ['doll', 'guitar', 'brush']
box_7 = ['horn', 'fish']

# Move the belt from Box 4 to Box 2
box_2.append(box_4.pop(box_4.index('belt')))

# Remove the fish from Box 7
box_7.remove('fish')

# Swap the bag in Box 0 with the controller in Box 5
box_0[0], box_5[box_5.index('controller')] = box_5[box_5.index('controller')], box_0[0]

# Swap the controller in Box 0 with the horn in Box 7
box_0[0], box_7[box_7.index('horn')] = box_7[box_7.index('horn')], box_0[0]

# Remove the horn from Box 0
box_0.remove('horn')

# Replace the jacket with the fish in Box 4
box_4[box_4.index('jacket')] = 'fish'

# Move the comb and the motorcycle from Box 5 to Box 3
box_3.extend([box_5.pop(box_5.index('comb')), box_5.pop(box_5.index('motorcycle'))])

# Put the laptop and the tree and the glasses into Box 6
box_6.extend(['laptop', 'tree', 'glasses'])

# Remove the comb and the motorcycle from Box 3
box_3 = []

# Swap the controller in Box 7 with the boot in Box 2
box_2[box_2.index('boot')], box_7[box_7.index('controller')] = box_7[box_7.index('controller')], box_2[box_2.index('boot')]

# Put the cloud into Box 1
box_1.append('cloud')

# Replace the cloud with the charger in Box 1
box_1[box_1.index('cloud')] = 'charger'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)