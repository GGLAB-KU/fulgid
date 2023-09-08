# Initial state of boxes
boxes = {
    0: ['lightning', 'butterfly', 'pot', 'camera'],
    1: ['comb', 'bus', 'grinder', 'shorts'],
    2: ['shelf', 'clock', 'mountain', 'lipstick', 'fork'],
    3: ['pen', 'cup', 'submarine'],
    4: ['dice', 'frame', 'tie', 'river'],
    5: ['flower', 'horn', 'makeup', 'magnet', 'apple'],
    6: ['shirt', 'shampoo'],
    7: ['puzzle', 'polish', 'freezer', 'violin', 'chair'],
    8: ['key', 'microwave', 'fish', 'gloves'],
    9: ['jacket']
}

# Replace the pot and the camera and the lightning with the toaster and the pillow and the comb in Box 0.
boxes[0].remove('pot')
boxes[0].remove('camera')
boxes[0].remove('lightning')
boxes[0].append('toaster')
boxes[0].append('pillow')
boxes[0].append('comb')

# Remove the mountain from Box 2.
boxes[2].remove('mountain')

# Move the violin and the polish and the chair from Box 7 to Box 9.
items_to_move = ['violin', 'polish', 'chair']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[9].append(item)

# Replace the tie with the speaker in Box 4.
boxes[4].remove('tie')
boxes[4].append('speaker')

# Replace the toaster with the glasses in Box 0.
boxes[0].remove('toaster')
boxes[0].append('glasses')

# Replace the fork and the lipstick and the shelf with the plane and the book and the guitar in Box 2.
boxes[2].remove('fork')
boxes[2].remove('lipstick')
boxes[2].remove('shelf')
boxes[2].append('plane')
boxes[2].append('book')
boxes[2].append('guitar')

# Remove the glasses and the butterfly from Box 0.
boxes[0].remove('glasses')
boxes[0].remove('butterfly')

# Put the leaf into Box 4.
boxes[4].append('leaf')

# Move the polish and the violin and the jacket from Box 9 to Box 1.
items_to_move = ['polish', 'violin', 'jacket']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Move the makeup from Box 5 to Box 8.
boxes[5].remove('makeup')
boxes[8].append('makeup')

# Swap the pillow in Box 0 with the guitar in Box 2.
boxes[0].remove('pillow')
boxes[2].remove('guitar')
boxes[0].append('guitar')
boxes[2].append('pillow')

# Move the chair from Box 9 to Box 2.
boxes[9].remove('chair')
boxes[2].append('chair')

# Move the leaf and the river and the speaker from Box 4 to Box 0.
items_to_move = ['leaf', 'river', 'speaker']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Remove the comb and the bus from Box 1.
boxes[1].remove('comb')
boxes[1].remove('bus')

# Put the towel and the coat into Box 2.
boxes[2].append('towel')
boxes[2].append('coat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")