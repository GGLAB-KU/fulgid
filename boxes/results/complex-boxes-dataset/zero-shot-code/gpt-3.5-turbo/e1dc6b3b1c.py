box_0 = ['mixer']
box_1 = ['bird', 'bear', 'dolphin', 'usb']
box_2 = []
box_3 = ['pen']
box_4 = ['fridge', 'comb', 'toaster', 'keyboard', 'makeup']
box_5 = ['leaf', 'glove']
box_6 = ['swimsuit', 'lion', 'lipstick', 'ring', 'candle']
box_7 = ['wallet', 'snow', 'lamp', 'earring']
box_8 = []

# Remove the toaster from Box 4
box_4.remove('toaster')

# Move the makeup from Box 4 to Box 0
box_0.append(box_4.pop(box_4.index('makeup')))

# Move the leaf from Box 5 to Box 8
box_8.append(box_5.pop(box_5.index('leaf')))

# Swap the leaf in Box 8 with the pen in Box 3
box_8.append(box_3.pop(box_3.index('pen')))
box_3.append(box_8.pop(box_8.index('leaf')))

# Move the fridge and the keyboard and the comb from Box 4 to Box 1
box_1.extend([box_4.pop(box_4.index('fridge')), box_4.pop(box_4.index('keyboard')), box_4.pop(box_4.index('comb'))])

# Swap the pen in Box 8 with the mixer in Box 0
box_8.append(box_0.pop(box_0.index('mixer')))
box_0.append(box_8.pop(box_8.index('pen')))

# Move the lamp and the snow and the wallet from Box 7 to Box 1
box_1.extend([box_7.pop(box_7.index('lamp')), box_7.pop(box_7.index('snow')), box_7.pop(box_7.index('wallet'))])

# Remove the makeup from Box 0
box_0.remove('makeup')

# Swap the earring in Box 7 with the pen in Box 0
box_7.append(box_0.pop(box_0.index('pen')))
box_0.append(box_7.pop(box_7.index('earring')))

# Move the pen from Box 7 to Box 6
box_6.append(box_7.pop(box_7.index('pen')))

# Replace the earring with the brush in Box 0
box_0.append('brush')
box_0.remove('earring')

# Put the swimsuit and the vase into Box 8
box_8.extend(['swimsuit', 'vase'])

# Swap the usb in Box 1 with the vase in Box 8
box_1.append(box_8.pop(box_8.index('usb')))
box_8.append(box_1.pop(box_1.index('vase')))

# Put the pen and the beach and the phone into Box 0
box_0.extend(['pen', 'beach', 'phone'])

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