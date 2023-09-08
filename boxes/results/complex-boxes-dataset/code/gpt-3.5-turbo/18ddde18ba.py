# Initial state of boxes
boxes = {
    0: ['drum', 'grinder', 'blanket', 'pot', 'star'],
    1: ['bear'],
    2: ['zipper', 'crown'],
    3: ['earring'],
    4: [],
    5: ['shoes', 'coin', 'dress', 'apple', 'glove'],
    6: ['mountain', 'shoe', 'clock', 'card', 'sandals'],
    7: ['doll', 'shampoo', 'usb', 'oven', 'piano'],
    8: ['bracelet', 'tiger', 'spoon', 'skirt', 'headphone'],
    9: ['magnet', 'guitar', 'bus', 'comet'],
    10: ['microscope', 'lamp'],
    11: ['toaster', 'butterfly', 'bell', 'comb'],
    12: ['note'],
    13: ['shark', 'motorcycle']
}

# Remove the headphone from Box 8.
boxes[8].remove('headphone')

# Remove the card and the sandals from Box 6.
boxes[6].remove('card')
boxes[6].remove('sandals')

# Remove the microscope from Box 10.
boxes[10].remove('microscope')

# Swap the lamp in Box 10 with the piano in Box 7.
boxes[10].remove('lamp')
boxes[7].remove('piano')
boxes[10].append('piano')
boxes[7].append('lamp')

# Swap the earring in Box 3 with the zipper in Box 2.
boxes[3].remove('earring')
boxes[2].remove('zipper')
boxes[3].append('zipper')
boxes[2].append('earring')

# Put the oven and the belt into Box 4.
boxes[4].append('oven')
boxes[4].append('belt')

# Move the zipper from Box 3 to Box 5.
boxes[3].remove('zipper')
boxes[5].append('zipper')

# Move the dress and the zipper and the shoes from Box 5 to Box 1.
items_to_move = ['dress', 'zipper', 'shoes']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[1].append(item)

# Put the microscope and the shelf into Box 1.
boxes[1].append('microscope')
boxes[1].append('shelf')

# Swap the glove in Box 5 with the grinder in Box 0.
boxes[5].remove('glove')
boxes[0].remove('grinder')
boxes[5].append('grinder')
boxes[0].append('glove')

# Empty Box 8.
boxes[8] = []

# Remove the mountain from Box 6.
boxes[6].remove('mountain')

# Replace the note with the shoe in Box 12.
boxes[12].remove('note')
boxes[12].append('shoe')

# Swap the piano in Box 10 with the belt in Box 4.
boxes[10].remove('piano')
boxes[4].remove('belt')
boxes[10].append('belt')
boxes[4].append('piano')

# Remove the shoe from Box 12.
boxes[12].remove('shoe')

# Swap the belt in Box 10 with the earring in Box 2.
boxes[10].remove('belt')
boxes[2].remove('earring')
boxes[10].append('earring')
boxes[2].append('belt')

# Swap the blanket in Box 0 with the usb in Box 7.
boxes[0].remove('blanket')
boxes[7].remove('usb')
boxes[0].append('usb')
boxes[7].append('blanket')

# Replace the shelf with the shoes in Box 1.
boxes[1].remove('shelf')
boxes[1].append('shoes')

# Replace the butterfly and the toaster and the bell with the blender and the scissors and the tape in Box 11.
boxes[11].remove('butterfly')
boxes[11].remove('toaster')
boxes[11].remove('bell')
boxes[11].append('blender')
boxes[11].append('scissors')
boxes[11].append('tape')

# Remove the usb from Box 0.
boxes[0].remove('usb')

# Put the ocean and the razor and the pot into Box 6.
boxes[6].append('ocean')
boxes[6].append('razor')
boxes[6].append('pot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")