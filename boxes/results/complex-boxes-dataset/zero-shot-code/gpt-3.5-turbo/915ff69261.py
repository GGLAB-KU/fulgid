box_0 = ['dog', 'scarf', 'sandals']
box_1 = ['toothbrush', 'submarine', 'earring', 'dolphin', 'lipstick']
box_2 = ['wig', 'frame', 'lightning', 'fridge']
box_3 = ['coral', 'ocean', 'tiger']
box_4 = []
box_5 = []
box_6 = ['cow', 'pot', 'horn', 'apple']
box_7 = ['grass', 'toaster', 'beach', 'table']
box_8 = ['fish', 'zipper', 'crown', 'basket', 'puzzle']
box_9 = ['thunder', 'dice', 'shelf', 'mirror']
box_10 = ['bag', 'microwave', 'dress']

# Remove the wig from Box 2
box_2.remove('wig')

# Move the microwave and the bag from Box 10 to Box 7
box_7.extend([box_10.pop(box_10.index('microwave')), box_10.pop(box_10.index('bag'))])

# Swap the table in Box 7 with the sandals in Box 0
box_7[box_7.index('table')], box_0[box_0.index('sandals')] = box_0[box_0.index('sandals')], box_7[box_7.index('table')]

# Move the pot and the apple and the horn from Box 6 to Box 10
box_10.extend([box_6.pop(box_6.index('pot')), box_6.pop(box_6.index('apple')), box_6.pop(box_6.index('horn'))])

# Put the leaf and the phone and the sun into Box 2
box_2.extend(['leaf', 'phone', 'sun'])

# Move the frame from Box 2 to Box 3
box_3.append(box_2.pop(box_2.index('frame')))

# Remove the dog and the table and the scarf from Box 0
box_0.remove('dog')
box_0.remove('table')
box_0.remove('scarf')

# Replace the lightning with the table in Box 2
box_2[box_2.index('lightning')] = 'table'

# Move the cow from Box 6 to Box 10
box_10.append(box_6.pop(box_6.index('cow')))

# Move the puzzle and the fish from Box 8 to Box 4
box_4.extend([box_8.pop(box_8.index('puzzle')), box_8.pop(box_8.index('fish'))])

# Put the shirt and the usb into Box 6
box_6.extend(['shirt', 'usb'])

# Empty Box 7
box_7.clear()

# Remove the coral and the frame and the tiger from Box 3
box_3.remove('coral')
box_3.remove('frame')
box_3.remove('tiger')

# Swap the apple in Box 10 with the usb in Box 6
box_10[box_10.index('apple')], box_6[box_6.index('usb')] = box_6[box_6.index('usb')], box_10[box_10.index('apple')]

# Move the dice and the thunder and the mirror from Box 9 to Box 10
box_10.extend([box_9.pop(box_9.index('dice')), box_9.pop(box_9.index('thunder')), box_9.pop(box_9.index('mirror'))])

# Remove the fish and the puzzle from Box 4
box_4.remove('fish')
box_4.remove('puzzle')

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