# Initial state of boxes
boxes = {
    0: ['basket', 'submarine', 'thunder', 'puzzle', 'rain'],
    1: ['tie', 'shelf'],
    2: ['umbrella', 'car', 'thread', 'drum'],
    3: ['grinder'],
    4: ['dolphin', 'perfume'],
    5: ['soap', 'chair', 'toothbrush', 'motorcycle'],
    6: ['helmet', 'tree', 'grass', 'shirt'],
    7: [],
    8: ['frame', 'bird', 'fridge'],
    9: ['crown'],
    10: ['sandals', 'note', 'mask', 'lamp'],
    11: ['necklace', 'moon'],
    12: ['shoe', 'vase', 'jungle'],
    13: ['glove', 'pan', 'flower', 'ocean'],
    14: ['island', 'pen', 'sculpture', 'bus', 'jacket']
}

# Put the cow into Box 12.
boxes[12].append('cow')

# Replace the frame and the bird and the fridge with the rocket and the shark and the branch in Box 8.
boxes[8].remove('frame')
boxes[8].remove('bird')
boxes[8].remove('fridge')
boxes[8].append('rocket')
boxes[8].append('shark')
boxes[8].append('branch')

# Put the tie into Box 8.
boxes[8].append('tie')

# Replace the perfume with the tie in Box 4.
boxes[4].remove('perfume')
boxes[4].append('tie')

# Swap the drum in Box 2 with the crown in Box 9.
boxes[2].remove('drum')
boxes[9].remove('crown')
boxes[2].append('crown')
boxes[9].append('drum')

# Move the sculpture from Box 14 to Box 8.
boxes[14].remove('sculpture')
boxes[8].append('sculpture')

# Replace the necklace with the oven in Box 11.
boxes[11].remove('necklace')
boxes[11].append('oven')

# Put the sun into Box 1.
boxes[1].append('sun')

# Put the mask and the snow and the lock into Box 10.
boxes[10].append('mask')
boxes[10].append('snow')
boxes[10].append('lock')

# Put the ocean and the dress and the bowl into Box 14.
boxes[14].append('ocean')
boxes[14].append('dress')
boxes[14].append('bowl')

# Replace the helmet and the tree with the freezer and the bracelet in Box 6.
boxes[6].remove('helmet')
boxes[6].remove('tree')
boxes[6].append('freezer')
boxes[6].append('bracelet')

# Swap the soap in Box 5 with the shelf in Box 1.
boxes[5].remove('soap')
boxes[1].remove('shelf')
boxes[5].append('shelf')
boxes[1].append('soap')

# Swap the ocean in Box 14 with the grinder in Box 3.
boxes[14].remove('ocean')
boxes[3].remove('grinder')
boxes[14].append('grinder')
boxes[3].append('ocean')

# Swap the vase in Box 12 with the ocean in Box 3.
boxes[12].remove('vase')
boxes[3].remove('ocean')
boxes[12].append('ocean')
boxes[3].append('vase')

# Replace the oven with the speaker in Box 11.
boxes[11].remove('oven')
boxes[11].append('speaker')

# Replace the drum with the star in Box 9.
boxes[9].remove('drum')
boxes[9].append('star')

# Replace the chair and the toothbrush and the shelf with the makeup and the plate and the bicycle in Box 5.
boxes[5].remove('chair')
boxes[5].remove('toothbrush')
boxes[1].remove('shelf')
boxes[5].append('makeup')
boxes[5].append('plate')
boxes[1].append('bicycle')

# Swap the moon in Box 11 with the shark in Box 8.
boxes[11].remove('moon')
boxes[8].remove('shark')
boxes[11].append('shark')
boxes[8].append('moon')

# Replace the grass and the bracelet and the freezer with the plane and the table and the boat in Box 6.
boxes[6].remove('grass')
boxes[6].remove('bracelet')
boxes[6].remove('freezer')
boxes[6].append('plane')
boxes[6].append('table')
boxes[6].append('boat')

# Replace the motorcycle with the ship in Box 5.
boxes[5].remove('motorcycle')
boxes[5].append('ship')

# Swap the car in Box 2 with the grinder in Box 14.
boxes[2].remove('car')
boxes[14].remove('grinder')
boxes[2].append('grinder')
boxes[14].append('car')

# Swap the sun in Box 1 with the plate in Box 5.
boxes[1].remove('sun')
boxes[5].remove('plate')
boxes[1].append('plate')
boxes[5].append('sun')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")