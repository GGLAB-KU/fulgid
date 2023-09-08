# Initial state of boxes
boxes = {
    0: ['bowl', 'table', 'piano', 'tree', 'pillow'],
    1: ['thread', 'paint', 'ring', 'umbrella', 'cloud'],
    2: ['truck', 'submarine'],
    3: ['plane', 'controller'],
    4: [],
    5: ['bracelet', 'dress', 'boot'],
    6: [],
    7: ['apple', 'jacket', 'pants', 'helmet', 'dog'],
    8: ['train', 'swimsuit', 'necklace', 'makeup', 'phone'],
    9: ['book'],
    10: ['bag'],
    11: ['comb', 'whistle', 'tiger', 'beach', 'clock'],
    12: [],
    13: []
}

# Swap the umbrella in Box 1 with the table in Box 0.
boxes[0].remove('table')
boxes[1].remove('umbrella')
boxes[0].append('umbrella')
boxes[1].append('table')

# Put the book and the forest and the mixer into Box 13.
boxes[13].extend(['book', 'forest', 'mixer'])

# Replace the tree and the bowl with the butterfly and the sandals in Box 0.
boxes[0].remove('tree')
boxes[0].remove('bowl')
boxes[0].append('butterfly')
boxes[0].append('sandals')

# Remove the truck and the submarine from Box 2.
boxes[2].remove('truck')
boxes[2].remove('submarine')

# Swap the bag in Box 10 with the apple in Box 7.
boxes[7].remove('apple')
boxes[10].remove('bag')
boxes[7].append('bag')
boxes[10].append('apple')

# Replace the phone and the makeup and the train with the river and the camera and the glove in Box 8.
boxes[8].remove('phone')
boxes[8].remove('makeup')
boxes[8].remove('train')
boxes[8].append('river')
boxes[8].append('camera')
boxes[8].append('glove')

# Replace the tiger with the towel in Box 11.
boxes[11].remove('tiger')
boxes[11].append('towel')

# Move the paint and the table from Box 1 to Box 7.
boxes[1].remove('paint')
boxes[1].remove('table')
boxes[7].append('paint')
boxes[7].append('table')

# Put the towel and the grass into Box 8.
boxes[8].extend(['towel', 'grass'])

# Swap the plane in Box 3 with the swimsuit in Box 8.
boxes[3].remove('plane')
boxes[8].remove('swimsuit')
boxes[3].append('swimsuit')
boxes[8].append('plane')

# Swap the book in Box 13 with the bracelet in Box 5.
boxes[5].remove('bracelet')
boxes[13].remove('book')
boxes[5].append('book')
boxes[13].append('bracelet')

# Remove the book from Box 9.
boxes[9].remove('book')

# Move the mixer and the forest from Box 13 to Box 2.
boxes[13].remove('mixer')
boxes[13].remove('forest')
boxes[2].append('mixer')
boxes[2].append('forest')

# Put the microscope and the paint and the bear into Box 4.
boxes[4].extend(['microscope', 'paint', 'bear'])

# Move the cloud and the thread and the ring from Box 1 to Box 0.
boxes[1].remove('cloud')
boxes[1].remove('thread')
boxes[1].remove('ring')
boxes[0].append('cloud')
boxes[0].append('thread')
boxes[0].append('ring')

# Move the swimsuit and the controller from Box 3 to Box 9.
boxes[3].remove('swimsuit')
boxes[3].remove('controller')
boxes[9].append('swimsuit')
boxes[9].append('controller')

# Move the pillow and the butterfly and the thread from Box 0 to Box 13.
boxes[0].remove('pillow')
boxes[0].remove('butterfly')
boxes[0].remove('thread')
boxes[13].append('pillow')
boxes[13].append('butterfly')
boxes[13].append('thread')

# Remove the mixer from Box 2.
boxes[2].remove('mixer')

# Put the mirror and the star into Box 7.
boxes[7].extend(['mirror', 'star'])

# Remove the butterfly and the bracelet and the thread from Box 13.
boxes[13].remove('butterfly')
boxes[13].remove('bracelet')
boxes[13].remove('thread')

# Move the beach and the whistle from Box 11 to Box 0.
boxes[11].remove('beach')
boxes[11].remove('whistle')
boxes[0].append('beach')
boxes[0].append('whistle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")