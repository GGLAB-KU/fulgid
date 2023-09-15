box_0 = ['ring', 'paint', 'lamp', 'cup', 'lock']
box_1 = ['pot']
box_2 = ['forest', 'needle', 'storm']
box_3 = ['cloud', 'usb', 'speaker']
box_4 = ['toy']
box_5 = []
box_6 = ['horse', 'island', 'key', 'piano']
box_7 = ['towel', 'comb']
box_8 = []
box_9 = ['horn', 'lion', 'lightning', 'shampoo', 'ocean']

# Replace the toy with the whistle in Box 4
box_4.remove('toy')
box_4.append('whistle')

# Swap the pot in Box 1 with the usb in Box 3
box_1.remove('pot')
box_3.remove('usb')
box_1.append('usb')
box_3.append('pot')

# Remove the whistle from Box 4
box_4.remove('whistle')

# Put the lock and the bird and the motorcycle into Box 4
box_4.extend(['lock', 'bird', 'motorcycle'])

# Put the perfume and the seaweed into Box 0
box_0.extend(['perfume', 'seaweed'])

# Put the swimsuit and the bus and the flower into Box 1
box_1.extend(['swimsuit', 'bus', 'flower'])

# Remove the flower and the usb from Box 1
box_1.remove('flower')
box_1.remove('usb')

# Move the bird and the motorcycle from Box 4 to Box 1
box_4.remove('bird')
box_4.remove('motorcycle')
box_1.extend(['bird', 'motorcycle'])

# Move the storm and the needle from Box 2 to Box 0
box_2.remove('storm')
box_2.remove('needle')
box_0.extend(['storm', 'needle'])

# Empty Box 0
box_0 = []

# Swap the key in Box 6 with the lock in Box 4
box_6.remove('key')
box_4.remove('lock')
box_6.append('lock')
box_4.append('key')

# Move the comb and the towel from Box 7 to Box 1
box_7.remove('comb')
box_7.remove('towel')
box_1.extend(['comb', 'towel'])

# Replace the speaker and the pot with the helmet and the wig in Box 3
box_3.remove('speaker')
box_3.remove('pot')
box_3.extend(['helmet', 'wig'])

# Swap the lightning in Box 9 with the island in Box 6
box_9.remove('lightning')
box_6.remove('island')
box_9.append('island')
box_6.append('lightning')

# Move the key from Box 4 to Box 0
box_4.remove('key')
box_0.append('key')

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