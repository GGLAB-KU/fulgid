# Initial state of boxes
boxes = {
    0: ['bicycle', 'book', 'star', 'pants', 'motorcycle'],
    1: ['freezer', 'belt', 'bracelet', 'thunder', 'thread'],
    2: ['candle', 'tiger', 'mask', 'bowl'],
    3: ['wallet', 'coat', 'spoon', 'toaster', 'earring'],
    4: ['microwave', 'drum', 'ocean'],
    5: ['umbrella', 'boot', 'sun', 'pot'],
    6: ['moon'],
    7: ['jacket'],
    8: ['rain'],
    9: ['plate', 'microscope'],
    10: ['butterfly', 'octopus']
}

# Swap the pot in Box 5 with the drum in Box 4.
boxes[4].remove('drum')
boxes[5].remove('pot')
boxes[4].append('pot')
boxes[5].append('drum')

# Remove the toaster from Box 3.
boxes[3].remove('toaster')

# Swap the umbrella in Box 5 with the belt in Box 1.
boxes[1].remove('belt')
boxes[5].remove('umbrella')
boxes[1].append('umbrella')
boxes[5].append('belt')

# Move the bicycle and the motorcycle from Box 0 to Box 5.
items_to_move = ['bicycle', 'motorcycle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Put the book into Box 9.
boxes[0].remove('book')
boxes[9].append('book')

# Move the star from Box 0 to Box 2.
boxes[0].remove('star')
boxes[2].append('star')

# Replace the book and the pants with the rocket and the key in Box 0.
boxes[0].remove('book')
boxes[0].remove('pants')
boxes[0].append('rocket')
boxes[0].append('key')

# Put the train and the sock into Box 3.
boxes[3].append('train')
boxes[3].append('sock')

# Remove the butterfly and the octopus from Box 10.
boxes[10].remove('butterfly')
boxes[10].remove('octopus')

# Replace the rain with the pot in Box 8.
boxes[8].remove('rain')
boxes[8].append('pot')

# Remove the rocket from Box 0.
boxes[0].remove('rocket')

# Swap the microscope in Box 9 with the wallet in Box 3.
boxes[3].remove('wallet')
boxes[9].remove('microscope')
boxes[3].append('microscope')
boxes[9].append('wallet')

# Empty Box 6.
boxes[6] = []

# Remove the bicycle and the boot and the belt from Box 5.
items_to_remove = ['bicycle', 'boot', 'belt']
for item in items_to_remove:
    boxes[5].remove(item)

# Remove the jacket from Box 7.
boxes[7].remove('jacket')

# Remove the key from Box 0.
boxes[0].remove('key')

# Replace the pot with the meteor in Box 4.
boxes[4].remove('pot')
boxes[4].append('meteor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")