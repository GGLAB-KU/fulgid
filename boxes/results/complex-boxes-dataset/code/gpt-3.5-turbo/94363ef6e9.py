# Initial state of boxes
boxes = {
    0: ['battery', 'sandals', 'cow', 'train', 'zipper'],
    1: ['plate', 'lipstick', 'pan', 'candle'],
    2: ['doll', 'boot', 'book'],
    3: [],
    4: ['butterfly'],
    5: ['branch', 'rain']
}

# Replace the book and the boot and the doll with the candle and the comb and the sun in Box 2.
boxes[2].remove('book')
boxes[2].remove('boot')
boxes[2].remove('doll')
boxes[2].append('candle')
boxes[2].append('comb')
boxes[2].append('sun')

# Put the elephant and the submarine into Box 4.
boxes[4].append('elephant')
boxes[4].append('submarine')

# Replace the battery with the dress in Box 0.
boxes[0].remove('battery')
boxes[0].append('dress')

# Remove the zipper and the sandals from Box 0.
boxes[0].remove('zipper')
boxes[0].remove('sandals')

# Move the plate and the candle and the lipstick from Box 1 to Box 2.
items_to_move = ['plate', 'candle', 'lipstick']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Put the flute and the laptop and the candle into Box 3.
boxes[3].append('flute')
boxes[3].append('laptop')
boxes[3].append('candle')

# Put the scarf into Box 4.
boxes[4].append('scarf')

# Move the dress and the train and the cow from Box 0 to Box 3.
items_to_move = ['dress', 'train', 'cow']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Remove the rain and the branch from Box 5.
boxes[5].remove('rain')
boxes[5].remove('branch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")