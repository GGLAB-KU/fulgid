# Initial state of boxes
boxes = {
    0: ['cow', 'fridge', 'wig', 'shelf', 'motorcycle'],
    1: [],
    2: ['button', 'shark', 'basket', 'seaweed'],
    3: [],
    4: ['note'],
    5: ['guitar', 'watch', 'horn'],
    6: ['star'],
    7: ['microwave', 'fork', 'butterfly'],
    8: ['vase', 'desert', 'table', 'submarine', 'cup']
}

# Put the horse into Box 3.
boxes[3].append('horse')

# Put the rocket and the microscope and the meteor into Box 8.
boxes[8].append('rocket')
boxes[8].append('microscope')
boxes[8].append('meteor')

# Remove the basket and the seaweed from Box 2.
boxes[2].remove('basket')
boxes[2].remove('seaweed')

# Swap the microwave in Box 7 with the shelf in Box 0.
boxes[0].remove('shelf')
boxes[7].remove('microwave')
boxes[0].append('microwave')
boxes[7].append('shelf')

# Remove the note from Box 4.
boxes[4].remove('note')

# Remove the microscope and the submarine from Box 8.
boxes[8].remove('microscope')
boxes[8].remove('submarine')

# Move the butterfly and the fork and the shelf from Box 7 to Box 2.
items_to_move = ['butterfly', 'fork', 'shelf']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[2].append(item)

# Remove the vase and the rocket and the cup from Box 8.
items_to_remove = ['vase', 'rocket', 'cup']
for item in items_to_remove:
    boxes[8].remove(item)

# Move the horse from Box 3 to Box 6.
boxes[3].remove('horse')
boxes[6].append('horse')

# Put the clock and the shoe and the brush into Box 1.
items_to_put = ['clock', 'shoe', 'brush']
for item in items_to_put:
    boxes[1].append(item)

# Put the car and the leaf and the phone into Box 6.
items_to_put = ['car', 'leaf', 'phone']
for item in items_to_put:
    boxes[6].append(item)

# Remove the phone from Box 6.
boxes[6].remove('phone')

# Swap the horn in Box 5 with the table in Box 8.
boxes[5].remove('horn')
boxes[8].remove('table')
boxes[5].append('table')
boxes[8].append('horn')

# Replace the meteor with the earring in Box 8.
boxes[8].remove('meteor')
boxes[8].append('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")