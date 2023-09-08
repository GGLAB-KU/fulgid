# Initial state of boxes
boxes = {
    0: ['clock', 'shark', 'tape', 'train'],
    1: [],
    2: ['bell', 'battery', 'magnet', 'candle', 'earring'],
    3: ['plane', 'mixer'],
    4: ['bear'],
    5: ['bag', 'pillow', 'scissors'],
    6: ['cow', 'tiger'],
    7: ['violin']
}

# Move the violin from Box 7 to Box 5.
boxes[7].remove('violin')
boxes[5].append('violin')

# Swap the magnet in Box 2 with the clock in Box 0.
boxes[2].remove('magnet')
boxes[0].remove('clock')
boxes[2].append('clock')
boxes[0].append('magnet')

# Swap the tiger in Box 6 with the mixer in Box 3.
boxes[6].remove('tiger')
boxes[3].remove('mixer')
boxes[6].append('mixer')
boxes[3].append('tiger')

# Put the toaster and the clock and the sock into Box 7.
items_to_move = ['toaster', 'clock', 'sock']
for item in items_to_move:
    boxes[7].append(item)

# Remove the cow and the mixer from Box 6.
boxes[6].remove('cow')
boxes[6].remove('mixer')

# Put the towel and the freezer into Box 7.
items_to_move = ['towel', 'freezer']
for item in items_to_move:
    boxes[7].append(item)

# Remove the towel and the clock from Box 7.
boxes[7].remove('towel')
boxes[7].remove('clock')

# Swap the pillow in Box 5 with the sock in Box 7.
boxes[5].remove('pillow')
boxes[7].remove('sock')
boxes[5].append('sock')
boxes[7].append('pillow')

# Put the shampoo and the grass into Box 5.
items_to_move = ['shampoo', 'grass']
for item in items_to_move:
    boxes[5].append(item)

# Swap the train in Box 0 with the bell in Box 2.
boxes[0].remove('train')
boxes[2].remove('bell')
boxes[0].append('bell')
boxes[2].append('train')

# Put the apple and the bicycle and the horse into Box 7.
items_to_move = ['apple', 'bicycle', 'horse']
for item in items_to_move:
    boxes[7].append(item)

# Move the bear from Box 4 to Box 5.
boxes[4].remove('bear')
boxes[5].append('bear')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")