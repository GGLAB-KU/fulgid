box_0 = ['microscope', 'toothpaste', 'shorts']
box_1 = []
box_2 = ['clock', 'fridge', 'mask', 'telescope']
box_3 = []
box_4 = ['puzzle', 'flute']

# Replace the telescope with the vase in Box 2
box_2.remove('telescope')
box_2.append('vase')

# Swap the flute in Box 4 with the mask in Box 2
box_4.remove('flute')
box_2.remove('mask')
box_4.append('mask')
box_2.append('flute')

# Swap the flute in Box 2 with the puzzle in Box 4
box_2.remove('flute')
box_4.remove('puzzle')
box_2.append('puzzle')
box_4.append('flute')

# Swap the mask in Box 4 with the microscope in Box 0
box_4.remove('mask')
box_0.remove('microscope')
box_4.append('microscope')
box_0.append('mask')

# Replace the clock and the vase with the beach and the usb in Box 2
box_2.remove('clock')
box_2.remove('vase')
box_2.append('beach')
box_2.append('usb')

# Put the swimsuit and the coat and the horn into Box 2
box_2.append('swimsuit')
box_2.append('coat')
box_2.append('horn')

# Put the glasses into Box 3
box_3.append('glasses')

# Swap the microscope in Box 4 with the mask in Box 0
box_4.remove('microscope')
box_0.remove('mask')
box_4.append('mask')
box_0.append('microscope')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)