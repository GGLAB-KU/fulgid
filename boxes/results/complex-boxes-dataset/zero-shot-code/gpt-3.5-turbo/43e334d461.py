box_0 = ['forest', 'usb', 'octopus', 'towel']
box_1 = ['truck', 'tree', 'toaster']
box_2 = ['perfume', 'card', 'frame']
box_3 = ['shoe', 'ocean', 'coat', 'watch']
box_4 = ['snow', 'umbrella', 'cow', 'microscope', 'star']
box_5 = ['key', 'plane', 'necklace']

# Move key and plane from Box 5 to Box 2
box_2.extend([box_5.pop(box_5.index('key')), box_5.pop(box_5.index('plane'))])

# Swap usb in Box 0 with plane in Box 2
box_0[box_0.index('usb')], box_2[box_2.index('plane')] = box_2[box_2.index('plane')], box_0[box_0.index('usb')]

# Swap snow in Box 4 with plane in Box 0
box_4[box_4.index('snow')], box_0[box_0.index('plane')] = box_0[box_0.index('plane')], box_4[box_4.index('snow')]

# Replace toaster, tree, and truck with violin, thunder, and telescope in Box 1
box_1 = ['violin', 'thunder', 'telescope']

# Swap snow in Box 0 with microscope in Box 4
box_0[box_0.index('snow')], box_4[box_4.index('microscope')] = box_4[box_4.index('microscope')], box_0[box_0.index('snow')]

# Put necklace into Box 2
box_2.append('necklace')

# Put jungle and razor into Box 2
box_2.extend(['jungle', 'razor'])

# Replace umbrella, cow, and star with shirt, octopus, and phone in Box 4
box_4 = ['shirt', 'octopus', 'phone']

# Replace necklace with jacket in Box 5
box_5[box_5.index('necklace')] = 'jacket'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)