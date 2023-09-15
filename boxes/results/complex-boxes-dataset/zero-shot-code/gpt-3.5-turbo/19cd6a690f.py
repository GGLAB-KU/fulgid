box_0 = ['bag']
box_1 = ['frame', 'shoe', 'toaster']
box_2 = ['glove', 'candle', 'button', 'coat', 'plane']
box_3 = ['butterfly', 'cloud', 'bell', 'ship', 'tie']
box_4 = ['star', 'apple']
box_5 = ['toothbrush']
box_6 = ['shelf']
box_7 = []
box_8 = ['camera', 'rock', 'coin']
box_9 = ['usb']
box_10 = ['moon', 'seaweed', 'vase', 'dolphin', 'toy']

# Swap the glove in Box 2 with the shelf in Box 6
box_2[0], box_6[0] = box_6[0], box_2[0]

# Swap the shelf in Box 2 with the frame in Box 1
box_2[0], box_1[0] = box_1[0], box_2[0]

# Swap the toy in Box 10 with the toothbrush in Box 5
box_10[-1], box_5[0] = box_5[0], box_10[-1]

# Remove the apple from Box 4
box_4.remove('apple')

# Remove the bag from Box 0
box_0.remove('bag')

# Put the plate into Box 0
box_0.append('plate')

# Replace the plate with the book in Box 0
box_0[-1] = 'book'

# Remove the book from Box 0
box_0.remove('book')

# Swap the vase in Box 10 with the rock in Box 8
box_10[2], box_8[1] = box_8[1], box_10[2]

# Move the usb from Box 9 to Box 3
box_3.append(box_9.pop())

# Move the toy from Box 5 to Box 4
box_4.append(box_5.pop())

# Put the toy and the laptop into Box 3
box_3.extend(['toy', 'laptop'])

# Move the toy and the star from Box 4 to Box 2
box_2.extend([box_4.pop(), 'toy'])

# Remove the camera and the vase from Box 8
box_8.remove('camera')
box_8.remove('vase')

# Replace the candle and the frame and the button with the flute and the fish and the thunder in Box 2
box_2 = ['flute', 'fish', 'thunder']

# Remove the glove from Box 6
box_6.remove('glove')

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