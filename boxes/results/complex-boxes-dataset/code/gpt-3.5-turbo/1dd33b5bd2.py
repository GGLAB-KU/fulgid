# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['freezer', 'guitar'],
    3: ['table', 'blender', 'spoon'],
    4: ['glasses'],
    5: ['pen', 'necklace', 'wire'],
    6: ['lion', 'horse', 'shampoo'],
    7: ['camera', 'perfume', 'charger', 'boat'],
    8: ['bracelet', 'plate'],
    9: ['sandals', 'fridge'],
    10: ['boot'],
    11: ['razor', 'car', 'beach'],
    12: [],
    13: ['watch'],
    14: ['grass']
}

# Remove the boot from Box 10.
boxes[10].remove('boot')

# Move the grass from Box 14 to Box 0.
boxes[14].remove('grass')
boxes[0].append('grass')

# Swap the plate in Box 8 with the spoon in Box 3.
boxes[8].remove('plate')
boxes[3].remove('spoon')
boxes[8].append('spoon')
boxes[3].append('plate')

# Replace the shampoo and the lion and the horse with the coat and the blanket and the dog in Box 6.
boxes[6].remove('shampoo')
boxes[6].remove('lion')
boxes[6].remove('horse')
boxes[6].append('coat')
boxes[6].append('blanket')
boxes[6].append('dog')

# Replace the guitar with the fish in Box 2.
boxes[2].remove('guitar')
boxes[2].append('fish')

# Remove the car and the razor from Box 11.
boxes[11].remove('car')
boxes[11].remove('razor')

# Put the spoon and the lamp and the microwave into Box 2.
boxes[3].remove('spoon')
boxes[2].append('spoon')
boxes[2].append('lamp')
boxes[2].append('microwave')

# Put the truck and the grass into Box 1.
boxes[1].append('truck')
boxes[14].remove('grass')
boxes[1].append('grass')

# Put the cow and the river and the fork into Box 3.
boxes[3].append('cow')
boxes[3].append('river')
boxes[3].append('fork')

# Put the violin and the camera and the frame into Box 5.
boxes[5].append('violin')
boxes[7].remove('camera')
boxes[5].append('camera')
boxes[5].append('frame')

# Replace the fridge with the train in Box 9.
boxes[9].remove('fridge')
boxes[9].append('train')

# Move the grass from Box 0 to Box 2.
boxes[0].remove('grass')
boxes[2].append('grass')

# Remove the charger from Box 7.
boxes[7].remove('charger')

# Remove the lamp and the spoon from Box 2.
boxes[2].remove('lamp')
boxes[2].remove('spoon')

# Put the jungle and the meteor and the headphone into Box 2.
boxes[2].append('jungle')
boxes[2].append('meteor')
boxes[2].append('headphone')

# Put the horn and the book and the moon into Box 9.
boxes[9].append('horn')
boxes[9].append('book')
boxes[9].append('moon')

# Remove the sandals from Box 9.
boxes[9].remove('sandals')

# Swap the jungle in Box 2 with the horn in Box 9.
boxes[2].remove('jungle')
boxes[9].remove('horn')
boxes[2].append('horn')
boxes[9].append('jungle')

# Move the glasses from Box 4 to Box 1.
boxes[4].remove('glasses')
boxes[1].append('glasses')

# Replace the beach with the keyboard in Box 11.
boxes[11].remove('beach')
boxes[11].append('keyboard')

# Remove the pen and the camera and the frame from Box 5.
boxes[5].remove('pen')
boxes[5].remove('camera')
boxes[5].remove('frame')

# Remove the freezer from Box 2.
boxes[2].remove('freezer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")