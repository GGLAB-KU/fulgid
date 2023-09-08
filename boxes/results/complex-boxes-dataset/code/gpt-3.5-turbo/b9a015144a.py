# Initial state of boxes
boxes = {
    0: ['controller'],
    1: [],
    2: ['ring', 'fork', 'zipper'],
    3: ['branch', 'brush'],
    4: ['elephant', 'mask', 'fridge'],
    5: ['pants'],
    6: ['necklace', 'comb', 'candle', 'wire', 'tiger'],
    7: ['mountain', 'phone', 'bicycle', 'lipstick', 'shoe'],
    8: ['skirt', 'microscope', 'train', 'crown', 'meteor'],
    9: ['jungle', 'snow', 'hat'],
    10: ['card', 'bracelet', 'key', 'umbrella'],
    11: ['gloves', 'horn', 'bowl', 'lamp'],
    12: ['pillow', 'watch', 'helmet'],
    13: ['bus', 'bear', 'boot', 'bird', 'clock'],
    14: ['charger']
}

# Remove the pants from Box 5.
boxes[5].remove('pants')

# Remove the bicycle from Box 7.
boxes[7].remove('bicycle')

# Swap the tiger in Box 6 with the elephant in Box 4.
boxes[6].remove('tiger')
boxes[4].remove('elephant')
boxes[6].append('elephant')
boxes[4].append('tiger')

# Swap the candle in Box 6 with the meteor in Box 8.
boxes[6].remove('candle')
boxes[8].remove('meteor')
boxes[6].append('meteor')
boxes[8].append('candle')

# Move the umbrella and the card from Box 10 to Box 13.
boxes[10].remove('umbrella')
boxes[10].remove('card')
boxes[13].append('umbrella')
boxes[13].append('card')

# Replace the helmet and the watch with the planet and the starfish in Box 12.
boxes[12].remove('helmet')
boxes[12].remove('watch')
boxes[12].append('planet')
boxes[12].append('starfish')

# Replace the bear and the bird with the console and the puzzle in Box 13.
boxes[13].remove('bear')
boxes[13].remove('bird')
boxes[13].append('console')
boxes[13].append('puzzle')

# Remove the horn and the gloves and the bowl from Box 11.
boxes[11].remove('horn')
boxes[11].remove('gloves')
boxes[11].remove('bowl')

# Swap the charger in Box 14 with the mountain in Box 7.
boxes[14].remove('charger')
boxes[7].remove('mountain')
boxes[14].append('mountain')
boxes[7].append('charger')

# Remove the necklace and the wire from Box 6.
boxes[6].remove('necklace')
boxes[6].remove('wire')

# Empty Box 8.
boxes[8] = []

# Move the starfish and the pillow from Box 12 to Box 4.
boxes[12].remove('starfish')
boxes[12].remove('pillow')
boxes[4].append('starfish')
boxes[4].append('pillow')

# Swap the zipper in Box 2 with the puzzle in Box 13.
boxes[2].remove('zipper')
boxes[13].remove('puzzle')
boxes[2].append('puzzle')
boxes[13].append('zipper')

# Swap the boot in Box 13 with the shoe in Box 7.
boxes[13].remove('boot')
boxes[7].remove('shoe')
boxes[13].append('shoe')
boxes[7].append('boot')

# Swap the meteor in Box 6 with the planet in Box 12.
boxes[6].remove('meteor')
boxes[12].remove('planet')
boxes[6].append('planet')
boxes[12].append('meteor')

# Empty Box 4.
boxes[4] = []

# Swap the controller in Box 0 with the clock in Box 13.
boxes[0].remove('controller')
boxes[13].remove('clock')
boxes[0].append('clock')
boxes[13].append('controller')

# Move the mountain from Box 14 to Box 5.
boxes[14].remove('mountain')
boxes[5].append('mountain')

# Remove the key from Box 10.
boxes[10].remove('key')

# Replace the ring and the puzzle and the fork with the sandals and the bicycle and the soap in Box 2.
boxes[2].remove('ring')
boxes[2].remove('puzzle')
boxes[2].remove('fork')
boxes[2].append('sandals')
boxes[2].append('bicycle')
boxes[2].append('soap')

# Move the bicycle from Box 2 to Box 7.
boxes[2].remove('bicycle')
boxes[7].append('bicycle')

# Remove the lamp from Box 11.
boxes[11].remove('lamp')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")