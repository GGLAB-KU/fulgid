# Initial state of boxes
boxes = {
    0: ['magnet', 'telescope', 'doll'],
    1: ['earring', 'rock', 'car'],
    2: ['brush', 'fish', 'table'],
    3: ['tiger', 'jungle'],
    4: ['fridge', 'grass', 'motorcycle', 'drum']
}

# Move the table from Box 2 to Box 0.
boxes[2].remove('table')
boxes[0].append('table')

# Remove the doll from Box 0.
boxes[0].remove('doll')

# Swap the earring in Box 1 with the fridge in Box 4.
boxes[1].remove('earring')
boxes[4].remove('fridge')
boxes[1].append('fridge')
boxes[4].append('earring')

# Put the cow into Box 2.
boxes[2].append('cow')

# Put the bear and the game into Box 1.
boxes[1].append('bear')
boxes[1].append('game')

# Remove the fish and the cow from Box 2.
boxes[2].remove('fish')
boxes[2].remove('cow')

# Move the motorcycle and the drum and the earring from Box 4 to Box 2.
items_to_move = ['motorcycle', 'drum', 'earring']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")