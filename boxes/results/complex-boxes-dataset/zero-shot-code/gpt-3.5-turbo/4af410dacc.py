box_0 = ['cat']
box_1 = ['makeup', 'clock', 'leaf']
box_2 = ['butterfly']
box_3 = ['swimsuit']
box_4 = ['zipper']
box_5 = ['earring', 'shoes', 'car', 'hat', 'octopus']
box_6 = ['fridge']
box_7 = ['note', 'planet', 'headphone', 'horse', 'glove']
box_8 = ['tiger', 'island', 'helmet', 'sandals']

# Remove the cat from Box 0
box_0.remove('cat')

# Put the boot and the violin into Box 3
box_3.extend(['boot', 'violin'])

# Replace the car and the earring and the octopus with the meteor and the glove and the shoes in Box 5
box_5 = ['meteor', 'glove', 'shoes']

# Remove the butterfly from Box 2
box_2.remove('butterfly')

# Replace the island with the planet in Box 8
box_8.remove('island')
box_8.append('planet')

# Swap the glove in Box 7 with the fridge in Box 6
box_6, box_7 = box_7, box_6

# Swap the note in Box 7 with the sandals in Box 8
box_7.remove('note')
box_8.remove('sandals')
box_7.append('sandals')
box_8.append('note')

# Replace the glove with the storm in Box 6
box_6.remove('glove')
box_6.append('storm')

# Move the shoes from Box 5 to Box 4
box_4.extend(box_5)
box_5 = []

# Move the helmet and the note and the tiger from Box 8 to Box 0
box_0.extend(['helmet', 'note', 'tiger'])
box_8 = []

# Move the tiger from Box 0 to Box 3
box_3.append(box_0.pop(box_0.index('tiger')))

# Move the shoes and the hat and the glove from Box 5 to Box 1
box_1.extend(box_5)
box_1.extend(['hat', 'glove'])
box_5 = []

# Swap the storm in Box 6 with the planet in Box 8
box_6.remove('storm')
box_8.remove('planet')
box_6.append('planet')
box_8.append('storm')

# Replace the meteor with the plate in Box 5
box_5.remove('meteor')
box_5.append('plate')

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