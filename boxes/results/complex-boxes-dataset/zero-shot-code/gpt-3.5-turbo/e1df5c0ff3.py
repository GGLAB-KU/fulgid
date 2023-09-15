box_0 = ['thunder', 'toothpaste', 'spoon']
box_1 = ['motorcycle', 'note', 'pot', 'usb']
box_2 = []
box_3 = ['microwave', 'microscope']
box_4 = ['toaster', 'ring', 'car', 'freezer', 'scissors']
box_5 = ['console', 'plane']
box_6 = ['boot', 'jungle']
box_7 = ['plate', 'river', 'perfume']
box_8 = ['controller', 'snow']
box_9 = ['horse', 'sock', 'shoe', 'cow']
box_10 = ['forest']

# Remove toothpaste, thunder, and spoon from Box 0
box_0.remove('toothpaste')
box_0.remove('thunder')
box_0.remove('spoon')

# Move river, perfume, and plate from Box 7 to Box 10
box_10.extend(box_7)
box_7.clear()

# Put towel and swimsuit into Box 8
box_8.extend(['towel', 'swimsuit'])

# Move console from Box 5 to Box 7
box_7.append(box_5.pop(0))

# Swap plate in Box 10 with towel in Box 8
box_10.remove('plate')
box_8.remove('towel')
box_10.append('towel')
box_8.append('plate')

# Put phone, bus, and horn into Box 2
box_2.extend(['phone', 'bus', 'horn'])

# Replace forest and perfume with beach and telescope in Box 10
box_10.remove('forest')
box_10.remove('perfume')
box_10.extend(['beach', 'telescope'])

# Move scissors, car, and ring from Box 4 to Box 1
box_1.extend(['scissors', 'car', 'ring'])
box_4.remove('scissors')
box_4.remove('car')
box_4.remove('ring')

# Empty Box 5
box_5.clear()

# Put microwave into Box 4
box_4.append('microwave')

# Move ring from Box 1 to Box 2
box_2.append(box_1.pop(box_1.index('ring')))

# Remove microscope from Box 3
box_3.remove('microscope')

# Swap jungle in Box 6 with horn in Box 2
box_2.append(box_6.pop(box_6.index('horn')))
box_6.append('jungle')

# Move horse, cow, and sock from Box 9 to Box 7
box_7.extend(['horse', 'cow', 'sock'])
box_9.remove('horse')
box_9.remove('cow')
box_9.remove('sock')

# Empty Box 2
box_2.clear()

# Remove toaster from Box 4
box_4.remove('toaster')

# Replace snow with wire in Box 8
box_8.remove('snow')
box_8.append('wire')

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