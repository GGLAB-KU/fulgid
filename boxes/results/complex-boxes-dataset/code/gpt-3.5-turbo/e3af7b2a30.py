# Initial state of boxes
boxes = {
    0: ['planet'],
    1: ['horse', 'usb', 'phone', 'butterfly'],
    2: ['mixer', 'shirt', 'lamp', 'bell'],
    3: ['bear'],
    4: ['thread', 'helmet'],
    5: ['flute', 'mask', 'ocean', 'pen', 'tape'],
    6: ['jacket', 'desert'],
    7: ['fridge', 'jungle', 'keyboard', 'earring'],
    8: ['camera', 'train', 'razor'],
    9: ['submarine', 'paint', 'microwave', 'microscope', 'wire'],
    10: ['cloud', 'frame', 'rocket', 'elephant', 'beach'],
    11: ['zipper', 'soap', 'controller'],
    12: ['mirror', 'brush', 'coat', 'bracelet'],
    13: [],
    14: ['button', 'shelf', 'toaster', 'battery']
}

# Move the thread from Box 4 to Box 8.
boxes[4].remove('thread')
boxes[8].append('thread')

# Put the chair and the flower and the motorcycle into Box 5.
items_to_move = ['chair', 'flower', 'motorcycle']
for item in items_to_move:
    boxes[5].append(item)

# Swap the lamp in Box 2 with the wire in Box 9.
boxes[2].remove('lamp')
boxes[9].remove('wire')
boxes[2].append('wire')
boxes[9].append('lamp')

# Move the soap from Box 11 to Box 1.
boxes[11].remove('soap')
boxes[1].append('soap')

# Replace the button and the toaster and the battery with the book and the paint and the shirt in Box 14.
boxes[14].remove('button')
boxes[14].remove('toaster')
boxes[14].remove('battery')
boxes[14].append('book')
boxes[14].append('paint')
boxes[14].append('shirt')

# Swap the zipper in Box 11 with the shirt in Box 2.
boxes[11].remove('zipper')
boxes[2].remove('shirt')
boxes[11].append('shirt')
boxes[2].append('zipper')

# Put the motorcycle and the toothpaste and the tie into Box 7.
items_to_move = ['motorcycle', 'toothpaste', 'tie']
for item in items_to_move:
    boxes[7].append(item)

# Put the helmet into Box 10.
boxes[4].remove('helmet')
boxes[10].append('helmet')

# Move the planet from Box 0 to Box 12.
boxes[0].remove('planet')
boxes[12].append('planet')

# Swap the thread in Box 8 with the helmet in Box 4.
boxes[8].remove('thread')
boxes[4].remove('helmet')
boxes[8].append('helmet')
boxes[4].append('thread')

# Put the pillow and the usb into Box 11.
items_to_move = ['pillow', 'usb']
for item in items_to_move:
    boxes[11].append(item)

# Swap the bear in Box 3 with the flower in Box 5.
boxes[3].remove('bear')
boxes[5].remove('flower')
boxes[3].append('flower')
boxes[5].append('bear')

# Swap the shirt in Box 14 with the zipper in Box 2.
boxes[14].remove('shirt')
boxes[2].remove('zipper')
boxes[14].append('zipper')
boxes[2].append('shirt')

# Put the harmonica into Box 11.
boxes[11].append('harmonica')

# Replace the usb with the magnet in Box 11.
boxes[11].remove('usb')
boxes[11].append('magnet')

# Remove the motorcycle from Box 5.
boxes[5].remove('motorcycle')

# Replace the zipper with the soap in Box 14.
boxes[14].remove('zipper')
boxes[14].append('soap')

# Move the rocket from Box 10 to Box 1.
boxes[10].remove('rocket')
boxes[1].append('rocket')

# Put the sun into Box 7.
boxes[7].append('sun')

# Put the fish and the comb and the tie into Box 10.
items_to_move = ['fish', 'comb', 'tie']
for item in items_to_move:
    boxes[10].append(item)

# Put the bird into Box 10.
boxes[10].append('bird')

# Remove the motorcycle and the toothpaste from Box 7.
boxes[7].remove('motorcycle')
boxes[7].remove('toothpaste')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")