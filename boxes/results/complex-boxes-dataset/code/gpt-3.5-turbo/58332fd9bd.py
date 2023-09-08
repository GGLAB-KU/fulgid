# Initial state of boxes
boxes = {
    0: ['tape', 'branch', 'needle'],
    1: ['plate', 'pillow'],
    2: ['boot', 'dog', 'book', 'grinder'],
    3: [],
    4: ['moon', 'truck'],
    5: ['leaf'],
    6: ['snow', 'pants', 'soap', 'usb', 'wire']
}

# Swap the dog in Box 2 with the leaf in Box 5.
boxes[2].remove('dog')
boxes[5].remove('leaf')
boxes[2].append('leaf')
boxes[5].append('dog')

# Move the moon from Box 4 to Box 1.
boxes[4].remove('moon')
boxes[1].append('moon')

# Put the fridge and the freezer and the tiger into Box 1.
items_to_add = ['fridge', 'freezer', 'tiger']
for item in items_to_add:
    boxes[1].append(item)

# Move the book and the grinder from Box 2 to Box 3.
items_to_move = ['book', 'grinder']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Move the dog from Box 5 to Box 0.
boxes[5].remove('dog')
boxes[0].append('dog')

# Replace the leaf and the boot with the key and the soap in Box 2.
boxes[2].remove('leaf')
boxes[2].remove('boot')
boxes[2].append('key')
boxes[2].append('soap')

# Put the chair and the shirt into Box 4.
items_to_add = ['chair', 'shirt']
for item in items_to_add:
    boxes[4].append(item)

# Put the toothpaste and the frame and the truck into Box 6.
items_to_add = ['toothpaste', 'frame', 'truck']
for item in items_to_add:
    boxes[6].append(item)

# Empty Box 2.
boxes[2] = []

# Remove the toothpaste and the wire and the pants from Box 6.
items_to_remove = ['toothpaste', 'wire', 'pants']
for item in items_to_remove:
    boxes[6].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")