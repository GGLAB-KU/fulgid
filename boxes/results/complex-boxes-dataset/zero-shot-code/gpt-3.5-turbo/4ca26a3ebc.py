box_0 = ['vase']
box_1 = ['car', 'fork']
box_2 = ['button', 'toothpaste', 'rain']
box_3 = ['butterfly', 'boat', 'crown']
box_4 = ['branch', 'storm', 'rock', 'wig', 'tiger']
box_5 = ['charger', 'shirt', 'towel', 'table', 'desert']
box_6 = ['perfume', 'glasses', 'lock', 'battery', 'pillow']

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)

# Move the rock, storm, and wig from Box 4 to Box 0
box_0.extend([box_4.pop(box_4.index('rock'))])
box_0.extend([box_4.pop(box_4.index('storm'))])
box_0.extend([box_4.pop(box_4.index('wig'))])

# Put the cow and hat into Box 0
box_0.append('cow')
box_0.append('hat')

# Replace the perfume with the comet in Box 6
box_6[box_6.index('perfume')] = 'comet'

# Remove the hat and storm from Box 0
box_0.remove('hat')
box_0.remove('storm')

# Move the wig from Box 0 to Box 4
box_4.append(box_0.pop(box_0.index('wig')))

# Move the towel and charger from Box 5 to Box 4
box_4.extend([box_5.pop(box_5.index('towel'))])
box_4.extend([box_5.pop(box_5.index('charger'))])

# Move the glasses and comet from Box 6 to Box 4
box_4.extend([box_6.pop(box_6.index('glasses'))])
box_4.extend([box_6.pop(box_6.index('comet'))])

# Move the rock, cow, and vase from Box 0 to Box 4
box_4.extend([box_0.pop(box_0.index('rock'))])
box_4.extend([box_0.pop(box_0.index('cow'))])
box_4.extend([box_0.pop(box_0.index('vase'))])

# Replace the crown and boat with the hat and spoon in Box 3
box_3[box_3.index('crown')] = 'hat'
box_3[box_3.index('boat')] = 'spoon'

# Move the fork from Box 1 to Box 2
box_2.append(box_1.pop(box_1.index('fork')))

# Swap the towel in Box 4 with the rain in Box 2
box_2[box_2.index('rain')], box_4[box_4.index('towel')] = box_4[box_4.index('towel')], box_2[box_2.index('rain')]

# Print the final state of the boxes
print_boxes()