# Initial state of boxes
boxes = {
    0: ['note', 'shelf', 'bracelet', 'freezer', 'forest'],
    1: ['cloud', 'mountain', 'table', 'sculpture'],
    2: ['bowl'],
    3: ['speaker', 'cow', 'ship'],
    4: ['pen'],
    5: ['console', 'perfume', 'coin'],
    6: ['lipstick', 'makeup', 'lightning'],
    7: ['shampoo', 'scissors']
}

# Remove the shampoo from Box 7.
boxes[7].remove('shampoo')

# Move the shelf and the note and the forest from Box 0 to Box 1.
items_to_move = ['shelf', 'note', 'forest']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Put the wire into Box 5.
boxes[5].append('wire')

# Remove the perfume from Box 5.
boxes[5].remove('perfume')

# Swap the bowl in Box 2 with the console in Box 5.
boxes[2].remove('bowl')
boxes[5].remove('console')
boxes[2].append('console')
boxes[5].append('bowl')

# Remove the lipstick from Box 6.
boxes[6].remove('lipstick')

# Swap the freezer in Box 0 with the pen in Box 4.
boxes[0].remove('freezer')
boxes[4].remove('pen')
boxes[0].append('pen')
boxes[4].append('freezer')

# Replace the cow and the ship and the speaker with the blender and the bracelet and the mountain in Box 3.
boxes[3].remove('cow')
boxes[3].remove('ship')
boxes[3].remove('speaker')
boxes[3].append('blender')
boxes[3].append('bracelet')
boxes[3].append('mountain')

# Put the sock and the headphone and the tie into Box 7.
items_to_move = ['sock', 'headphone', 'tie']
for item in items_to_move:
    boxes[7].append(item)

# Replace the lightning and the makeup with the telescope and the blanket in Box 6.
boxes[6].remove('lightning')
boxes[6].remove('makeup')
boxes[6].append('telescope')
boxes[6].append('blanket')

# Put the bus and the soap into Box 5.
items_to_move = ['bus', 'soap']
for item in items_to_move:
    boxes[5].append(item)

# Swap the bracelet in Box 0 with the freezer in Box 4.
boxes[0].remove('bracelet')
boxes[4].remove('freezer')
boxes[0].append('freezer')
boxes[4].append('bracelet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")