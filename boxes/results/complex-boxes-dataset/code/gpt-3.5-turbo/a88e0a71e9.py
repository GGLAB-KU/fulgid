# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['zipper', 'coat', 'key'],
    3: ['mixer', 'dog', 'meteor', 'thunder'],
    4: ['charger', 'crown'],
    5: [],
    6: [],
    7: ['toaster', 'dice'],
    8: ['jacket', 'shirt', 'rock', 'butterfly'],
    9: ['keyboard', 'drum', 'button'],
    10: ['towel', 'makeup'],
    11: ['chair', 'spoon', 'wallet', 'flute', 'controller'],
    12: []
}

# Remove the toaster and the dice from Box 7.
boxes[7].remove('toaster')
boxes[7].remove('dice')

# Put the lipstick and the umbrella and the planet into Box 1.
boxes[1].append('lipstick')
boxes[1].append('umbrella')
boxes[1].append('planet')

# Swap the towel in Box 10 with the key in Box 2.
boxes[10].remove('towel')
boxes[2].remove('key')
boxes[10].append('key')
boxes[2].append('towel')

# Move the crown from Box 4 to Box 7.
boxes[4].remove('crown')
boxes[7].append('crown')

# Remove the makeup and the key from Box 10.
boxes[10].remove('makeup')
boxes[10].remove('key')

# Remove the rock and the jacket and the shirt from Box 8.
items_to_remove = ['rock', 'jacket', 'shirt']
for item in items_to_remove:
    boxes[8].remove(item)

# Replace the mixer and the meteor with the island and the forest in Box 3.
boxes[3].remove('mixer')
boxes[3].remove('meteor')
boxes[3].append('island')
boxes[3].append('forest')

# Remove the island and the forest and the dog from Box 3.
items_to_remove = ['island', 'forest', 'dog']
for item in items_to_remove:
    boxes[3].remove(item)

# Move the charger from Box 4 to Box 5.
boxes[4].remove('charger')
boxes[5].append('charger')

# Put the key and the chair into Box 10.
boxes[10].append('key')
boxes[10].append('chair')

# Swap the wallet in Box 11 with the umbrella in Box 1.
boxes[11].remove('wallet')
boxes[1].remove('umbrella')
boxes[11].append('umbrella')
boxes[1].append('wallet')

# Remove the key from Box 10.
boxes[10].remove('key')

# Remove the crown from Box 7.
boxes[7].remove('crown')

# Move the chair from Box 10 to Box 6.
boxes[10].remove('chair')
boxes[6].append('chair')

# Put the truck into Box 3.
boxes[3].append('truck')

# Swap the lipstick in Box 1 with the charger in Box 5.
boxes[1].remove('lipstick')
boxes[5].remove('charger')
boxes[1].append('charger')
boxes[5].append('lipstick')

# Replace the lipstick with the microwave in Box 5.
boxes[5].remove('lipstick')
boxes[5].append('microwave')

# Swap the keyboard in Box 9 with the butterfly in Box 8.
boxes[9].remove('keyboard')
boxes[8].remove('butterfly')
boxes[9].append('butterfly')
boxes[8].append('keyboard')

# Move the spoon and the controller and the umbrella from Box 11 to Box 0.
items_to_move = ['spoon', 'controller', 'umbrella']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[0].append(item)

# Remove the chair from Box 6.
boxes[6].remove('chair')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")