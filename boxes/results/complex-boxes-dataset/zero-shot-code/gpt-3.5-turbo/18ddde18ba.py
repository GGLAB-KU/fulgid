box_0 = ['drum', 'grinder', 'blanket', 'pot', 'star']
box_1 = ['bear']
box_2 = ['zipper', 'crown']
box_3 = ['earring']
box_4 = []
box_5 = ['shoes', 'coin', 'dress', 'apple', 'glove']
box_6 = ['mountain', 'shoe', 'clock', 'card', 'sandals']
box_7 = ['doll', 'shampoo', 'usb', 'oven', 'piano']
box_8 = ['bracelet', 'tiger', 'spoon', 'skirt', 'headphone']
box_9 = ['magnet', 'guitar', 'bus', 'comet']
box_10 = ['microscope', 'lamp']
box_11 = ['toaster', 'butterfly', 'bell', 'comb']
box_12 = ['note']
box_13 = ['shark', 'motorcycle']

# Remove the headphone from Box 8
box_8.remove('headphone')

# Remove the card and the sandals from Box 6
box_6.remove('card')
box_6.remove('sandals')

# Remove the microscope from Box 10
box_10.remove('microscope')

# Swap the lamp in Box 10 with the piano in Box 7
box_10.remove('lamp')
box_7.remove('piano')
box_10.append('piano')
box_7.append('lamp')

# Swap the earring in Box 3 with the zipper in Box 2
box_3.remove('earring')
box_2.remove('zipper')
box_3.append('zipper')
box_2.append('earring')

# Put the oven and the belt into Box 4
box_4.append('oven')
box_4.append('belt')

# Move the zipper from Box 3 to Box 5
box_3.remove('zipper')
box_5.append('zipper')

# Move the dress and the zipper and the shoes from Box 5 to Box 1
box_5.remove('dress')
box_5.remove('zipper')
box_5.remove('shoes')
box_1.append('dress')
box_1.append('zipper')
box_1.append('shoes')

# Put the microscope and the shelf into Box 1
box_1.append('microscope')
box_1.append('shelf')

# Swap the glove in Box 5 with the grinder in Box 0
box_5.remove('glove')
box_0.remove('grinder')
box_5.append('grinder')
box_0.append('glove')

# Empty Box 8
box_8 = []

# Remove the mountain from Box 6
box_6.remove('mountain')

# Replace the note with the shoe in Box 12
box_12.remove('note')
box_12.append('shoe')

# Swap the piano in Box 10 with the belt in Box 4
box_10.remove('piano')
box_4.remove('belt')
box_10.append('belt')
box_4.append('piano')

# Remove the shoe from Box 12
box_12.remove('shoe')

# Swap the belt in Box 10 with the earring in Box 2
box_10.remove('belt')
box_2.remove('earring')
box_10.append('earring')
box_2.append('belt')

# Swap the blanket in Box 0 with the usb in Box 7
box_0.remove('blanket')
box_7.remove('usb')
box_0.append('usb')
box_7.append('blanket')

# Replace the shelf with the shoes in Box 1
box_1.remove('shelf')
box_1.append('shoes')

# Replace the butterfly and the toaster and the bell with the blender and the scissors and the tape in Box 11
box_11.remove('butterfly')
box_11.remove('toaster')
box_11.remove('bell')
box_11.append('blender')
box_11.append('scissors')
box_11.append('tape')

# Remove the usb from Box 0
box_0.remove('usb')

# Put the ocean and the razor and the pot into Box 6
box_6.append('ocean')
box_6.append('razor')
box_6.append('pot')

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
print("Box 13:", box_13)