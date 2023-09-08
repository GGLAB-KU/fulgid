# Initial state of boxes
boxes = {
    0: ['card', 'shoes'],
    1: ['spoon', 'clock', 'watch'],
    2: ['motorcycle', 'blanket'],
    3: ['umbrella', 'shark', 'thunder', 'lamp', 'dress'],
    4: [],
    5: ['truck', 'bicycle', 'shorts'],
    6: ['shelf', 'pen', 'perfume'],
    7: ['swimsuit', 'octopus'],
    8: ['whistle', 'cow', 'sandals', 'console', 'note'],
    9: ['phone', 'button', 'puzzle']
}

# Put the shelf and the glasses into Box 1.
boxes[1].append('shelf')
boxes[1].append('glasses')

# Replace the shelf and the perfume and the pen with the horse and the rocket and the tiger in Box 6.
boxes[6].remove('shelf')
boxes[6].remove('perfume')
boxes[6].remove('pen')
boxes[6].append('horse')
boxes[6].append('rocket')
boxes[6].append('tiger')

# Move the watch and the glasses and the shelf from Box 1 to Box 7.
items_to_move = ['watch', 'glasses', 'shelf']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[7].append(item)

# Put the violin and the pillow into Box 0.
boxes[0].append('violin')
boxes[0].append('pillow')

# Move the tiger and the rocket and the horse from Box 6 to Box 0.
items_to_move = ['tiger', 'rocket', 'horse']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Put the swimsuit into Box 1.
boxes[1].append('swimsuit')

# Swap the shorts in Box 5 with the cow in Box 8.
boxes[5].remove('shorts')
boxes[8].remove('cow')
boxes[5].append('cow')
boxes[8].append('shorts')

# Put the keyboard and the butterfly and the thread into Box 7.
boxes[7].append('keyboard')
boxes[7].append('butterfly')
boxes[7].append('thread')

# Remove the swimsuit and the spoon and the clock from Box 1.
items_to_remove = ['swimsuit', 'spoon', 'clock']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the glasses from Box 7 to Box 3.
boxes[7].remove('glasses')
boxes[3].append('glasses')

# Remove the blanket from Box 2.
boxes[2].remove('blanket')

# Remove the truck and the bicycle from Box 5.
boxes[5].remove('truck')
boxes[5].remove('bicycle')

# Remove the dress and the thunder and the shark from Box 3.
items_to_remove = ['dress', 'thunder', 'shark']
for item in items_to_remove:
    boxes[3].remove(item)

# Put the lion and the towel and the microwave into Box 3.
boxes[3].append('lion')
boxes[3].append('towel')
boxes[3].append('microwave')

# Move the motorcycle from Box 2 to Box 5.
boxes[2].remove('motorcycle')
boxes[5].append('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")