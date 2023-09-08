# Initial state of boxes
boxes = {
    0: ['wallet'],
    1: ['puzzle', 'microwave'],
    2: ['vase'],
    3: ['mirror', 'shoe', 'grinder', 'zipper'],
    4: ['frame', 'controller', 'chair', 'necklace', 'fork'],
    5: ['lipstick', 'gloves', 'toothpaste', 'blanket'],
    6: ['comet', 'camera', 'rock', 'bag'],
    7: ['laptop', 'bracelet', 'candle', 'ship'],
    8: ['meteor', 'bird'],
    9: ['game'],
    10: ['wig', 'shelf', 'hat', 'thunder', 'toaster'],
    11: ['dice']
}

# Replace the vase with the lock in Box 2.
boxes[2].remove('vase')
boxes[2].append('lock')

# Swap the zipper in Box 3 with the fork in Box 4.
boxes[3].remove('zipper')
boxes[4].remove('fork')
boxes[3].append('fork')
boxes[4].append('zipper')

# Put the starfish into Box 3.
boxes[3].append('starfish')

# Move the thunder and the wig from Box 10 to Box 3.
boxes[10].remove('thunder')
boxes[10].remove('wig')
boxes[3].append('thunder')
boxes[3].append('wig')

# Put the violin into Box 1.
boxes[1].append('violin')

# Remove the laptop and the candle and the ship from Box 7.
boxes[7].remove('laptop')
boxes[7].remove('candle')
boxes[7].remove('ship')

# Swap the puzzle in Box 1 with the wallet in Box 0.
boxes[1].remove('puzzle')
boxes[0].remove('wallet')
boxes[1].append('wallet')
boxes[0].append('puzzle')

# Replace the wallet and the violin and the microwave with the brush and the plate and the shelf in Box 1.
boxes[1].remove('wallet')
boxes[1].remove('violin')
boxes[1].remove('microwave')
boxes[1].append('brush')
boxes[1].append('plate')
boxes[1].append('shelf')

# Put the chair and the controller into Box 7.
boxes[7].append('chair')
boxes[7].append('controller')

# Move the zipper and the chair and the controller from Box 4 to Box 1.
boxes[4].remove('zipper')
boxes[4].remove('chair')
boxes[4].remove('controller')
boxes[1].append('zipper')
boxes[1].append('chair')
boxes[1].append('controller')

# Put the bird into Box 5.
boxes[5].append('bird')

# Swap the shoe in Box 3 with the controller in Box 7.
boxes[3].remove('shoe')
boxes[7].remove('controller')
boxes[3].append('controller')
boxes[7].append('shoe')

# Put the sun into Box 8.
boxes[8].append('sun')

# Move the gloves and the toothpaste and the lipstick from Box 5 to Box 10.
boxes[5].remove('gloves')
boxes[5].remove('toothpaste')
boxes[5].remove('lipstick')
boxes[10].append('gloves')
boxes[10].append('toothpaste')
boxes[10].append('lipstick')

# Move the game from Box 9 to Box 6.
boxes[9].remove('game')
boxes[6].append('game')

# Swap the rock in Box 6 with the dice in Box 11.
boxes[6].remove('rock')
boxes[11].remove('dice')
boxes[6].append('dice')
boxes[11].append('rock')

# Remove the hat and the lipstick and the shelf from Box 10.
boxes[10].remove('hat')
boxes[10].remove('lipstick')
boxes[10].remove('shelf')

# Move the chair and the controller from Box 1 to Box 8.
boxes[1].remove('chair')
boxes[1].remove('controller')
boxes[8].append('chair')
boxes[8].append('controller')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")