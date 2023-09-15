box_0 = ['candle', 'snow', 'puzzle']
box_1 = ['comb', 'train', 'cow']
box_2 = ['dice', 'pot', 'mirror', 'gloves']
box_3 = ['guitar', 'octopus', 'leaf', 'coral']
box_4 = ['wire', 'magnet', 'key', 'toaster']
box_5 = ['doll', 'fish', 'pants', 'tiger']

# Replace items in Box 5
box_5[0] = 'doll'
box_5[1] = 'camera'
box_5[2] = 'fridge'

# Replace items in Box 0
box_0[0] = 'controller'
box_0[1] = 'bowl'
box_0[2] = 'bear'

# Swap key in Box 4 with guitar in Box 3
box_4[2], box_3[0] = box_3[0], box_4[2]

# Put thunder and pants into Box 0
box_0.append('thunder')
box_0.append('pants')

# Replace gloves, pot, and dice with shirt, ocean, and swimsuit in Box 2
box_2[2] = 'shirt'
box_2[3] = 'ocean'
box_2.append('swimsuit')

# Remove thunder and pants from Box 0
box_0.remove('thunder')
box_0.remove('pants')

# Swap controller in Box 0 with toaster in Box 4
box_0[0], box_4[3] = box_4[3], box_0[0]

# Replace wire with wig in Box 4
box_4[0] = 'wig'

# Put octopus, bear, and dog into Box 2
box_2.append('octopus')
box_2.append('bear')
box_2.append('dog')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)