box_0 = ['desert', 'apple', 'rain', 'star']
box_1 = ['necklace', 'beach', 'game']
box_2 = ['towel']
box_3 = ['pot', 'candle', 'shoe']
box_4 = ['wallet', 'branch', 'freezer', 'bird', 'guitar']
box_5 = ['dice', 'shoes', 'scissors']
box_6 = ['glasses', 'leaf', 'polish']
box_7 = ['toaster', 'blanket', 'whistle']
box_8 = ['toothbrush', 'boat', 'umbrella']
box_9 = ['telescope']
box_10 = ['jungle', 'bicycle']
box_11 = ['sun']
box_12 = ['phone', 'starfish', 'button', 'boot', 'puzzle']
box_13 = ['basket', 'pan']

# Move the bird from Box 4 to Box 3
box_3.append(box_4.pop(box_4.index('bird')))

# Remove the bicycle from Box 10
box_10.remove('bicycle')

# Swap the boat in Box 8 with the dice in Box 5
box_8[box_8.index('boat')], box_5[box_5.index('dice')] = box_5[box_5.index('dice')], box_8[box_8.index('boat')]

# Replace the telescope with the island in Box 9
box_9[box_9.index('telescope')] = 'island'

# Move the pan and the basket from Box 13 to Box 7
box_7.extend([box_13.pop(box_13.index('pan')), box_13.pop(box_13.index('basket'))])

# Put the jungle and the thunder and the microwave into Box 2
box_2.extend(['jungle', 'thunder', 'microwave'])

# Move the toothbrush and the umbrella from Box 8 to Box 3
box_3.extend([box_8.pop(box_8.index('toothbrush')), box_8.pop(box_8.index('umbrella'))])

# Replace the bird and the pot and the shoe with the puzzle and the forest and the blender in Box 3
box_3.extend(['puzzle', 'forest', 'blender'])
box_3.remove('bird')
box_3.remove('pot')
box_3.remove('shoe')

# Remove the dice from Box 8
box_8.remove('dice')

# Replace the island with the perfume in Box 9
box_9[box_9.index('island')] = 'perfume'

# Replace the shoes and the scissors with the sandals and the watch in Box 5
box_5[box_5.index('shoes')] = 'sandals'
box_5[box_5.index('scissors')] = 'watch'

# Remove the sun from Box 11
box_11.remove('sun')

# Move the candle and the blender and the forest from Box 3 to Box 2
box_2.extend([box_3.pop(box_3.index('candle')), box_3.pop(box_3.index('blender')), box_3.pop(box_3.index('forest'))])

# Put the headphone into Box 6
box_6.append('headphone')

# Empty Box 6
box_6 = []

# Replace the beach and the game and the necklace with the bicycle and the harmonica and the toothbrush in Box 1
box_1.extend(['bicycle', 'harmonica', 'toothbrush'])
box_1.remove('beach')
box_1.remove('game')
box_1.remove('necklace')

# Remove the blanket and the pan and the toaster from Box 7
box_7.remove('blanket')
box_7.remove('pan')
box_7.remove('toaster')

# Replace the umbrella and the puzzle with the rain and the flower in Box 3
box_3[box_3.index('umbrella')] = 'rain'
box_3[box_3.index('puzzle')] = 'flower'

# Put the hat and the whistle and the butterfly into Box 4
box_4.extend(['hat', 'whistle', 'butterfly'])

# Swap the perfume in Box 9 with the freezer in Box 4
box_9[box_9.index('perfume')], box_4[box_4.index('freezer')] = box_4[box_4.index('freezer')], box_9[box_9.index('perfume')]

# Put the table into Box 13
box_13.append('table')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")