# Initial state of boxes
boxes = {
    0: ['dolphin'],
    1: ['jungle'],
    2: ['makeup', 'tape', 'submarine', 'blender'],
    3: ['bear'],
    4: ['chair', 'leaf'],
    5: ['speaker'],
    6: ['bowl', 'elephant', 'towel', 'coin'],
    7: ['book', 'spoon', 'shoe', 'magnet', 'forest'],
    8: ['dice', 'necklace', 'puzzle', 'watch'],
    9: ['moon', 'button', 'ocean'],
    10: ['key', 'storm'],
    11: ['zipper']
}

# Remove the jungle from Box 1.
boxes[1].remove('jungle')

# Put the glasses into Box 7.
boxes[7].append('glasses')

# Put the mirror and the watch and the lamp into Box 3.
boxes[3].extend(['mirror', 'watch', 'lamp'])

# Move the dolphin from Box 0 to Box 4.
boxes[0].remove('dolphin')
boxes[4].append('dolphin')

# Put the polish and the star and the ship into Box 6.
boxes[6].extend(['polish', 'star', 'ship'])

# Swap the magnet in Box 7 with the necklace in Box 8.
boxes[7].remove('magnet')
boxes[8].remove('necklace')
boxes[7].append('necklace')
boxes[8].append('magnet')

# Move the magnet and the watch and the puzzle from Box 8 to Box 3.
items_to_move = ['magnet', 'watch', 'puzzle']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Swap the moon in Box 9 with the speaker in Box 5.
boxes[9].remove('moon')
boxes[5].remove('speaker')
boxes[9].append('speaker')
boxes[5].append('moon')

# Swap the moon in Box 5 with the book in Box 7.
boxes[5].remove('moon')
boxes[7].remove('book')
boxes[5].append('book')
boxes[7].append('moon')

# Swap the leaf in Box 4 with the makeup in Box 2.
boxes[4].remove('leaf')
boxes[2].remove('makeup')
boxes[4].append('makeup')
boxes[2].append('leaf')

# Replace the chair and the makeup with the shelf and the comet in Box 4.
boxes[4].remove('chair')
boxes[4].remove('makeup')
boxes[4].append('shelf')
boxes[4].append('comet')

# Move the tape from Box 2 to Box 9.
boxes[2].remove('tape')
boxes[9].append('tape')

# Move the dice from Box 8 to Box 2.
boxes[8].remove('dice')
boxes[2].append('dice')

# Swap the tape in Box 9 with the book in Box 5.
boxes[9].remove('tape')
boxes[5].remove('book')
boxes[9].append('book')
boxes[5].append('tape')

# Move the key and the storm from Box 10 to Box 7.
boxes[10].remove('key')
boxes[10].remove('storm')
boxes[7].extend(['key', 'storm'])

# Move the button and the book from Box 9 to Box 4.
boxes[9].remove('button')
boxes[9].remove('book')
boxes[4].extend(['button', 'book'])

# Replace the shelf with the butterfly in Box 4.
boxes[4].remove('shelf')
boxes[4].append('butterfly')

# Remove the moon and the glasses and the key from Box 7.
boxes[7].remove('moon')
boxes[7].remove('glasses')
boxes[7].remove('key')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")