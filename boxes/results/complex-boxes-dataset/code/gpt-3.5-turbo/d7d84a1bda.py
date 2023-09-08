# Initial state of boxes
boxes = {
    0: ['flute', 'comb', 'card', 'cup'],
    1: ['coin'],
    2: ['bicycle', 'river', 'towel', 'lamp'],
    3: [],
    4: ['shoes', 'bracelet', 'thread', 'controller'],
    5: ['planet', 'pants'],
    6: []
}

# Remove the coin from Box 1.
boxes[1].remove('coin')

# Move the river and the towel from Box 2 to Box 3.
items_to_move = ['river', 'towel']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Replace the river with the sun in Box 3.
boxes[3].remove('river')
boxes[3].append('sun')

# Replace the lamp with the pen in Box 2.
boxes[2].remove('lamp')
boxes[2].append('pen')

# Swap the shoes in Box 4 with the towel in Box 3.
boxes[4].remove('shoes')
boxes[3].remove('towel')
boxes[4].append('towel')
boxes[3].append('shoes')

# Put the keyboard and the headphone and the tiger into Box 4.
items_to_move = ['keyboard', 'headphone', 'tiger']
for item in items_to_move:
    boxes[4].append(item)

# Empty Box 0.
boxes[0] = []

# Remove the thread from Box 4.
boxes[4].remove('thread')

# Move the pants from Box 5 to Box 2.
boxes[5].remove('pants')
boxes[2].append('pants')

# Replace the bracelet and the tiger and the towel with the vase and the grinder and the headphone in Box 4.
boxes[4].remove('bracelet')
boxes[4].remove('tiger')
boxes[4].remove('towel')
boxes[4].append('vase')
boxes[4].append('grinder')
boxes[4].append('headphone')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")