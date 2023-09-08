# Initial state of boxes
boxes = {
    0: ['elephant', 'grass', 'dress'],
    1: ['bear', 'watch'],
    2: ['hat', 'desert', 'scarf', 'cup'],
    3: [],
    4: ['skirt', 'shark', 'tape', 'bag', 'console'],
    5: ['seaweed', 'forest'],
    6: ['belt', 'plate', 'lock', 'vase', 'sock']
}

# Move the bear and the watch from Box 1 to Box 6.
boxes[1].remove('bear')
boxes[1].remove('watch')
boxes[6].append('bear')
boxes[6].append('watch')

# Replace the seaweed and the forest with the makeup and the snow in Box 5.
boxes[5].remove('seaweed')
boxes[5].remove('forest')
boxes[5].append('makeup')
boxes[5].append('snow')

# Remove the watch and the bear from Box 6.
boxes[6].remove('watch')
boxes[6].remove('bear')

# Move the vase and the lock from Box 6 to Box 1.
boxes[6].remove('vase')
boxes[6].remove('lock')
boxes[1].append('vase')
boxes[1].append('lock')

# Swap the sock in Box 6 with the bag in Box 4.
boxes[6].remove('sock')
boxes[4].remove('bag')
boxes[6].append('bag')
boxes[4].append('sock')

# Move the lock and the vase from Box 1 to Box 2.
boxes[1].remove('lock')
boxes[1].remove('vase')
boxes[2].append('lock')
boxes[2].append('vase')

# Move the dress and the grass and the elephant from Box 0 to Box 2.
items_to_move = ['dress', 'grass', 'elephant']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Swap the console in Box 4 with the dress in Box 2.
boxes[4].remove('console')
boxes[2].remove('dress')
boxes[4].append('dress')
boxes[2].append('console')

# Remove the bag from Box 6.
boxes[6].remove('bag')

# Put the shampoo and the magnet and the elephant into Box 3.
items_to_move = ['shampoo', 'magnet', 'elephant']
for item in items_to_move:
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")