# Initial state of boxes
boxes = {
    0: ['butterfly'],
    1: ['violin', 'star'],
    2: ['grinder', 'shoes', 'blender'],
    3: ['lock'],
    4: ['oven', 'sock', 'swimsuit'],
    5: ['bicycle', 'crown', 'pillow', 'desert', 'mountain'],
    6: ['apple', 'shorts', 'sculpture', 'boot'],
    7: ['sandals', 'fridge'],
    8: ['game', 'coin', 'elephant'],
    9: ['candle', 'boat', 'tape'],
    10: ['belt'],
    11: ['rock', 'toaster']
}

# Replace the star with the makeup in Box 1.
boxes[1].remove('star')
boxes[1].append('makeup')

# Remove the lock from Box 3.
boxes[3].remove('lock')

# Remove the rock and the toaster from Box 11.
boxes[11].remove('rock')
boxes[11].remove('toaster')

# Remove the violin and the makeup from Box 1.
boxes[1].remove('violin')
boxes[1].remove('makeup')

# Move the apple from Box 6 to Box 7.
boxes[6].remove('apple')
boxes[7].append('apple')

# Put the lion and the comet and the seaweed into Box 4.
items_to_add = ['lion', 'comet', 'seaweed']
for item in items_to_add:
    boxes[4].append(item)

# Remove the sandals from Box 7.
boxes[7].remove('sandals')

# Move the butterfly from Box 0 to Box 3.
boxes[0].remove('butterfly')
boxes[3].append('butterfly')

# Swap the mountain in Box 5 with the shoes in Box 2.
boxes[5].remove('mountain')
boxes[2].remove('shoes')
boxes[5].append('shoes')
boxes[2].append('mountain')

# Move the grinder and the blender from Box 2 to Box 5.
items_to_move = ['grinder', 'blender']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Replace the desert and the pillow with the boot and the snow in Box 5.
boxes[5].remove('desert')
boxes[5].remove('pillow')
boxes[5].append('boot')
boxes[5].append('snow')

# Replace the boot and the grinder with the table and the ring in Box 5.
boxes[5].remove('boot')
boxes[5].remove('grinder')
boxes[5].append('table')
boxes[5].append('ring')

# Replace the butterfly with the plane in Box 3.
boxes[3].remove('butterfly')
boxes[3].append('plane')

# Swap the coin in Box 8 with the boot in Box 6.
boxes[8].remove('coin')
boxes[6].remove('boot')
boxes[8].append('boot')
boxes[6].append('coin')

# Put the brush into Box 7.
boxes[7].append('brush')

# Swap the fridge in Box 7 with the coin in Box 6.
boxes[7].remove('fridge')
boxes[6].remove('coin')
boxes[7].append('coin')
boxes[6].append('fridge')

# Move the mountain from Box 2 to Box 8.
boxes[2].remove('mountain')
boxes[8].append('mountain')

# Put the piano into Box 10.
boxes[10].append('piano')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")