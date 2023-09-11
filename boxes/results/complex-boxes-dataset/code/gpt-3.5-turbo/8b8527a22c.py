# Initial state of boxes
boxes = {
    0: ['clock', 'usb', 'puzzle'],
    1: ['ocean'],
    2: ['crown', 'chair', 'shoes', 'storm'],
    3: ['grinder', 'rock', 'wire'],
    4: ['coat', 'phone', 'toy'],
    5: ['book', 'drum', 'magnet', 'comb'],
    6: ['rain', 'harmonica'],
    7: ['branch'],
    8: ['beach'],
    9: [],
    10: ['helmet']
}

# Replace the rock and the wire and the grinder with the plane and the polish and the fish in Box 3.
boxes[3].remove('grinder')
boxes[3].remove('rock')
boxes[3].remove('wire')
boxes[3].append('plane')
boxes[3].append('polish')
boxes[3].append('fish')

# Put the charger and the fork into Box 1.
boxes[1].append('charger')
boxes[1].append('fork')

# Move the helmet from Box 10 to Box 9.
boxes[10].remove('helmet')
boxes[9].append('helmet')

# Remove the fork and the ocean from Box 1.
boxes[1].remove('fork')
boxes[1].remove('ocean')

# Remove the harmonica from Box 6.
boxes[6].remove('harmonica')

# Move the crown and the storm and the chair from Box 2 to Box 6.
items_to_move = ['crown', 'storm', 'chair']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Move the branch from Box 7 to Box 9.
boxes[7].remove('branch')
boxes[9].append('branch')

# Put the umbrella into Box 9.
boxes[9].append('umbrella')

# Remove the toy from Box 4.
boxes[4].remove('toy')

# Put the brush and the flower and the usb into Box 10.
boxes[10].append('brush')
boxes[10].append('flower')
boxes[10].append('usb')

# Swap the charger in Box 1 with the shoes in Box 2.
boxes[1].remove('charger')
boxes[2].remove('shoes')
boxes[1].append('shoes')
boxes[2].append('charger')

# Swap the brush in Box 10 with the phone in Box 4.
boxes[10].remove('brush')
boxes[4].remove('phone')
boxes[10].append('phone')
boxes[4].append('brush')

# Replace the drum and the book and the comb with the leaf and the shelf and the card in Box 5.
boxes[5].remove('drum')
boxes[5].remove('book')
boxes[5].remove('comb')
boxes[5].append('leaf')
boxes[5].append('shelf')
boxes[5].append('card')

# Replace the charger with the blender in Box 2.
boxes[2].remove('charger')
boxes[2].append('blender')

# Remove the crown from Box 6.
boxes[6].remove('crown')

# Put the speaker and the pan into Box 8.
boxes[8].append('speaker')
boxes[8].append('pan')

# Replace the pan and the speaker with the lipstick and the crown in Box 8.
boxes[8].remove('pan')
boxes[8].remove('speaker')
boxes[8].append('lipstick')
boxes[8].append('crown')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")