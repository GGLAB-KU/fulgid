box_0 = ['freezer', 'telescope', 'dice']
box_1 = ['clock', 'bowl', 'scissors', 'keyboard']
box_2 = ['apple', 'guitar', 'coat', 'hat', 'sock']
box_3 = ['fridge', 'frame', 'microwave', 'violin', 'scarf']
box_4 = []
box_5 = ['cat', 'game', 'vase', 'crown', 'gloves']
box_6 = ['lion', 'seaweed']
box_7 = []
box_8 = ['pillow']
box_9 = []
box_10 = ['octopus', 'rocket', 'toothpaste', 'shorts']

# Remove the frame and the scarf from Box 3
box_3.remove('frame')
box_3.remove('scarf')

# Put the sandals and the lightning and the game into Box 4
box_4.extend(['sandals', 'lightning', 'game'])

# Put the scarf and the sandals and the mixer into Box 4
box_4.extend(['scarf', 'sandals', 'mixer'])

# Swap the octopus in Box 10 with the fridge in Box 3
box_10.remove('octopus')
box_3.remove('fridge')
box_10.append('fridge')
box_3.append('octopus')

# Put the brush and the umbrella into Box 2
box_2.extend(['brush', 'umbrella'])

# Move the telescope and the dice from Box 0 to Box 1
box_1.extend(['telescope', 'dice'])
box_0.remove('telescope')
box_0.remove('dice')

# Remove the fridge and the toothpaste and the shorts from Box 10
box_10.remove('fridge')
box_10.remove('toothpaste')
box_10.remove('shorts')

# Move the apple and the hat and the guitar from Box 2 to Box 8
box_8.extend(['apple', 'hat', 'guitar'])
box_2.remove('apple')
box_2.remove('hat')
box_2.remove('guitar')

# Swap the sock in Box 2 with the scarf in Box 4
box_2.remove('sock')
box_4.remove('scarf')
box_2.append('scarf')
box_4.append('sock')

# Remove the guitar and the apple and the hat from Box 8
box_8.remove('guitar')
box_8.remove('apple')
box_8.remove('hat')

# Remove the microwave and the octopus from Box 3
box_3.remove('microwave')
box_3.remove('octopus')

# Empty Box 6
box_6.clear()

# Swap the crown in Box 5 with the pillow in Box 8
box_5.remove('crown')
box_8.remove('pillow')
box_5.append('pillow')
box_8.append('crown')

# Move the rocket from Box 10 to Box 3
box_3.append('rocket')
box_10.remove('rocket')

# Move the vase from Box 5 to Box 7
box_7.append('vase')
box_5.remove('vase')

# Replace the crown with the dice in Box 8
box_8.remove('crown')
box_8.append('dice')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]):
    print(f"Box {i}: {box}")