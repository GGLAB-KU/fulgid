# Initial state of boxes
boxes = {
    0: [],
    1: ['blender', 'zipper'],
    2: ['candle'],
    3: ['comet', 'swimsuit', 'coral', 'train', 'car'],
    4: ['usb'],
    5: ['fridge', 'rocket', 'pen'],
    6: ['horse', 'boat', 'tiger', 'ship'],
    7: ['rain', 'keyboard', 'mountain', 'harmonica', 'crown'],
    8: [],
    9: ['sculpture', 'thunder', 'jungle', 'spoon'],
    10: ['key', 'frame', 'headphone'],
    11: ['flute', 'earring', 'lock'],
    12: ['cup'],
    13: ['microwave', 'shorts', 'lipstick', 'mask'],
    14: []
}

# Remove the frame from Box 10.
boxes[10].remove('frame')

# Swap the zipper in Box 1 with the tiger in Box 6.
boxes[1].remove('zipper')
boxes[6].remove('tiger')
boxes[1].append('tiger')
boxes[6].append('zipper')

# Remove the jungle and the sculpture and the spoon from Box 9.
items_to_remove = ['jungle', 'sculpture', 'spoon']
for item in items_to_remove:
    boxes[9].remove(item)

# Swap the blender in Box 1 with the mountain in Box 7.
boxes[1].remove('blender')
boxes[7].remove('mountain')
boxes[1].append('mountain')
boxes[7].append('blender')

# Put the bracelet into Box 4.
boxes[4].append('bracelet')

# Swap the candle in Box 2 with the thunder in Box 9.
boxes[2].remove('candle')
boxes[9].remove('thunder')
boxes[2].append('thunder')
boxes[9].append('candle')

# Remove the mountain from Box 1.
boxes[1].remove('mountain')

# Move the bracelet from Box 4 to Box 14.
boxes[4].remove('bracelet')
boxes[14].append('bracelet')

# Swap the usb in Box 4 with the lipstick in Box 13.
boxes[4].remove('usb')
boxes[13].remove('lipstick')
boxes[4].append('lipstick')
boxes[13].append('usb')

# Move the rocket and the fridge from Box 5 to Box 6.
items_to_move = ['rocket', 'fridge']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[6].append(item)

# Empty Box 5.
boxes[5] = []

# Remove the bracelet from Box 14.
boxes[14].remove('bracelet')

# Swap the thunder in Box 2 with the tiger in Box 1.
boxes[2].remove('thunder')
boxes[1].remove('tiger')
boxes[2].append('tiger')
boxes[1].append('thunder')

# Put the mirror into Box 2.
boxes[2].append('mirror')

# Swap the lipstick in Box 4 with the candle in Box 9.
boxes[4].remove('lipstick')
boxes[9].remove('candle')
boxes[4].append('candle')
boxes[9].append('lipstick')

# Put the scarf into Box 4.
boxes[4].append('scarf')

# Replace the thunder with the tie in Box 1.
boxes[1].remove('thunder')
boxes[1].append('tie')

# Swap the comet in Box 3 with the key in Box 10.
boxes[3].remove('comet')
boxes[10].remove('key')
boxes[3].append('key')
boxes[10].append('comet')

# Replace the train and the coral and the swimsuit with the dice and the violin and the shelf in Box 3.
boxes[3].remove('train')
boxes[3].remove('coral')
boxes[3].remove('swimsuit')
boxes[3].append('dice')
boxes[3].append('violin')
boxes[3].append('shelf')

# Move the lock from Box 11 to Box 12.
boxes[11].remove('lock')
boxes[12].append('lock')

# Replace the scarf and the candle with the shampoo and the truck in Box 4.
boxes[4].remove('scarf')
boxes[4].remove('candle')
boxes[4].append('shampoo')
boxes[4].append('truck')

# Replace the usb and the mask with the snow and the note in Box 13.
boxes[13].remove('usb')
boxes[13].remove('mask')
boxes[13].append('snow')
boxes[13].append('note')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")