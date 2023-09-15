box_0 = ['glove', 'microscope']
box_1 = []
box_2 = ['needle', 'camera', 'zipper', 'shark']
box_3 = []
box_4 = ['rocket', 'forest', 'key']
box_5 = ['ship']
box_6 = ['bicycle', 'bus', 'bird', 'shoe']
box_7 = ['toothpaste', 'pants', 'frame', 'candle']
box_8 = []

# Move the bus, shoe, and bird from Box 6 to Box 4
box_4.extend([box_6.pop(box_6.index('bus')), box_6.pop(box_6.index('shoe')), box_6.pop(box_6.index('bird'))])

# Replace the ship with the bird in Box 5
box_5.pop()
box_5.append('bird')

# Move the forest from Box 4 to Box 3
box_3.append(box_4.pop(box_4.index('forest')))

# Swap the candle in Box 7 with the bird in Box 5
box_7[box_7.index('candle')], box_5[box_5.index('bird')] = box_5[box_5.index('bird')], box_7[box_7.index('candle')]

# Move the key, rocket, and bus from Box 4 to Box 1
box_1.extend([box_4.pop(box_4.index('key')), box_4.pop(box_4.index('rocket')), box_4.pop(box_4.index('bus'))])

# Put the towel into Box 4
box_4.append('towel')

# Remove the bicycle from Box 6
box_6.remove('bicycle')

# Put the scissors, wire, and bell into Box 3
box_3.extend(['scissors', 'wire', 'bell'])

# Move the rocket from Box 1 to Box 0
box_0.append(box_1.pop(box_1.index('rocket')))

# Replace the key and bus with the bell and keyboard in Box 1
box_1[box_1.index('key')] = 'bell'
box_1[box_1.index('bus')] = 'keyboard'

# Move the shark, needle, and camera from Box 2 to Box 6
box_6.extend([box_2.pop(box_2.index('shark')), box_2.pop(box_2.index('needle')), box_2.pop(box_2.index('camera'))])

# Remove the towel and shoe from Box 4
box_4.remove('towel')
box_4.remove('shoe')

# Swap the bird in Box 7 with the bird in Box 4
box_7[box_7.index('bird')], box_4[box_4.index('bird')] = box_4[box_4.index('bird')], box_7[box_7.index('bird')]

# Replace the bird with the crown in Box 4
box_4[box_4.index('bird')] = 'crown'

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