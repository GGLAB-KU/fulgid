box_0 = ['helmet', 'speaker']
box_1 = ['bear', 'violin', 'crown', 'tie', 'polish']
box_2 = ['storm', 'scissors', 'pants', 'tree']
box_3 = ['dolphin', 'dice']
box_4 = ['camera']
box_5 = ['piano', 'usb']
box_6 = ['thread', 'wallet']
box_7 = ['bus', 'microwave']

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)
    print("Box 7:", box_7)

# Move the thread from Box 6 to Box 1
box_1.append(box_6.pop(box_6.index('thread')))

# Put the guitar and the shorts and the tree into Box 1
box_1.extend(['guitar', 'shorts', 'tree'])

# Move the wallet from Box 6 to Box 5
box_5.append(box_6.pop(box_6.index('wallet')))

# Move the pants and the scissors from Box 2 to Box 0
box_0.extend([box_2.pop(box_2.index('pants')), box_2.pop(box_2.index('scissors'))])

# Move the tree and the storm from Box 2 to Box 7
box_7.extend([box_2.pop(box_2.index('tree')), box_2.pop(box_2.index('storm'))])

# Move the storm and the bus from Box 7 to Box 4
box_4.extend([box_7.pop(box_7.index('storm')), box_7.pop(box_7.index('bus'))])

# Put the charger into Box 6
box_6.append('charger')

# Replace the tree and the microwave with the seaweed and the polish in Box 7
box_7[box_7.index('tree')] = 'seaweed'
box_7[box_7.index('microwave')] = 'polish'

# Move the charger from Box 6 to Box 1
box_1.append(box_6.pop(box_6.index('charger')))

# Swap the storm in Box 4 with the tie in Box 1
box_1[box_1.index('tie')] = 'storm'
box_4[box_4.index('storm')] = 'tie'

# Move the dolphin and the dice from Box 3 to Box 5
box_5.extend([box_3.pop(box_3.index('dolphin')), box_3.pop(box_3.index('dice'))])

# Put the helmet and the watch into Box 6
box_6.extend(['helmet', 'watch'])

# Print the final state of the boxes
print_boxes()