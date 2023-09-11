# Initial state of boxes
boxes = {
    0: ['whistle', 'comet', 'blanket', 'bear'],
    1: ['shirt'],
    2: ['needle', 'planet', 'scarf'],
    3: ['motorcycle', 'paint'],
    4: ['watch', 'car', 'bell'],
    5: ['pants', 'piano', 'headphone', 'shampoo', 'snow'],
    6: ['game', 'camera', 'microscope', 'branch'],
    7: ['frame', 'rock', 'pillow', 'thread', 'lamp'],
    8: ['violin', 'console', 'ship'],
    9: [],
    10: [],
    11: ['blender', 'bus', 'table'],
    12: ['scissors', 'rain', 'note', 'mountain']
}

# Replace the scarf and the planet and the needle with the octopus and the bowl and the shoes in Box 2.
boxes[2].remove('scarf')
boxes[2].remove('planet')
boxes[2].remove('needle')
boxes[2].append('octopus')
boxes[2].append('bowl')
boxes[2].append('shoes')

# Put the mirror and the bowl and the grass into Box 3.
boxes[3].append('mirror')
boxes[3].append('bowl')
boxes[3].append('grass')

# Move the ship and the console and the violin from Box 8 to Box 12.
items_to_move = ['ship', 'console', 'violin']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[12].append(item)

# Put the storm and the oven and the comb into Box 0.
boxes[0].append('storm')
boxes[0].append('oven')
boxes[0].append('comb')

# Replace the console and the violin and the note with the shoe and the makeup and the candle in Box 12.
boxes[12].remove('console')
boxes[12].remove('violin')
boxes[12].remove('note')
boxes[12].append('shoe')
boxes[12].append('makeup')
boxes[12].append('candle')

# Empty Box 12.
boxes[12] = []

# Put the fridge into Box 1.
boxes[1].append('fridge')

# Move the rock from Box 7 to Box 4.
boxes[7].remove('rock')
boxes[4].append('rock')

# Swap the octopus in Box 2 with the branch in Box 6.
boxes[2].remove('octopus')
boxes[6].remove('branch')
boxes[2].append('branch')
boxes[6].append('octopus')

# Swap the grass in Box 3 with the bus in Box 11.
boxes[3].remove('grass')
boxes[11].remove('bus')
boxes[3].append('bus')
boxes[11].append('grass')

# Move the snow and the headphone and the shampoo from Box 5 to Box 4.
items_to_move = ['snow', 'headphone', 'shampoo']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Replace the camera with the brush in Box 6.
boxes[6].remove('camera')
boxes[6].append('brush')

# Put the grinder into Box 3.
boxes[3].append('grinder')

# Swap the blender in Box 11 with the fridge in Box 1.
boxes[11].remove('blender')
boxes[1].remove('fridge')
boxes[11].append('fridge')
boxes[1].append('blender')

# Remove the bowl and the shoes and the branch from Box 2.
items_to_remove = ['bowl', 'shoes', 'branch']
for item in items_to_remove:
    boxes[2].remove(item)

# Replace the headphone and the snow and the car with the frame and the toothbrush and the shorts in Box 4.
boxes[4].remove('headphone')
boxes[4].remove('snow')
boxes[4].remove('car')
boxes[4].append('frame')
boxes[4].append('toothbrush')
boxes[4].append('shorts')

# Move the fridge and the table and the grass from Box 11 to Box 1.
items_to_move = ['fridge', 'table', 'grass']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[1].append(item)

# Replace the frame and the rock and the shorts with the watch and the toy and the button in Box 4.
boxes[4].remove('frame')
boxes[4].remove('rock')
boxes[4].remove('shorts')
boxes[4].append('watch')
boxes[4].append('toy')
boxes[4].append('button')

# Replace the grinder and the bus and the mirror with the freezer and the pot and the shoe in Box 3.
boxes[3].remove('grinder')
boxes[3].remove('bus')
boxes[3].remove('mirror')
boxes[3].append('freezer')
boxes[3].append('pot')
boxes[3].append('shoe')

# Replace the microscope and the brush and the octopus with the rocket and the tape and the cup in Box 6.
boxes[6].remove('microscope')
boxes[6].remove('brush')
boxes[6].remove('octopus')
boxes[6].append('rocket')
boxes[6].append('tape')
boxes[6].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")