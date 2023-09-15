box_0 = ['toy', 'keyboard', 'sock']
box_1 = []
box_2 = ['starfish', 'paint', 'pen']
box_3 = ['apple', 'ship', 'submarine', 'belt']
box_4 = ['oven', 'rock', 'whistle']
box_5 = ['seaweed', 'shampoo', 'pillow']
box_6 = ['usb', 'shoes']
box_7 = ['shirt']
box_8 = []
box_9 = ['blanket', 'comet']
box_10 = ['rain', 'soap']
box_11 = ['planet', 'pants', 'grass', 'swimsuit']

# Move the comet and the blanket from Box 9 to Box 4
box_4.extend([box_9.pop(box_9.index('comet')), box_9.pop(box_9.index('blanket'))])

# Remove the comet and the rock from Box 4
box_4.remove('comet')
box_4.remove('rock')

# Move the apple and the belt from Box 3 to Box 9
box_9.extend([box_3.pop(box_3.index('apple')), box_3.pop(box_3.index('belt'))])

# Move the whistle and the oven from Box 4 to Box 5
box_5.extend([box_4.pop(box_4.index('whistle')), box_4.pop(box_4.index('oven'))])

# Swap the shoes in Box 6 with the rain in Box 10
box_6[box_6.index('shoes')], box_10[box_10.index('rain')] = box_10[box_10.index('rain')], box_6[box_6.index('shoes')]

# Replace the starfish and the pen with the toothbrush and the controller in Box 2
box_2[box_2.index('starfish')] = 'toothbrush'
box_2[box_2.index('pen')] = 'controller'

# Replace the paint and the controller with the necklace and the river in Box 2
box_2[box_2.index('paint')] = 'necklace'
box_2[box_2.index('controller')] = 'river'

# Move the submarine and the ship from Box 3 to Box 8
box_8.extend([box_3.pop(box_3.index('submarine')), box_3.pop(box_3.index('ship'))])

# Put the shirt into Box 6
box_6.append(box_7.pop())

# Remove the shirt from Box 7
box_7.remove('shirt')

# Remove the shoes and the soap from Box 10
box_10.remove('shoes')
box_10.remove('soap')

# Move the grass from Box 11 to Box 9
box_9.append(box_11.pop(box_11.index('grass')))

# Put the scarf and the coat and the helmet into Box 11
box_11.extend(['scarf', 'coat', 'helmet'])

# Empty Box 8
box_8.clear()

# Move the blanket from Box 4 to Box 7
box_7.append(box_4.pop(box_4.index('blanket')))

# Move the seaweed and the shampoo and the oven from Box 5 to Box 6
box_6.extend([box_5.pop(box_5.index('seaweed')), box_5.pop(box_5.index('shampoo')), box_5.pop(box_5.index('oven'))])

# Move the helmet from Box 11 to Box 0
box_0.append(box_11.pop(box_11.index('helmet')))

# Move the swimsuit and the scarf from Box 11 to Box 1
box_1.extend([box_11.pop(box_11.index('swimsuit')), box_11.pop(box_11.index('scarf'))])

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
print("Box 11:", box_11)