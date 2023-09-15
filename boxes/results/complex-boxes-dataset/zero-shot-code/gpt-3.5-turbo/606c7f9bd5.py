box_0 = ['toy']
box_1 = ['microwave', 'coral', 'gloves', 'tiger']
box_2 = ['boot']
box_3 = []
box_4 = ['scissors', 'candle', 'puzzle', 'thread', 'frame']
box_5 = ['mirror', 'crown', 'controller', 'pen']
box_6 = ['basket', 'shelf', 'wire', 'pan', 'polish']
box_7 = ['shorts', 'fish', 'shirt']
box_8 = ['bicycle', 'bus', 'magnet']
box_9 = ['needle', 'flute', 'bag']

# Move the puzzle and the candle from Box 4 to Box 5
box_5.extend([box_4.pop(box_4.index('puzzle')), box_4.pop(box_4.index('candle'))])

# Swap the bus in Box 8 with the scissors in Box 4
box_8[box_8.index('bus')], box_4[box_4.index('scissors')] = box_4[box_4.index('scissors')], box_8[box_8.index('bus')]

# Replace the fish with the mountain in Box 7
box_7[box_7.index('fish')] = 'mountain'

# Swap the controller in Box 5 with the toy in Box 0
box_5[box_5.index('controller')], box_0[0] = box_0[0], box_5[box_5.index('controller')]

# Empty Box 0
box_0 = []

# Swap the microwave in Box 1 with the boot in Box 2
box_1[box_1.index('microwave')], box_2[box_2.index('boot')] = box_2[box_2.index('boot')], box_1[box_1.index('microwave')]

# Remove the flute from Box 9
box_9.remove('flute')

# Put the toothpaste and the bicycle and the boat into Box 5
box_5.extend(['toothpaste', 'bicycle', 'boat'])

# Swap the microwave in Box 2 with the shelf in Box 6
box_2[box_2.index('boot')], box_6[box_6.index('shelf')] = box_6[box_6.index('shelf')], box_2[box_2.index('boot')]

# Replace the boat and the mirror with the mask and the usb in Box 5
box_5[box_5.index('boat')], box_5[box_5.index('mirror')] = 'mask', 'usb'

# Swap the magnet in Box 8 with the shorts in Box 7
box_8[box_8.index('magnet')], box_7[box_7.index('shorts')] = box_7[box_7.index('shorts')], box_8[box_8.index('magnet')]

# Move the bag from Box 9 to Box 8
box_8.append(box_9.pop(box_9.index('bag')))

# Put the bicycle and the horse into Box 6
box_6.extend(['bicycle', 'horse'])

# Swap the bag in Box 8 with the frame in Box 4
box_8[box_8.index('bag')], box_4[box_4.index('frame')] = box_4[box_4.index('frame')], box_8[box_8.index('bag')]

# Move the bag and the bus from Box 4 to Box 8
box_8.extend([box_4.pop(box_4.index('bag')), box_4.pop(box_4.index('bus'))])

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