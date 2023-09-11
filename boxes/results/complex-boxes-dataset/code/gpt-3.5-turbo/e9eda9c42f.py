# Initial state of boxes
boxes = {
    0: ['seaweed', 'rock'],
    1: [],
    2: ['game'],
    3: [],
    4: ['ocean', 'octopus'],
    5: ['lock', 'button', 'soap', 'book'],
    6: ['sculpture', 'needle', 'piano'],
    7: ['dog', 'crown'],
    8: ['battery', 'candle'],
    9: ['snow', 'scarf'],
    10: ['fridge']
}

# Put the laptop and the scarf and the headphone into Box 6.
boxes[6].append('laptop')
boxes[6].append('scarf')
boxes[6].append('headphone')

# Move the scarf from Box 9 to Box 3.
boxes[9].remove('scarf')
boxes[3].append('scarf')

# Replace the rock and the seaweed with the helmet and the speaker in Box 0.
boxes[0].remove('rock')
boxes[0].remove('seaweed')
boxes[0].append('helmet')
boxes[0].append('speaker')

# Remove the snow from Box 9.
boxes[9].remove('snow')

# Empty Box 10.
boxes[10] = []

# Put the plate and the card into Box 7.
boxes[7].append('plate')
boxes[7].append('card')

# Swap the game in Box 2 with the plate in Box 7.
boxes[2].remove('game')
boxes[7].remove('plate')
boxes[2].append('plate')
boxes[7].append('game')

# Remove the octopus from Box 4.
boxes[4].remove('octopus')

# Replace the helmet and the speaker with the bowl and the blender in Box 0.
boxes[0].remove('helmet')
boxes[0].remove('speaker')
boxes[0].append('bowl')
boxes[0].append('blender')

# Move the battery and the candle from Box 8 to Box 2.
boxes[8].remove('battery')
boxes[8].remove('candle')
boxes[2].append('battery')
boxes[2].append('candle')

# Put the bear and the coat into Box 5.
boxes[5].append('bear')
boxes[5].append('coat')

# Remove the headphone and the scarf from Box 6.
boxes[6].remove('headphone')
boxes[6].remove('scarf')

# Swap the bowl in Box 0 with the book in Box 5.
boxes[0].remove('bowl')
boxes[5].remove('book')
boxes[0].append('book')
boxes[5].append('bowl')

# Move the book from Box 0 to Box 4.
boxes[0].remove('book')
boxes[4].append('book')

# Move the sculpture and the piano from Box 6 to Box 5.
boxes[6].remove('sculpture')
boxes[6].remove('piano')
boxes[5].append('sculpture')
boxes[5].append('piano')

# Swap the plate in Box 2 with the book in Box 4.
boxes[2].remove('plate')
boxes[4].remove('book')
boxes[2].append('book')
boxes[4].append('plate')

# Swap the dog in Box 7 with the needle in Box 6.
boxes[7].remove('dog')
boxes[6].remove('needle')
boxes[7].append('needle')
boxes[6].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")