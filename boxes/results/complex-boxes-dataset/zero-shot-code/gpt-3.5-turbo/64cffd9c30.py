box_0 = ['battery', 'truck']
box_1 = ['tie', 'rocket', 'moon']
box_2 = ['grinder', 'wallet', 'shoes', 'toothbrush']
box_3 = ['bag', 'dog', 'dolphin']
box_4 = ['mirror', 'bird']
box_5 = ['rain', 'shark']
box_6 = ['bear', 'crown', 'plane', 'guitar']

# Move the wallet from Box 2 to Box 1
box_1.append(box_2.pop(box_2.index('wallet')))

# Move the plane and the crown and the guitar from Box 6 to Box 1
box_1.extend([box_6.pop(box_6.index('plane')), box_6.pop(box_6.index('crown')), box_6.pop(box_6.index('guitar'))])

# Put the sun into Box 0
box_0.append('sun')

# Put the paint and the comet into Box 1
box_1.extend(['paint', 'comet'])

# Put the magnet and the speaker into Box 5
box_5.extend(['magnet', 'speaker'])

# Remove the truck and the battery and the sun from Box 0
box_0.remove('truck')
box_0.remove('battery')
box_0.remove('sun')

# Put the razor into Box 2
box_2.append('razor')

# Replace the bird with the glasses in Box 4
box_4[box_4.index('bird')] = 'glasses'

# Move the razor and the grinder from Box 2 to Box 1
box_1.extend([box_2.pop(box_2.index('razor')), box_2.pop(box_2.index('grinder'))])

# Put the bird into Box 4
box_4.append('bird')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)