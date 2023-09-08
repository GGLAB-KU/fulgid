# Initial state of boxes
boxes = {
    0: ['flute', 'pot'],
    1: ['shoes', 'controller', 'bear', 'chair'],
    2: ['pen', 'brush', 'pan', 'usb'],
    3: ['mixer', 'ship', 'guitar', 'freezer', 'car'],
    4: ['meteor', 'makeup', 'rocket', 'comb'],
    5: ['camera', 'mirror'],
    6: ['train', 'dolphin', 'plate', 'bowl', 'lamp'],
    7: ['pillow', 'game', 'zipper', 'lipstick', 'button'],
    8: [],
    9: ['fork', 'bicycle'],
    10: ['snow', 'cup', 'belt', 'bird', 'note'],
    11: ['table', 'swimsuit', 'blanket'],
    12: ['telescope'],
    13: ['coat', 'desert'],
    14: ['bag', 'watch', 'whistle', 'scissors']
}

# Remove the blanket and the swimsuit from Box 11.
boxes[11].remove('blanket')
boxes[11].remove('swimsuit')

# Remove the table from Box 11.
boxes[11].remove('table')

# Move the telescope from Box 12 to Box 11.
boxes[12].remove('telescope')
boxes[11].append('telescope')

# Remove the guitar and the mixer from Box 3.
boxes[3].remove('guitar')
boxes[3].remove('mixer')

# Swap the bowl in Box 6 with the ship in Box 3.
boxes[6].remove('bowl')
boxes[3].remove('ship')
boxes[6].append('ship')
boxes[3].append('bowl')

# Remove the mirror and the camera from Box 5.
boxes[5].remove('mirror')
boxes[5].remove('camera')

# Swap the zipper in Box 7 with the flute in Box 0.
boxes[7].remove('zipper')
boxes[0].remove('flute')
boxes[7].append('flute')
boxes[0].append('zipper')

# Move the freezer and the car from Box 3 to Box 10.
boxes[3].remove('freezer')
boxes[3].remove('car')
boxes[10].append('freezer')
boxes[10].append('car')

# Swap the comb in Box 4 with the shoes in Box 1.
boxes[4].remove('comb')
boxes[1].remove('shoes')
boxes[4].append('shoes')
boxes[1].append('comb')

# Move the train from Box 6 to Box 2.
boxes[6].remove('train')
boxes[2].append('train')

# Move the bowl from Box 3 to Box 5.
boxes[3].remove('bowl')
boxes[5].append('bowl')

# Put the train into Box 8.
boxes[8].append('train')

# Put the spoon and the microwave into Box 1.
boxes[1].append('spoon')
boxes[1].append('microwave')

# Move the pen from Box 2 to Box 12.
boxes[2].remove('pen')
boxes[12].append('pen')

# Replace the brush with the belt in Box 2.
boxes[2].remove('brush')
boxes[2].append('belt')

# Move the coat from Box 13 to Box 14.
boxes[13].remove('coat')
boxes[14].append('coat')

# Remove the whistle and the coat from Box 14.
boxes[14].remove('whistle')
boxes[14].remove('coat')

# Replace the pen with the candle in Box 12.
boxes[12].remove('pen')
boxes[12].append('candle')

# Remove the fork and the bicycle from Box 9.
boxes[9].remove('fork')
boxes[9].remove('bicycle')

# Replace the train with the forest in Box 8.
boxes[8].remove('train')
boxes[8].append('forest')

# Move the bear and the controller from Box 1 to Box 2.
boxes[1].remove('bear')
boxes[1].remove('controller')
boxes[2].append('bear')
boxes[2].append('controller')

# Remove the plate from Box 6.
boxes[6].remove('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")