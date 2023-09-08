# Initial state of boxes
boxes = {
    0: ['razor', 'laptop', 'dress'],
    1: ['car', 'submarine'],
    2: ['fridge', 'apple', 'rocket', 'pen', 'chair'],
    3: [],
    4: ['card', 'bell', 'lion'],
    5: ['cat'],
    6: ['lipstick', 'blender', 'sculpture', 'usb'],
    7: ['ship', 'bicycle', 'telescope', 'makeup'],
    8: ['microscope'],
    9: [],
    10: ['spoon', 'boot', 'frame'],
    11: [],
    12: ['needle']
}

# Swap the chair in Box 2 with the cat in Box 5.
boxes[2].remove('chair')
boxes[5].remove('cat')
boxes[2].append('cat')
boxes[5].append('chair')

# Replace the submarine and the car with the glasses and the pillow in Box 1.
boxes[1].remove('submarine')
boxes[1].remove('car')
boxes[1].append('glasses')
boxes[1].append('pillow')

# Move the bell and the lion from Box 4 to Box 9.
boxes[4].remove('bell')
boxes[4].remove('lion')
boxes[9].append('bell')
boxes[9].append('lion')

# Swap the needle in Box 12 with the dress in Box 0.
boxes[12].remove('needle')
boxes[0].remove('dress')
boxes[12].append('dress')
boxes[0].append('needle')

# Move the lion from Box 9 to Box 1.
boxes[9].remove('lion')
boxes[1].append('lion')

# Empty Box 10.
boxes[10] = []

# Move the chair from Box 5 to Box 1.
boxes[5].remove('chair')
boxes[1].append('chair')

# Put the coat into Box 6.
boxes[6].append('coat')

# Swap the card in Box 4 with the makeup in Box 7.
boxes[4].remove('card')
boxes[7].remove('makeup')
boxes[4].append('makeup')
boxes[7].append('card')

# Move the microscope from Box 8 to Box 5.
boxes[8].remove('microscope')
boxes[5].append('microscope')

# Move the pillow and the lion from Box 1 to Box 8.
boxes[1].remove('pillow')
boxes[1].remove('lion')
boxes[8].append('pillow')
boxes[8].append('lion')

# Move the bicycle and the ship and the telescope from Box 7 to Box 11.
boxes[7].remove('bicycle')
boxes[7].remove('ship')
boxes[7].remove('telescope')
boxes[11].append('bicycle')
boxes[11].append('ship')
boxes[11].append('telescope')

# Move the bell from Box 9 to Box 7.
boxes[9].remove('bell')
boxes[7].append('bell')

# Swap the dress in Box 12 with the card in Box 7.
boxes[12].remove('dress')
boxes[7].remove('card')
boxes[12].append('card')
boxes[7].append('dress')

# Replace the makeup with the shorts in Box 4.
boxes[4].remove('makeup')
boxes[4].append('shorts')

# Put the boot and the glove into Box 3.
boxes[3].append('boot')
boxes[3].append('glove')

# Replace the needle and the razor and the laptop with the wig and the blender and the phone in Box 0.
boxes[0].remove('needle')
boxes[0].remove('razor')
boxes[0].remove('laptop')
boxes[0].append('wig')
boxes[0].append('blender')
boxes[0].append('phone')

# Replace the card with the flute in Box 12.
boxes[12].remove('card')
boxes[12].append('flute')

# Remove the telescope and the ship and the bicycle from Box 11.
boxes[11].remove('telescope')
boxes[11].remove('ship')
boxes[11].remove('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")