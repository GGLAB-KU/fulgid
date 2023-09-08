# Initial state of boxes
boxes = {
    0: ['lion', 'pillow', 'helmet', 'belt'],
    1: ['magnet', 'button'],
    2: ['bell', 'console', 'hat', 'razor', 'glasses'],
    3: ['toothbrush', 'guitar', 'table'],
    4: [],
    5: [],
    6: ['telescope', 'rock', 'vase', 'dog', 'river'],
    7: ['mask', 'wire', 'bag', 'shark', 'rain']
}

# Swap the magnet in Box 1 with the guitar in Box 3.
boxes[1].remove('magnet')
boxes[3].remove('guitar')
boxes[1].append('guitar')
boxes[3].append('magnet')

# Move the rain and the bag from Box 7 to Box 5.
items_to_move = ['rain', 'bag']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Replace the console and the razor and the hat with the brush and the pen and the keyboard in Box 2.
boxes[2].remove('console')
boxes[2].remove('razor')
boxes[2].remove('hat')
boxes[2].append('brush')
boxes[2].append('pen')
boxes[2].append('keyboard')

# Remove the rain from Box 5.
boxes[5].remove('rain')

# Swap the guitar in Box 1 with the pillow in Box 0.
boxes[1].remove('guitar')
boxes[0].remove('pillow')
boxes[1].append('pillow')
boxes[0].append('guitar')

# Replace the keyboard with the zipper in Box 2.
boxes[2].remove('keyboard')
boxes[2].append('zipper')

# Swap the glasses in Box 2 with the wire in Box 7.
boxes[2].remove('glasses')
boxes[7].remove('wire')
boxes[2].append('wire')
boxes[7].append('glasses')

# Move the button and the pillow from Box 1 to Box 5.
items_to_move = ['button', 'pillow']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Remove the guitar and the lion and the helmet from Box 0.
items_to_remove = ['guitar', 'lion', 'helmet']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the ship into Box 6.
boxes[6].append('ship')

# Move the belt from Box 0 to Box 5.
boxes[0].remove('belt')
boxes[5].append('belt')

# Move the brush and the zipper from Box 2 to Box 0.
items_to_move = ['brush', 'zipper']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")