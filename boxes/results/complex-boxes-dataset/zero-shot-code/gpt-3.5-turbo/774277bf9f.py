box_0 = ['bird', 'coat', 'shampoo', 'earring', 'basket']
box_1 = ['rocket', 'fish', 'magnet']
box_2 = ['comb']
box_3 = ['submarine', 'octopus', 'flute', 'car']
box_4 = ['candle', 'wire', 'rain', 'headphone']
box_5 = ['coral', 'toaster', 'grass', 'sock']
box_6 = ['towel', 'leaf']
box_7 = ['book', 'mask', 'helmet', 'dolphin']
box_8 = ['perfume']

# Remove grass, sock, and coral from Box 5
box_5.remove('grass')
box_5.remove('sock')
box_5.remove('coral')

# Empty Box 2
box_2 = []

# Replace car with spoon in Box 3
box_3.remove('car')
box_3.append('spoon')

# Move perfume from Box 8 to Box 3
box_8.remove('perfume')
box_3.append('perfume')

# Remove submarine from Box 3
box_3.remove('submarine')

# Put towel, moon, and needle into Box 3
box_3.append('towel')
box_3.append('moon')
box_3.append('needle')

# Move toaster from Box 5 to Box 3
box_5.remove('toaster')
box_3.append('toaster')

# Move towel and leaf from Box 6 to Box 0
box_6.remove('towel')
box_0.append('towel')
box_6.remove('leaf')
box_0.append('leaf')

# Replace fish and rocket with toaster and truck in Box 1
box_1.remove('fish')
box_1.remove('rocket')
box_1.append('toaster')
box_1.append('truck')

# Put frame into Box 8
box_8.append('frame')

# Swap towel in Box 0 with octopus in Box 3
box_0.remove('towel')
box_3.remove('octopus')
box_0.append('octopus')
box_3.append('towel')

# Swap toaster in Box 1 with headphone in Box 4
box_1.remove('toaster')
box_4.remove('headphone')
box_1.append('headphone')
box_4.append('toaster')

# Replace magnet and headphone with comb and pot in Box 1
box_1.remove('magnet')
box_1.remove('headphone')
box_1.append('comb')
box_1.append('pot')

# Move leaf, earring, and octopus from Box 0 to Box 7
box_0.remove('leaf')
box_7.append('leaf')
box_0.remove('earring')
box_7.append('earring')
box_0.remove('octopus')
box_7.append('octopus')

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