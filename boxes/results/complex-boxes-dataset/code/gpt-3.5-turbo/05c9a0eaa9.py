# Initial state of boxes
boxes = {
    0: ['grinder', 'bracelet', 'glove'],
    1: ['boot', 'star', 'cup', 'jungle'],
    2: ['bus'],
    3: ['desert', 'guitar', 'headphone', 'shoe'],
    4: ['hat'],
    5: [],
    6: ['speaker'],
    7: ['train', 'key'],
    8: ['polish', 'console', 'butterfly', 'helmet'],
    9: ['sun', 'storm', 'rock'],
    10: ['pillow', 'shorts'],
    11: [],
    12: [],
    13: [],
    14: ['thunder', 'necklace']
}

# Move the polish and the console from Box 8 to Box 9.
boxes[8].remove('polish')
boxes[8].remove('console')
boxes[9].append('polish')
boxes[9].append('console')

# Remove the hat from Box 4.
boxes[4].remove('hat')

# Replace the grinder with the soap in Box 0.
boxes[0].remove('grinder')
boxes[0].append('soap')

# Put the basket and the desert into Box 4.
boxes[4].append('basket')
boxes[4].append('desert')

# Replace the desert and the headphone and the shoe with the beach and the keyboard and the pants in Box 3.
boxes[3].remove('desert')
boxes[3].remove('headphone')
boxes[3].remove('shoe')
boxes[3].append('beach')
boxes[3].append('keyboard')
boxes[3].append('pants')

# Put the watch and the plate and the umbrella into Box 9.
boxes[9].append('watch')
boxes[9].append('plate')
boxes[9].append('umbrella')

# Swap the speaker in Box 6 with the butterfly in Box 8.
boxes[6].remove('speaker')
boxes[8].remove('butterfly')
boxes[6].append('butterfly')
boxes[8].append('speaker')

# Move the bus from Box 2 to Box 14.
boxes[2].remove('bus')
boxes[14].append('bus')

# Put the car and the pen into Box 0.
boxes[0].append('car')
boxes[0].append('pen')

# Replace the helmet and the speaker with the lamp and the comet in Box 8.
boxes[8].remove('helmet')
boxes[8].remove('speaker')
boxes[8].append('lamp')
boxes[8].append('comet')

# Remove the pants and the guitar and the keyboard from Box 3.
boxes[3].remove('pants')
boxes[3].remove('guitar')
boxes[3].remove('keyboard')

# Move the desert and the basket from Box 4 to Box 12.
boxes[4].remove('desert')
boxes[4].remove('basket')
boxes[12].append('desert')
boxes[12].append('basket')

# Swap the cup in Box 1 with the train in Box 7.
boxes[1].remove('cup')
boxes[7].remove('train')
boxes[1].append('train')
boxes[7].append('cup')

# Remove the comet and the lamp from Box 8.
boxes[8].remove('comet')
boxes[8].remove('lamp')

# Move the thunder and the bus and the necklace from Box 14 to Box 11.
boxes[14].remove('thunder')
boxes[14].remove('bus')
boxes[14].remove('necklace')
boxes[11].append('thunder')
boxes[11].append('bus')
boxes[11].append('necklace')

# Swap the bus in Box 11 with the car in Box 0.
boxes[11].remove('bus')
boxes[0].remove('car')
boxes[11].append('car')
boxes[0].append('bus')

# Replace the star and the boot and the train with the boat and the truck and the grinder in Box 1.
boxes[1].remove('star')
boxes[1].remove('boot')
boxes[1].remove('train')
boxes[1].append('boat')
boxes[1].append('truck')
boxes[1].append('grinder')

# Put the gloves into Box 8.
boxes[8].append('gloves')

# Put the dog and the earring and the branch into Box 13.
boxes[13].append('dog')
boxes[13].append('earring')
boxes[13].append('branch')

# Put the lightning into Box 13.
boxes[13].append('lightning')

# Move the truck and the grinder and the boat from Box 1 to Box 11.
boxes[1].remove('truck')
boxes[1].remove('grinder')
boxes[1].remove('boat')
boxes[11].append('truck')
boxes[11].append('grinder')
boxes[11].append('boat')

# Move the butterfly from Box 6 to Box 10.
boxes[6].remove('butterfly')
boxes[10].append('butterfly')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")