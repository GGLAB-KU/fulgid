# Initial state of boxes
boxes = {
    0: ['octopus', 'coat'],
    1: ['chair', 'horse'],
    2: ['river', 'mountain', 'rock'],
    3: ['blanket'],
    4: ['dice', 'umbrella', 'cloud', 'toothbrush', 'console'],
    5: [],
    6: ['toothpaste', 'controller', 'leaf', 'book', 'button'],
    7: ['spoon', 'bell'],
    8: ['mixer'],
    9: ['piano', 'ship', 'dog'],
    10: ['note', 'island', 'hat'],
    11: ['headphone'],
    12: ['shorts', 'shirt'],
    13: ['freezer'],
    14: ['cat']
}

# Put the hat and the phone into Box 10.
boxes[10].append('hat')
boxes[10].append('phone')

# Put the meteor and the usb into Box 9.
boxes[9].append('meteor')
boxes[9].append('usb')

# Replace the bell and the spoon with the beach and the submarine in Box 7.
boxes[7].remove('bell')
boxes[7].remove('spoon')
boxes[7].append('beach')
boxes[7].append('submarine')

# Swap the blanket in Box 3 with the horse in Box 1.
boxes[1].remove('horse')
boxes[3].remove('blanket')
boxes[1].append('blanket')
boxes[3].append('horse')

# Swap the hat in Box 10 with the blanket in Box 1.
boxes[1].remove('blanket')
boxes[10].remove('hat')
boxes[1].append('hat')
boxes[10].append('blanket')

# Remove the shorts and the shirt from Box 12.
boxes[12].remove('shorts')
boxes[12].remove('shirt')

# Move the freezer from Box 13 to Box 12.
boxes[13].remove('freezer')
boxes[12].append('freezer')

# Replace the controller and the leaf with the pan and the pot in Box 6.
boxes[6].remove('controller')
boxes[6].remove('leaf')
boxes[6].append('pan')
boxes[6].append('pot')

# Replace the headphone with the blender in Box 11.
boxes[11].remove('headphone')
boxes[11].append('blender')

# Move the cat from Box 14 to Box 11.
boxes[14].remove('cat')
boxes[11].append('cat')

# Swap the hat in Box 1 with the shoe in Box 10.
boxes[1].remove('hat')
boxes[10].remove('shoe')
boxes[1].append('shoe')
boxes[10].append('hat')

# Put the grinder into Box 8.
boxes[8].append('grinder')

# Move the freezer from Box 12 to Box 10.
boxes[12].remove('freezer')
boxes[10].append('freezer')

# Move the usb and the ship and the piano from Box 9 to Box 10.
items_to_move = ['usb', 'ship', 'piano']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[10].append(item)

# Remove the submarine and the beach from Box 7.
boxes[7].remove('submarine')
boxes[7].remove('beach')

# Replace the cat with the rock in Box 11.
boxes[11].remove('cat')
boxes[11].append('rock')

# Empty Box 6.
boxes[6] = []

# Move the note from Box 10 to Box 1.
boxes[10].remove('note')
boxes[1].append('note')

# Replace the horse with the bowl in Box 3.
boxes[3].remove('horse')
boxes[3].append('bowl')

# Swap the meteor in Box 9 with the bowl in Box 3.
boxes[9].remove('meteor')
boxes[3].remove('bowl')
boxes[9].append('bowl')
boxes[3].append('meteor')

# Remove the coat and the octopus from Box 0.
boxes[0].remove('coat')
boxes[0].remove('octopus')

# Remove the dice and the cloud and the toothbrush from Box 4.
items_to_remove = ['dice', 'cloud', 'toothbrush']
for item in items_to_remove:
    boxes[4].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")