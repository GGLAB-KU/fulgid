# Initial state of boxes
boxes = {
    0: ['skirt', 'shorts', 'towel', 'needle'],
    1: ['shark', 'comb', 'bus'],
    2: [],
    3: ['candle'],
    4: []
}

# Swap the needle in Box 0 with the candle in Box 3.
boxes[0].remove('needle')
boxes[3].remove('candle')
boxes[0].append('candle')
boxes[3].append('needle')

# Replace the shorts with the cow in Box 0.
boxes[0].remove('shorts')
boxes[0].append('cow')

# Move the cow and the skirt and the towel from Box 0 to Box 4.
items_to_move = ['cow', 'skirt', 'towel']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Replace the skirt and the cow with the keyboard and the plane in Box 4.
boxes[4].remove('skirt')
boxes[4].remove('cow')
boxes[4].append('keyboard')
boxes[4].append('plane')

# Put the toy and the soap into Box 3.
boxes[3].append('toy')
boxes[3].append('soap')

# Move the toy and the needle from Box 3 to Box 2.
boxes[3].remove('toy')
boxes[3].remove('needle')
boxes[2].append('toy')
boxes[2].append('needle')

# Replace the plane and the keyboard with the whistle and the button in Box 4.
boxes[4].remove('plane')
boxes[4].remove('keyboard')
boxes[4].append('whistle')
boxes[4].append('button')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")