box_0 = ['fridge', 'wig', 'glove']
box_1 = ['sun', 'doll']
box_2 = []
box_3 = []
box_4 = ['key', 'jungle', 'usb', 'train']
box_5 = ['lock', 'rocket']
box_6 = ['microwave', 'freezer', 'meteor', 'mountain']
box_7 = ['tree', 'coral', 'needle']
box_8 = []
box_9 = ['headphone']
box_10 = ['bear', 'grass']
box_11 = ['river', 'butterfly']

# Move the microwave, mountain, and meteor from Box 6 to Box 2
box_2.extend([box_6.pop(box_6.index('microwave')), box_6.pop(box_6.index('mountain')), box_6.pop(box_6.index('meteor'))])

# Remove the sun and the doll from Box 1
box_1.remove('sun')
box_1.remove('doll')

# Remove the meteor from Box 2
box_2.remove('meteor')

# Replace the bear with the shorts in Box 10
box_10.remove('bear')
box_10.append('shorts')

# Put the lamp into Box 5
box_5.append('lamp')

# Swap the lamp in Box 5 with the freezer in Box 6
box_5.remove('lamp')
box_6.remove('freezer')
box_5.append('freezer')
box_6.append('lamp')

# Put the magnet and the horse into Box 7
box_7.extend(['magnet', 'horse'])

# Empty Box 0
box_0.clear()

# Move the headphone from Box 9 to Box 5
box_5.append(box_9.pop())

# Swap the shorts in Box 10 with the key in Box 4
box_10.remove('shorts')
box_4.remove('key')
box_10.append('key')
box_4.append('shorts')

# Remove the coral from Box 7
box_7.remove('coral')

# Move the lamp from Box 6 to Box 5
box_5.append(box_6.pop(box_6.index('lamp')))

# Move the needle from Box 7 to Box 11
box_11.append(box_7.pop(box_7.index('needle')))

# Swap the microwave in Box 2 with the butterfly in Box 11
box_2.remove('microwave')
box_11.remove('butterfly')
box_2.append('butterfly')
box_11.append('microwave')

# Remove the microwave and the needle from Box 11
box_11.remove('microwave')
box_11.remove('needle')

# Remove the shorts and the usb from Box 4
box_4.remove('shorts')
box_4.remove('usb')

# Remove the grass from Box 10
box_10.remove('grass')

# Put the table into Box 6
box_6.append('table')

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