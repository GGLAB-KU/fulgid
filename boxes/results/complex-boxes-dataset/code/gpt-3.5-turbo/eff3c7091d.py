# Initial state of boxes
boxes = {
    0: ['coin', 'battery'],
    1: ['sock', 'wire', 'comb'],
    2: ['zipper', 'key'],
    3: [],
    4: ['elephant'],
    5: ['controller', 'bus', 'cow', 'plate', 'jacket'],
    6: ['clock', 'jungle', 'laptop', 'pen'],
    7: ['paint', 'shelf'],
    8: ['vase', 'plane']
}

# Remove the battery and the coin from Box 0.
boxes[0].remove('battery')
boxes[0].remove('coin')

# Replace the elephant with the skirt in Box 4.
boxes[4].remove('elephant')
boxes[4].append('skirt')

# Move the wire and the sock from Box 1 to Box 8.
items_to_move = ['wire', 'sock']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Put the vase and the wig into Box 4.
boxes[4].append('vase')
boxes[4].append('wig')

# Swap the shelf in Box 7 with the zipper in Box 2.
boxes[7].remove('shelf')
boxes[2].remove('zipper')
boxes[7].append('zipper')
boxes[2].append('shelf')

# Move the skirt and the wig and the vase from Box 4 to Box 0.
items_to_move = ['skirt', 'wig', 'vase']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Put the necklace into Box 2.
boxes[2].append('necklace')

# Replace the key with the skirt in Box 2.
boxes[2].remove('key')
boxes[2].append('skirt')

# Put the pan and the doll and the button into Box 5.
items_to_put = ['pan', 'doll', 'button']
for item in items_to_put:
    boxes[5].append(item)

# Put the umbrella into Box 4.
boxes[4].append('umbrella')

# Swap the comb in Box 1 with the paint in Box 7.
boxes[1].remove('comb')
boxes[7].remove('paint')
boxes[1].append('paint')
boxes[7].append('comb')

# Move the necklace and the shelf and the skirt from Box 2 to Box 3.
items_to_move = ['necklace', 'shelf', 'skirt']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Replace the skirt and the necklace and the shelf with the bowl and the coral and the spoon in Box 3.
boxes[3].remove('skirt')
boxes[3].remove('necklace')
boxes[3].remove('shelf')
boxes[3].append('bowl')
boxes[3].append('coral')
boxes[3].append('spoon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")