# Initial state of boxes
boxes = {
    0: ['cat', 'shoe', 'grass', 'candle', 'horse'],
    1: ['card', 'soap'],
    2: [],
    3: ['motorcycle', 'piano', 'vase'],
    4: [],
    5: ['plane', 'dog', 'fridge', 'sock']
}

# Put the toothbrush and the coral into Box 4.
boxes[4].append('toothbrush')
boxes[4].append('coral')

# Replace the vase and the motorcycle with the brush and the shampoo in Box 3.
boxes[3].remove('vase')
boxes[3].remove('motorcycle')
boxes[3].append('brush')
boxes[3].append('shampoo')

# Move the dog and the fridge from Box 5 to Box 3.
items_to_move = ['dog', 'fridge']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Move the dog and the shampoo from Box 3 to Box 0.
items_to_move = ['dog', 'shampoo']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Put the bear and the thunder and the glasses into Box 2.
items_to_put = ['bear', 'thunder', 'glasses']
for item in items_to_put:
    boxes[2].append(item)

# Replace the plane and the sock with the toy and the guitar in Box 5.
boxes[5].remove('plane')
boxes[5].remove('sock')
boxes[5].append('toy')
boxes[5].append('guitar')

# Move the glasses from Box 2 to Box 0.
boxes[2].remove('glasses')
boxes[0].append('glasses')

# Swap the dog in Box 0 with the thunder in Box 2.
boxes[0].remove('dog')
boxes[2].remove('thunder')
boxes[0].append('thunder')
boxes[2].append('dog')

# Move the card from Box 1 to Box 0.
boxes[1].remove('card')
boxes[0].append('card')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")