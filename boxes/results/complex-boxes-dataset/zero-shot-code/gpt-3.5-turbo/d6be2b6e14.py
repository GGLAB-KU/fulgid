box_0 = ['wallet']
box_1 = ['puzzle', 'microwave']
box_2 = ['vase']
box_3 = ['mirror', 'shoe', 'grinder', 'zipper']
box_4 = ['frame', 'controller', 'chair', 'necklace', 'fork']
box_5 = ['lipstick', 'gloves', 'toothpaste', 'blanket']
box_6 = ['comet', 'camera', 'rock', 'bag']
box_7 = ['laptop', 'bracelet', 'candle', 'ship']
box_8 = ['meteor', 'bird']
box_9 = ['game']
box_10 = ['wig', 'shelf', 'hat', 'thunder', 'toaster']
box_11 = ['dice']

# Replace the vase with the lock in Box 2
box_2 = ['lock']

# Swap the zipper in Box 3 with the fork in Box 4
box_3[3], box_4[4] = box_4[4], box_3[3]

# Put the starfish into Box 3
box_3.append('starfish')

# Move the thunder and the wig from Box 10 to Box 3
box_10.remove('thunder')
box_10.remove('wig')
box_3.extend(['thunder', 'wig'])

# Put the violin into Box 1
box_1.append('violin')

# Remove the laptop and the candle and the ship from Box 7
box_7.remove('laptop')
box_7.remove('candle')
box_7.remove('ship')

# Swap the puzzle in Box 1 with the wallet in Box 0
box_0[0], box_1[0] = box_1[0], box_0[0]

# Replace the wallet and the violin and the microwave with the brush and the plate and the shelf in Box 1
box_1 = ['brush', 'plate', 'shelf']

# Put the chair and the controller into Box 7
box_7.extend(['chair', 'controller'])

# Move the zipper and the chair and the controller from Box 4 to Box 1
box_4.remove('zipper')
box_4.remove('chair')
box_4.remove('controller')
box_1.extend(['zipper', 'chair', 'controller'])

# Put the bird into Box 5
box_5.append('bird')

# Swap the shoe in Box 3 with the controller in Box 7
box_3[1], box_7[3] = box_7[3], box_3[1]

# Put the sun into Box 8
box_8.append('sun')

# Move the gloves and the toothpaste and the lipstick from Box 5 to Box 10
box_5.remove('gloves')
box_5.remove('toothpaste')
box_5.remove('lipstick')
box_10.extend(['gloves', 'toothpaste', 'lipstick'])

# Move the game from Box 9 to Box 6
box_9.remove('game')
box_6.append('game')

# Swap the rock in Box 6 with the dice in Box 11
box_6[2], box_11[0] = box_11[0], box_6[2]

# Remove the hat and the lipstick and the shelf from Box 10
box_10.remove('hat')
box_10.remove('lipstick')
box_10.remove('shelf')

# Move the chair and the controller from Box 1 to Box 8
box_1.remove('chair')
box_1.remove('controller')
box_8.extend(['chair', 'controller'])

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")