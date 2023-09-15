box_0 = ['dice', 'microscope', 'horn', 'star']
box_1 = ['polish', 'snow', 'jacket', 'starfish']
box_2 = ['cat']
box_3 = ['soap', 'elephant', 'tie', 'camera', 'shoe']
box_4 = ['glasses', 'lipstick', 'bicycle', 'oven']
box_5 = ['butterfly', 'toothpaste', 'battery', 'console', 'lion']
box_6 = ['button', 'boot', 'bus']
box_7 = []
box_8 = ['bracelet', 'pen']
box_9 = []

def print_boxes():
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

# Put the bracelet into Box 6
box_6.append('bracelet')

# Put the shark and the pan into Box 4
box_4.extend(['shark', 'pan'])

# Empty Box 3
box_3.clear()

# Move the console and the battery from Box 5 to Box 4
box_4.extend([box_5.pop(box_5.index('console')), box_5.pop(box_5.index('battery'))])

# Replace the cat with the tie in Box 2
box_2[0] = 'tie'

# Swap the pen in Box 8 with the horn in Box 0
box_8[0], box_0[2] = box_0[2], box_8[0]

# Replace the polish with the book in Box 1
box_1[0] = 'book'

# Swap the tie in Box 2 with the bus in Box 6
box_2[0], box_6[2] = box_6[2], box_2[0]

# Move the horn and the bracelet from Box 8 to Box 6
box_6.extend([box_8.pop(1), box_8.pop(0)])

# Move the bus from Box 2 to Box 0
box_0.append(box_2.pop(0))

# Remove the oven and the bicycle and the shark from Box 4
box_4.remove('oven')
box_4.remove('bicycle')
box_4.remove('shark')

# Swap the console in Box 4 with the toothpaste in Box 5
box_4[3], box_5[1] = box_5[1], box_4[3]

# Put the pants into Box 2
box_2.append('pants')

# Put the glasses and the lock into Box 9
box_9.extend(['glasses', 'lock'])

# Remove the pants from Box 2
box_2.remove('pants')

# Print the final state of the boxes
print_boxes()