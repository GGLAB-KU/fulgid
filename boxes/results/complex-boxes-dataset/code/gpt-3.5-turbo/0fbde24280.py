# Initial state of boxes
boxes = {
    0: ['bell'],
    1: ['dress', 'gloves', 'clock', 'comet'],
    2: ['polish', 'game', 'seaweed', 'table', 'meteor'],
    3: [],
    4: ['crown', 'drum', 'cow', 'toaster', 'perfume'],
    5: ['sock', 'beach'],
    6: ['spoon', 'phone', 'glove'],
    7: ['leaf', 'card', 'shorts', 'coin', 'button'],
    8: ['dice']
}

# Replace the gloves and the clock with the bicycle and the flute in Box 1.
boxes[1].remove('gloves')
boxes[1].remove('clock')
boxes[1].append('bicycle')
boxes[1].append('flute')

# Replace the shorts with the elephant in Box 7.
boxes[7].remove('shorts')
boxes[7].append('elephant')

# Swap the dice in Box 8 with the drum in Box 4.
boxes[8], boxes[4] = boxes[4], boxes[8]

# Put the boot and the bear into Box 6.
boxes[6].append('boot')
boxes[6].append('bear')

# Put the paint into Box 7.
boxes[7].append('paint')

# Remove the bell from Box 0.
boxes[0].remove('bell')

# Move the cow and the toaster and the crown from Box 4 to Box 6.
items_to_move = ['cow', 'toaster', 'crown']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Put the plane and the flute and the spoon into Box 6.
items_to_move = ['plane', 'flute', 'spoon']
for item in items_to_move:
    boxes[6].append(item)

# Put the wig and the boot and the toothbrush into Box 8.
items_to_move = ['wig', 'boot', 'toothbrush']
for item in items_to_move:
    boxes[8].append(item)

# Swap the dice in Box 4 with the beach in Box 5.
boxes[4], boxes[5] = boxes[5], boxes[4]

# Remove the dice and the sock from Box 5.
boxes[5].remove('dice')
boxes[5].remove('sock')

# Move the flute from Box 1 to Box 4.
boxes[1].remove('flute')
boxes[4].append('flute')

# Replace the coin and the elephant with the towel and the fish in Box 7.
boxes[7].remove('coin')
boxes[7].remove('elephant')
boxes[7].append('towel')
boxes[7].append('fish')

# Move the flute from Box 6 to Box 4.
boxes[6].remove('flute')
boxes[4].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")