# Initial state of boxes
boxes = {
    0: ['dress', 'rain', 'comb', 'button'],
    1: ['coin', 'sock', 'charger', 'whistle', 'rock'],
    2: ['bag', 'pillow'],
    3: ['perfume'],
    4: ['crown', 'puzzle', 'shampoo', 'note', 'submarine'],
    5: ['brush', 'necklace', 'lock'],
    6: ['cup', 'vase', 'comet', 'telescope', 'train'],
    7: [],
    8: ['polish', 'watch', 'freezer', 'book', 'blender']
}

# Remove the sock and the rock from Box 1.
boxes[1].remove('sock')
boxes[1].remove('rock')

# Remove the polish from Box 8.
boxes[8].remove('polish')

# Swap the blender in Box 8 with the charger in Box 1.
boxes[8].remove('blender')
boxes[1].remove('charger')
boxes[8].append('charger')
boxes[1].append('blender')

# Put the boot into Box 2.
boxes[2].append('boot')

# Move the necklace from Box 5 to Box 1.
boxes[5].remove('necklace')
boxes[1].append('necklace')

# Swap the comet in Box 6 with the pillow in Box 2.
boxes[6].remove('comet')
boxes[2].remove('pillow')
boxes[6].append('pillow')
boxes[2].append('comet')

# Move the comb and the dress from Box 0 to Box 2.
items_to_move = ['comb', 'dress']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Remove the submarine and the note and the puzzle from Box 4.
items_to_remove = ['submarine', 'note', 'puzzle']
for item in items_to_remove:
    boxes[4].remove(item)

# Replace the lock with the thunder in Box 5.
boxes[5].remove('lock')
boxes[5].append('thunder')

# Swap the freezer in Box 8 with the button in Box 0.
boxes[8].remove('freezer')
boxes[0].remove('button')
boxes[8].append('button')
boxes[0].append('freezer')

# Swap the bag in Box 2 with the freezer in Box 0.
boxes[2].remove('bag')
boxes[0].remove('freezer')
boxes[2].append('freezer')
boxes[0].append('bag')

# Move the rain and the bag from Box 0 to Box 6.
items_to_move = ['rain', 'bag']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Move the blender and the whistle from Box 1 to Box 2.
items_to_move = ['blender', 'whistle']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")