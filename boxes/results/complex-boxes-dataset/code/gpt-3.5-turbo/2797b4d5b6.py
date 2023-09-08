# Initial state of boxes
boxes = {
    0: [],
    1: ['vase'],
    2: ['lion', 'book', 'comb'],
    3: ['shelf', 'river', 'moon', 'lightning', 'bag'],
    4: ['key'],
    5: ['dice', 'boot', 'jacket'],
    6: ['dog', 'storm', 'button'],
    7: ['shampoo', 'apple'],
    8: [],
    9: ['lipstick']
}

# Remove the lipstick from Box 9.
boxes[9].remove('lipstick')

# Swap the shelf in Box 3 with the boot in Box 5.
boxes[3].remove('shelf')
boxes[5].remove('boot')
boxes[3].append('boot')
boxes[5].append('shelf')

# Put the belt and the bicycle and the sculpture into Box 7.
items_to_move = ['belt', 'bicycle', 'sculpture']
for item in items_to_move:
    boxes[7].append(item)

# Put the chair and the grass into Box 6.
items_to_move = ['chair', 'grass']
for item in items_to_move:
    boxes[6].append(item)

# Replace the dice with the seaweed in Box 5.
boxes[5].remove('dice')
boxes[5].append('seaweed')

# Remove the lion from Box 2.
boxes[2].remove('lion')

# Swap the bag in Box 3 with the comb in Box 2.
boxes[3].remove('bag')
boxes[2].remove('comb')
boxes[3].append('comb')
boxes[2].append('bag')

# Put the toaster and the clock and the button into Box 5.
items_to_move = ['toaster', 'clock', 'button']
for item in items_to_move:
    boxes[5].append(item)

# Put the makeup into Box 9.
boxes[9].append('makeup')

# Put the car and the needle into Box 0.
items_to_move = ['car', 'needle']
for item in items_to_move:
    boxes[0].append(item)

# Replace the makeup with the shark in Box 9.
boxes[9].remove('makeup')
boxes[9].append('shark')

# Replace the apple and the belt with the cow and the snow in Box 7.
boxes[7].remove('apple')
boxes[7].remove('belt')
boxes[7].append('cow')
boxes[7].append('snow')

# Remove the shark from Box 9.
boxes[9].remove('shark')

# Put the rain into Box 8.
boxes[8].append('rain')

# Move the book from Box 2 to Box 0.
boxes[2].remove('book')
boxes[0].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")