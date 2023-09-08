# Initial state of boxes
boxes = {
    0: ['necklace', 'rocket', 'hat', 'magnet'],
    1: ['book', 'desert', 'starfish', 'oven', 'coral'],
    2: ['perfume', 'rock', 'button'],
    3: ['puzzle', 'sun', 'shoe', 'skirt'],
    4: ['moon', 'toaster', 'shark', 'shorts']
}

# Move the shorts and the shark and the toaster from Box 4 to Box 2.
items_to_move = ['shorts', 'shark', 'toaster']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Put the makeup and the necklace and the pants into Box 1.
items_to_put = ['makeup', 'necklace', 'pants']
for item in items_to_put:
    boxes[1].append(item)

# Put the chair and the boot and the razor into Box 1.
items_to_put = ['chair', 'boot', 'razor']
for item in items_to_put:
    boxes[1].append(item)

# Swap the makeup in Box 1 with the sun in Box 3.
boxes[1].remove('makeup')
boxes[3].remove('sun')
boxes[1].append('sun')
boxes[3].append('makeup')

# Replace the shoe and the makeup with the oven and the swimsuit in Box 3.
boxes[3].remove('shoe')
boxes[3].remove('makeup')
boxes[3].append('oven')
boxes[3].append('swimsuit')

# Remove the swimsuit and the puzzle from Box 3.
boxes[3].remove('swimsuit')
boxes[3].remove('puzzle')

# Move the moon from Box 4 to Box 3.
boxes[4].remove('moon')
boxes[3].append('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")