# Initial state of boxes
boxes = {
    0: ['truck', 'bicycle', 'drum', 'microscope'],
    1: ['mixer', 'plane'],
    2: ['shelf', 'scarf', 'guitar'],
    3: ['starfish', 'hat'],
    4: ['horse', 'usb', 'storm'],
    5: ['bear', 'soap', 'basket', 'butterfly'],
    6: [],
    7: ['game', 'wire', 'pan', 'bag'],
    8: ['frame', 'mountain'],
    9: ['river', 'submarine', 'makeup', 'perfume'],
    10: ['shoes', 'freezer']
}

# Remove the pan and the wire from Box 7.
boxes[7].remove('pan')
boxes[7].remove('wire')

# Put the fish into Box 10.
boxes[10].append('fish')

# Empty Box 9.
boxes[9] = []

# Put the motorcycle and the umbrella and the dog into Box 2.
boxes[2].append('motorcycle')
boxes[2].append('umbrella')
boxes[2].append('dog')

# Put the mountain into Box 7.
boxes[7].append('mountain')

# Move the motorcycle and the scarf and the dog from Box 2 to Box 7.
items_to_move = ['motorcycle', 'scarf', 'dog']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[7].append(item)

# Put the scarf and the horse and the jungle into Box 10.
items_to_move = ['scarf', 'horse', 'jungle']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[10].append(item)

# Replace the mountain with the tape in Box 8.
boxes[8].remove('mountain')
boxes[8].append('tape')

# Swap the hat in Box 3 with the jungle in Box 10.
boxes[3].remove('hat')
boxes[10].remove('jungle')
boxes[3].append('jungle')
boxes[10].append('hat')

# Remove the bear from Box 5.
boxes[5].remove('bear')

# Swap the horse in Box 4 with the umbrella in Box 2.
boxes[4].remove('horse')
boxes[2].remove('umbrella')
boxes[4].append('umbrella')
boxes[2].append('horse')

# Move the fish from Box 10 to Box 0.
boxes[10].remove('fish')
boxes[0].append('fish')

# Empty Box 1.
boxes[1] = []

# Put the glasses and the whistle and the toy into Box 7.
boxes[7].append('glasses')
boxes[7].append('whistle')
boxes[7].append('toy')

# Remove the shelf and the guitar and the horse from Box 2.
items_to_remove = ['shelf', 'guitar', 'horse']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the crown and the grass into Box 2.
boxes[2].append('crown')
boxes[2].append('grass')

# Put the horn and the makeup into Box 1.
boxes[1].append('horn')
boxes[1].append('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")