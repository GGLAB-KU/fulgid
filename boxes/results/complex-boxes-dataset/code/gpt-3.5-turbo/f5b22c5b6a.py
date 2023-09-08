# Initial state of boxes
boxes = {
    0: ['sandals'],
    1: ['comb', 'phone'],
    2: [],
    3: ['book', 'starfish', 'toothpaste', 'note', 'needle'],
    4: ['clock', 'cup', 'coral', 'shoes'],
    5: []
}

# Replace the sandals with the plane in Box 0.
boxes[0].remove('sandals')
boxes[0].append('plane')

# Put the bowl into Box 4.
boxes[4].append('bowl')

# Put the dress into Box 3.
boxes[3].append('dress')

# Swap the clock in Box 4 with the plane in Box 0.
boxes[0].remove('plane')
boxes[4].remove('clock')
boxes[0].append('clock')
boxes[4].append('plane')

# Remove the coral and the bowl from Box 4.
boxes[4].remove('coral')
boxes[4].remove('bowl')

# Put the wire and the cat and the coat into Box 4.
boxes[4].append('wire')
boxes[4].append('cat')
boxes[4].append('coat')

# Move the clock from Box 0 to Box 4.
boxes[0].remove('clock')
boxes[4].append('clock')

# Move the comb and the phone from Box 1 to Box 0.
boxes[1].remove('comb')
boxes[1].remove('phone')
boxes[0].append('comb')
boxes[0].append('phone')

# Put the earring into Box 5.
boxes[5].append('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")