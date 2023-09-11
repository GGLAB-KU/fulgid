# Initial state of boxes
boxes = {
    0: ['dice', 'shorts', 'car'],
    1: ['card', 'towel'],
    2: ['lightning'],
    3: ['umbrella', 'headphone'],
    4: ['telescope', 'soap', 'sandals', 'wallet'],
    5: [],
    6: [],
    7: ['river', 'doll', 'lion', 'razor', 'tie'],
    8: ['mask'],
    9: ['shelf', 'flower', 'controller', 'train', 'motorcycle'],
    10: ['thread'],
    11: ['lipstick', 'cow', 'fridge', 'puzzle', 'book'],
    12: ['truck', 'clock']
}

# Move the cow and the book from Box 11 to Box 2.
boxes[11].remove('cow')
boxes[11].remove('book')
boxes[2].append('cow')
boxes[2].append('book')

# Remove the thread from Box 10.
boxes[10].remove('thread')

# Swap the card in Box 1 with the truck in Box 12.
boxes[1].remove('card')
boxes[12].remove('truck')
boxes[1].append('truck')
boxes[12].append('card')

# Put the bell into Box 8.
boxes[8].append('bell')

# Put the pan into Box 1.
boxes[1].append('pan')

# Move the lipstick from Box 11 to Box 1.
boxes[11].remove('lipstick')
boxes[1].append('lipstick')

# Empty Box 11.
boxes[11] = []

# Move the controller and the train and the shelf from Box 9 to Box 2.
items_to_move = ['controller', 'train', 'shelf']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[2].append(item)

# Move the shorts and the car from Box 0 to Box 9.
items_to_move = ['shorts', 'car']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Swap the mask in Box 8 with the motorcycle in Box 9.
boxes[8].remove('mask')
boxes[9].remove('motorcycle')
boxes[8].append('motorcycle')
boxes[9].append('mask')

# Move the flower from Box 9 to Box 7.
boxes[9].remove('flower')
boxes[7].append('flower')

# Put the thread into Box 10.
boxes[10].append('thread')

# Remove the tie from Box 7.
boxes[7].remove('tie')

# Remove the shorts and the car and the mask from Box 9.
items_to_remove = ['shorts', 'car', 'mask']
for item in items_to_remove:
    boxes[9].remove(item)

# Move the bell and the motorcycle from Box 8 to Box 9.
boxes[8].remove('bell')
boxes[8].remove('motorcycle')
boxes[9].append('bell')
boxes[9].append('motorcycle')

# Remove the truck and the lipstick and the pan from Box 1.
items_to_remove = ['truck', 'lipstick', 'pan']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the towel in Box 1 with the clock in Box 12.
boxes[1].remove('towel')
boxes[12].remove('clock')
boxes[1].append('clock')
boxes[12].append('towel')

# Replace the umbrella and the headphone with the shelf and the tree in Box 3.
boxes[3].remove('umbrella')
boxes[3].remove('headphone')
boxes[3].append('shelf')
boxes[3].append('tree')

# Move the book and the train and the controller from Box 2 to Box 6.
items_to_move = ['book', 'train', 'controller']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Move the dice from Box 0 to Box 10.
boxes[0].remove('dice')
boxes[10].append('dice')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")