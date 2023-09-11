# Initial state of boxes
boxes = {
    0: ['dice', 'seaweed', 'toaster', 'rocket'],
    1: ['harmonica', 'island', 'car', 'bowl'],
    2: ['flute'],
    3: [],
    4: ['mountain', 'rock', 'swimsuit', 'pan']
}

# Remove the swimsuit from Box 4.
boxes[4].remove('swimsuit')

# Put the scissors and the sock and the sun into Box 2.
items_to_add = ['scissors', 'sock', 'sun']
for item in items_to_add:
    boxes[2].append(item)

# Move the harmonica and the island from Box 1 to Box 0.
items_to_move = ['harmonica', 'island']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Put the pants and the dolphin into Box 2.
items_to_add = ['pants', 'dolphin']
for item in items_to_add:
    boxes[2].append(item)

# Put the train into Box 3.
boxes[3].append('train')

# Replace the rock and the pan and the mountain with the bag and the shirt and the headphone in Box 4.
boxes[4].remove('rock')
boxes[4].remove('pan')
boxes[4].remove('mountain')
boxes[4].append('bag')
boxes[4].append('shirt')
boxes[4].append('headphone')

# Move the bowl from Box 1 to Box 2.
boxes[1].remove('bowl')
boxes[2].append('bowl')

# Swap the car in Box 1 with the train in Box 3.
boxes[1].remove('car')
boxes[3].remove('train')
boxes[1].append('train')
boxes[3].append('car')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")