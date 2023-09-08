# Initial state of boxes
boxes = {
    0: [],
    1: ['horn', 'bus', 'storm'],
    2: [],
    3: ['clock', 'pan', 'headphone', 'dolphin'],
    4: ['forest', 'fork', 'necklace'],
    5: ['paint', 'harmonica', 'crown', 'bracelet', 'car'],
    6: []
}

# Move the clock and the dolphin and the headphone from Box 3 to Box 1.
items_to_move = ['clock', 'dolphin', 'headphone']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Replace the crown and the paint and the car with the grinder and the bird and the octopus in Box 5.
items_to_replace = ['crown', 'paint', 'car']
items_to_add = ['grinder', 'bird', 'octopus']
for item_to_replace, item_to_add in zip(items_to_replace, items_to_add):
    boxes[5].remove(item_to_replace)
    boxes[5].append(item_to_add)

# Put the puzzle into Box 4.
boxes[4].append('puzzle')

# Put the plane and the grass and the motorcycle into Box 0.
items_to_add = ['plane', 'grass', 'motorcycle']
for item in items_to_add:
    boxes[0].append(item)

# Put the dolphin and the pants into Box 6.
items_to_add = ['dolphin', 'pants']
for item in items_to_add:
    boxes[6].append(item)

# Replace the plane and the grass and the motorcycle with the lightning and the shorts and the button in Box 0.
items_to_replace = ['plane', 'grass', 'motorcycle']
items_to_add = ['lightning', 'shorts', 'button']
for item_to_replace, item_to_add in zip(items_to_replace, items_to_add):
    boxes[0].remove(item_to_replace)
    boxes[0].append(item_to_add)

# Replace the shorts and the button and the lightning with the shark and the game and the dice in Box 0.
items_to_replace = ['shorts', 'button', 'lightning']
items_to_add = ['shark', 'game', 'dice']
for item_to_replace, item_to_add in zip(items_to_replace, items_to_add):
    boxes[0].remove(item_to_replace)
    boxes[0].append(item_to_add)

# Put the shark into Box 1.
boxes[1].append('shark')

# Move the forest and the necklace and the fork from Box 4 to Box 6.
items_to_move = ['forest', 'necklace', 'fork']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Put the seaweed into Box 3.
boxes[3].append('seaweed')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")