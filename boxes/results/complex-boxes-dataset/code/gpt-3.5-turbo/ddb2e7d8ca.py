# Initial state of boxes
boxes = {
    0: ['ocean', 'truck', 'bus', 'cat'],
    1: [],
    2: ['branch', 'razor', 'toy'],
    3: ['microwave', 'piano'],
    4: [],
    5: ['gloves']
}

# Put the swimsuit and the brush into Box 1.
boxes[1].append('swimsuit')
boxes[1].append('brush')

# Replace the gloves with the wig in Box 5.
boxes[5].remove('gloves')
boxes[5].append('wig')

# Swap the bus in Box 0 with the swimsuit in Box 1.
boxes[0].remove('bus')
boxes[1].remove('swimsuit')
boxes[0].append('swimsuit')
boxes[1].append('bus')

# Put the oven and the table into Box 3.
boxes[3].append('oven')
boxes[3].append('table')

# Move the wig from Box 5 to Box 2.
boxes[5].remove('wig')
boxes[2].append('wig')

# Put the basket and the blanket and the lock into Box 2.
boxes[2].append('basket')
boxes[2].append('blanket')
boxes[2].append('lock')

# Put the shampoo and the pot into Box 4.
boxes[4].append('shampoo')
boxes[4].append('pot')

# Swap the bus in Box 1 with the shampoo in Box 4.
boxes[1].remove('bus')
boxes[4].remove('shampoo')
boxes[1].append('shampoo')
boxes[4].append('bus')

# Move the wig and the toy and the basket from Box 2 to Box 5.
items_to_move = ['wig', 'toy', 'basket']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")