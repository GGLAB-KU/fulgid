box_0 = ['paint', 'planet', 'lightning', 'toy', 'gloves']
box_1 = ['shirt', 'toothbrush']
box_2 = ['frame']
box_3 = ['phone', 'skirt']
box_4 = []
box_5 = ['doll', 'moon', 'elephant']
box_6 = ['table', 'pot', 'pan', 'shelf', 'vase']

# Remove toothbrush from Box 1
box_1.remove('toothbrush')

# Replace paint and planet with microscope and speaker in Box 0
box_0.remove('paint')
box_0.remove('planet')
box_0.extend(['microscope', 'speaker'])

# Replace frame with flower in Box 2
box_2.remove('frame')
box_2.append('flower')

# Swap toy in Box 0 with shirt in Box 1
box_0.remove('toy')
box_1.remove('shirt')
box_0.append('shirt')
box_1.append('toy')

# Move moon, elephant, and doll from Box 5 to Box 3
box_5.remove('moon')
box_5.remove('elephant')
box_5.remove('doll')
box_3.extend(['moon', 'elephant', 'doll'])

# Swap speaker in Box 0 with toy in Box 1
box_0.remove('speaker')
box_1.remove('toy')
box_0.append('toy')
box_1.append('speaker')

# Put controller into Box 1
box_1.append('controller')

# Put usb into Box 0
box_0.append('usb')

# Swap table in Box 6 with usb in Box 0
box_6.remove('table')
box_0.remove('usb')
box_6.append('usb')
box_0.append('table')

# Put bear into Box 6
box_6.append('bear')

# Swap bear in Box 6 with moon in Box 3
box_6.remove('bear')
box_3.remove('moon')
box_6.append('moon')
box_3.append('bear')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)