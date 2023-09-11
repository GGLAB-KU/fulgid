# Initial state of boxes
boxes = {
    0: ['pan', 'blanket', 'speaker', 'oven'],
    1: ['snow', 'shirt', 'pillow'],
    2: ['tiger', 'helmet', 'wallet', 'river', 'toy'],
    3: []
}

# Move the pillow and the shirt from Box 1 to Box 2.
boxes[1].remove('pillow')
boxes[1].remove('shirt')
boxes[2].append('pillow')
boxes[2].append('shirt')

# Put the meteor and the zipper into Box 1.
boxes[1].append('meteor')
boxes[1].append('zipper')

# Replace the blanket and the speaker with the keyboard and the comet in Box 0.
boxes[0].remove('blanket')
boxes[0].remove('speaker')
boxes[0].append('keyboard')
boxes[0].append('comet')

# Remove the pan and the keyboard and the oven from Box 0.
boxes[0].remove('pan')
boxes[0].remove('keyboard')
boxes[0].remove('oven')

# Put the sculpture and the razor into Box 1.
boxes[1].append('sculpture')
boxes[1].append('razor')

# Move the helmet and the wallet and the toy from Box 2 to Box 3.
items_to_move = ['helmet', 'wallet', 'toy']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")