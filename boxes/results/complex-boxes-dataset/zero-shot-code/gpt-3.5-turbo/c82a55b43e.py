box_0 = ['grass', 'necklace', 'puzzle', 'coat', 'meteor']
box_1 = ['tree', 'umbrella', 'dolphin', 'bracelet', 'piano']
box_2 = ['butterfly', 'wire', 'ocean', 'charger']
box_3 = ['telescope']
box_4 = ['mask']
box_5 = ['boat', 'console', 'coral']
box_6 = ['bear', 'laptop', 'speaker', 'pen']

# Move the puzzle from Box 0 to Box 6
box_6.append(box_0.pop(box_0.index('puzzle')))

# Remove the speaker from Box 6
box_6.remove('speaker')

# Move the charger and the ocean and the butterfly from Box 2 to Box 6
box_6.extend([box_2.pop(box_2.index('charger')), box_2.pop(box_2.index('ocean')), box_2.pop(box_2.index('butterfly'))])

# Put the butterfly into Box 4
box_4.append(box_6.pop(box_6.index('butterfly')))

# Move the mask from Box 4 to Box 0
box_0.append(box_4.pop(box_4.index('mask')))

# Put the chair and the magnet and the boat into Box 0
box_0.extend(['chair', 'magnet', 'boat'])

# Swap the ocean in Box 6 with the butterfly in Box 4
box_6.append(box_4.pop(box_4.index('ocean')))
box_4.append(box_6.pop(box_6.index('butterfly')))

# Move the wire from Box 2 to Box 3
box_3.append(box_2.pop(box_2.index('wire')))

# Replace the dolphin and the umbrella and the bracelet with the bowl and the shoes and the necklace in Box 1
box_1[2:5] = ['bowl', 'shoes', 'necklace']

# Swap the console in Box 5 with the wire in Box 3
box_5.append(box_3.pop(box_3.index('console')))
box_3.append(box_5.pop(box_5.index('wire')))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)