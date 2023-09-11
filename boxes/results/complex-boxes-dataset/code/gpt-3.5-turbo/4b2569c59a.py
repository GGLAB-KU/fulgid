# Initial state of boxes
boxes = {
    0: [],
    1: ['shorts', 'dice', 'soap'],
    2: ['doll'],
    3: [],
    4: ['toy'],
    5: ['polish', 'snow', 'coin'],
    6: [],
    7: ['fridge', 'umbrella', 'camera', 'plate', 'shoes'],
    8: ['sock', 'boot'],
    9: ['truck', 'speaker'],
    10: []
}

# Remove the toy from Box 4.
boxes[4].remove('toy')

# Put the glasses and the makeup into Box 3.
boxes[3].append('glasses')
boxes[3].append('makeup')

# Remove the fridge from Box 7.
boxes[7].remove('fridge')

# Swap the doll in Box 2 with the shorts in Box 1.
boxes[2], boxes[1] = boxes[1], boxes[2]

# Move the dice from Box 1 to Box 7.
boxes[1].remove('dice')
boxes[7].append('dice')

# Replace the sock with the console in Box 8.
boxes[8].remove('sock')
boxes[8].append('console')

# Move the polish and the coin from Box 5 to Box 7.
items_to_move = ['polish', 'coin']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Empty Box 1.
boxes[1] = []

# Remove the console from Box 8.
boxes[8].remove('console')

# Swap the shorts in Box 2 with the speaker in Box 9.
boxes[2], boxes[9] = boxes[9], boxes[2]

# Remove the speaker from Box 2.
boxes[2].remove('speaker')

# Swap the boot in Box 8 with the glasses in Box 3.
boxes[8], boxes[3] = boxes[3], boxes[8]

# Put the dress into Box 4.
boxes[4].append('dress')

# Put the bird and the makeup into Box 7.
boxes[7].append('bird')
boxes[7].append('makeup')

# Move the makeup from Box 3 to Box 0.
boxes[3].remove('makeup')
boxes[0].append('makeup')

# Move the snow from Box 5 to Box 10.
boxes[5].remove('snow')
boxes[10].append('snow')

# Move the shorts and the truck from Box 9 to Box 3.
items_to_move = ['shorts', 'truck']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")