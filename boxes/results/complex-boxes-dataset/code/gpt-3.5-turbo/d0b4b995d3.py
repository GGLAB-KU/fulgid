# Initial state of boxes
boxes = {
    0: ['planet', 'octopus'],
    1: ['fridge', 'makeup', 'zipper', 'coin'],
    2: ['piano', 'doll', 'fork', 'car'],
    3: ['razor', 'moon'],
    4: ['island', 'coat', 'shampoo', 'horse'],
    5: ['flute', 'thunder'],
    6: ['butterfly', 'shelf', 'microwave', 'coral'],
    7: ['glasses', 'lion'],
    8: ['game', 'umbrella', 'scissors', 'pan', 'glove'],
    9: ['tie', 'grinder', 'meteor'],
    10: [],
    11: ['sculpture', 'microscope', 'thread', 'watch', 'headphone'],
    12: ['motorcycle', 'starfish', 'sock', 'lightning', 'earring'],
    13: [],
    14: ['toaster', 'phone']
}

# Replace the lion with the scissors in Box 7.
boxes[7].remove('lion')
boxes[7].append('scissors')

# Remove the scissors and the glasses from Box 7.
boxes[7].remove('scissors')
boxes[7].remove('glasses')

# Replace the shampoo and the coat and the island with the piano and the desert and the cow in Box 4.
boxes[4].remove('shampoo')
boxes[4].remove('coat')
boxes[4].remove('island')
boxes[4].append('piano')
boxes[4].append('desert')
boxes[4].append('cow')

# Replace the meteor with the camera in Box 9.
boxes[9].remove('meteor')
boxes[9].append('camera')

# Move the starfish and the earring from Box 12 to Box 13.
boxes[12].remove('starfish')
boxes[12].remove('earring')
boxes[13].append('starfish')
boxes[13].append('earring')

# Replace the pan and the game with the comet and the paint in Box 8.
boxes[8].remove('pan')
boxes[8].remove('game')
boxes[8].append('comet')
boxes[8].append('paint')

# Replace the toaster with the tiger in Box 14.
boxes[14].remove('toaster')
boxes[14].append('tiger')

# Replace the paint and the umbrella with the moon and the thunder in Box 8.
boxes[8].remove('paint')
boxes[8].remove('umbrella')
boxes[8].append('moon')
boxes[8].append('thunder')

# Remove the moon and the comet from Box 8.
boxes[8].remove('moon')
boxes[8].remove('comet')

# Move the camera and the grinder from Box 9 to Box 4.
boxes[9].remove('camera')
boxes[9].remove('grinder')
boxes[4].append('camera')
boxes[4].append('grinder')

# Put the lion and the console into Box 0.
boxes[0].append('lion')
boxes[0].append('console')

# Put the gloves into Box 14.
boxes[14].append('gloves')

# Remove the piano from Box 4.
boxes[4].remove('piano')

# Remove the car from Box 2.
boxes[2].remove('car')

# Put the microwave into Box 4.
boxes[4].append('microwave')

# Replace the razor with the motorcycle in Box 3.
boxes[3].remove('razor')
boxes[3].append('motorcycle')

# Swap the watch in Box 11 with the octopus in Box 0.
boxes[11].remove('watch')
boxes[0].remove('octopus')
boxes[11].append('octopus')
boxes[0].append('watch')

# Swap the fork in Box 2 with the cow in Box 4.
boxes[2].remove('fork')
boxes[4].remove('cow')
boxes[2].append('cow')
boxes[4].append('fork')

# Remove the thunder and the scissors from Box 8.
boxes[8].remove('thunder')
boxes[8].remove('scissors')

# Remove the thunder and the flute from Box 5.
boxes[5].remove('thunder')
boxes[5].remove('flute')

# Remove the phone and the tiger from Box 14.
boxes[14].remove('phone')
boxes[14].remove('tiger')

# Put the clock and the seaweed into Box 12.
boxes[12].append('clock')
boxes[12].append('seaweed')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")