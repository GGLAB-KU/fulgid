box_0 = ['shoes', 'mask']
box_1 = ['forest']
box_2 = []
box_3 = ['horn', 'harmonica', 'flower']
box_4 = ['toothbrush', 'usb']
box_5 = ['hat', 'phone', 'dog', 'frame']
box_6 = ['lion', 'starfish']
box_7 = ['headphone']
box_8 = ['cup', 'cat', 'speaker', 'guitar', 'snow']
box_9 = ['helmet', 'lipstick', 'shirt', 'shoe', 'coral']

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

# Move the forest from Box 1 to Box 7
box_7.append(box_1.pop(0))

# Swap the usb in Box 4 with the mask in Box 0
box_0[0], box_4[1] = box_4[1], box_0[0]

# Move the mask from Box 4 to Box 1
box_1.append(box_4.pop(0))

# Move the shoes and the usb from Box 0 to Box 9
box_9.extend(box_0)
box_0.clear()

# Put the charger and the tiger and the necklace into Box 9
box_9.extend(['charger', 'tiger', 'necklace'])

# Put the violin and the bell and the pants into Box 3
box_3.extend(['violin', 'bell', 'pants'])

# Move the flower and the bell from Box 3 to Box 7
box_7.extend([box_3.pop(2), box_3.pop(2)])

# Replace the hat and the phone with the telescope and the watch in Box 5
box_5[0] = 'telescope'
box_5[1] = 'watch'

# Move the violin and the pants from Box 3 to Box 4
box_4.extend([box_3.pop(2), box_3.pop(2)])

# Move the toothbrush and the pants and the violin from Box 4 to Box 9
box_9.extend([box_4.pop(0), box_4.pop(1), box_4.pop(2)])

# Swap the shoes in Box 9 with the mask in Box 1
box_1[0], box_9[3] = box_9[3], box_1[0]

# Move the telescope from Box 5 to Box 2
box_2.append(box_5.pop(0))

# Replace the harmonica and the horn with the coin and the shoe in Box 3
box_3[0] = 'coin'
box_3[1] = 'shoe'

# Replace the frame and the dog and the watch with the shampoo and the controller and the jungle in Box 5
box_5[0] = 'shampoo'
box_5[1] = 'controller'
box_5[2] = 'jungle'

# Replace the shampoo with the key in Box 5
box_5[0] = 'key'

print("\nAfter modifications:")
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