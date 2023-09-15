box_0 = ['starfish', 'bag']
box_1 = ['paint', 'beach']
box_2 = ['shorts']
box_3 = ['bird', 'shirt', 'rocket']
box_4 = ['microwave', 'forest']

# Replace the paint with the bicycle in Box 1
box_1[box_1.index('paint')] = 'bicycle'

# Move the microwave from Box 4 to Box 1
box_1.append(box_4.pop(box_4.index('microwave')))

# Replace the shorts with the whistle in Box 2
box_2[box_2.index('shorts')] = 'whistle'

# Put the keyboard and the fish and the helmet into Box 0
box_0.extend(['keyboard', 'fish', 'helmet'])

# Remove the bird from Box 3
box_3.remove('bird')

# Swap the microwave in Box 1 with the starfish in Box 0
box_0[box_0.index('helmet')], box_1[box_1.index('microwave')] = box_1[box_1.index('microwave')], box_0[box_0.index('helmet')]

# Swap the helmet in Box 0 with the shirt in Box 3
box_0[box_0.index('helmet')], box_3[box_3.index('shirt')] = box_3[box_3.index('shirt')], box_0[box_0.index('helmet')]

# Swap the beach in Box 1 with the helmet in Box 3
box_1[box_1.index('beach')], box_3[box_3.index('helmet')] = box_3[box_3.index('helmet')], box_1[box_1.index('beach')]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)