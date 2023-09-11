# Initial state of boxes
boxes = {
    0: ['bird', 'coat', 'shampoo', 'earring', 'basket'],
    1: ['rocket', 'fish', 'magnet'],
    2: ['comb'],
    3: ['submarine', 'octopus', 'flute', 'car'],
    4: ['candle', 'wire', 'rain', 'headphone'],
    5: ['coral', 'toaster', 'grass', 'sock'],
    6: ['towel', 'leaf'],
    7: ['book', 'mask', 'helmet', 'dolphin'],
    8: ['perfume']
}

# Remove the grass and the sock and the coral from Box 5.
items_to_remove = ['grass', 'sock', 'coral']
for item in items_to_remove:
    boxes[5].remove(item)

# Empty Box 2.
boxes[2] = []

# Replace the car with the spoon in Box 3.
boxes[3].remove('car')
boxes[3].append('spoon')

# Move the perfume from Box 8 to Box 3.
boxes[8].remove('perfume')
boxes[3].append('perfume')

# Remove the submarine from Box 3.
boxes[3].remove('submarine')

# Put the towel and the moon and the needle into Box 3.
items_to_add = ['towel', 'moon', 'needle']
for item in items_to_add:
    boxes[3].append(item)

# Move the toaster from Box 5 to Box 3.
boxes[5].remove('toaster')
boxes[3].append('toaster')

# Move the towel and the leaf from Box 6 to Box 0.
items_to_move = ['towel', 'leaf']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Replace the fish and the rocket with the toaster and the truck in Box 1.
boxes[1].remove('fish')
boxes[1].remove('rocket')
boxes[1].append('toaster')
boxes[1].append('truck')

# Put the frame into Box 8.
boxes[8].append('frame')

# Swap the towel in Box 0 with the octopus in Box 3.
boxes[0].remove('towel')
boxes[3].remove('octopus')
boxes[0].append('octopus')
boxes[3].append('towel')

# Swap the toaster in Box 1 with the headphone in Box 4.
boxes[1].remove('toaster')
boxes[4].remove('headphone')
boxes[1].append('headphone')
boxes[4].append('toaster')

# Replace the magnet and the headphone with the comb and the pot in Box 1.
boxes[1].remove('magnet')
boxes[1].remove('headphone')
boxes[1].append('comb')
boxes[1].append('pot')

# Move the leaf and the earring and the octopus from Box 0 to Box 7.
items_to_move = ['leaf', 'earring', 'octopus']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[7].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")