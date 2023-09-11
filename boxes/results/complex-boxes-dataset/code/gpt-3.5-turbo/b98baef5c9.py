# Initial state of boxes
boxes = {
    0: ['telescope', 'drum'],
    1: ['sock', 'shorts', 'mixer', 'note'],
    2: ['camera', 'gloves', 'moon'],
    3: ['plate'],
    4: ['candle']
}

# Move the gloves from Box 2 to Box 0.
boxes[0].append(boxes[2].pop(1))

# Swap the drum in Box 0 with the sock in Box 1.
boxes[0][1], boxes[1][0] = boxes[1][0], boxes[0][1]

# Put the belt and the drum into Box 1.
boxes[1].extend(['belt', 'drum'])

# Move the gloves and the sock and the telescope from Box 0 to Box 4.
items_to_move = ['gloves', 'sock', 'telescope']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Remove the camera and the moon from Box 2.
boxes[2].remove('camera')
boxes[2].remove('moon')

# Move the sock and the telescope from Box 4 to Box 2.
items_to_move = ['sock', 'telescope']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Move the candle and the gloves from Box 4 to Box 2.
items_to_move = ['candle', 'gloves']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Move the plate from Box 3 to Box 2.
boxes[3].remove('plate')
boxes[2].append('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")