# Initial state of boxes
boxes = {
    0: ['game', 'bird', 'bell'],
    1: ['skirt', 'mountain', 'brush', 'grinder'],
    2: ['toy', 'harmonica', 'comb'],
    3: ['boat'],
    4: ['frame', 'pillow'],
    5: ['lion', 'wallet', 'flute'],
    6: ['pot']
}

# Put the speaker into Box 6.
boxes[6].append('speaker')

# Move the boat from Box 3 to Box 2.
boxes[2].append(boxes[3].pop())

# Remove the wallet from Box 5.
boxes[5].remove('wallet')

# Move the grinder and the brush and the mountain from Box 1 to Box 6.
items_to_move = ['grinder', 'brush', 'mountain']
for item in items_to_move:
    boxes[6].append(boxes[1].pop())

# Remove the lion from Box 5.
boxes[5].remove('lion')

# Replace the comb and the harmonica and the toy with the controller and the zipper and the dice in Box 2.
boxes[2].remove('comb')
boxes[2].remove('harmonica')
boxes[2].remove('toy')
boxes[2].append('controller')
boxes[2].append('zipper')
boxes[2].append('dice')

# Move the dice and the controller and the zipper from Box 2 to Box 1.
items_to_move = ['dice', 'controller', 'zipper']
for item in items_to_move:
    boxes[1].append(boxes[2].pop())

# Replace the flute with the bowl in Box 5.
boxes[5].remove('flute')
boxes[5].append('bowl')

# Put the cow and the rock and the blanket into Box 1.
items_to_put = ['cow', 'rock', 'blanket']
for item in items_to_put:
    boxes[1].append(item)

# Move the bell from Box 0 to Box 2.
boxes[2].append(boxes[0].pop())

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")