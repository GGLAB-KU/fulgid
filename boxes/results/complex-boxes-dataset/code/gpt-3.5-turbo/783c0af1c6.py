# Initial state of boxes
boxes = {
    0: [],
    1: ['ship', 'note', 'butterfly', 'bear', 'dice'],
    2: ['controller', 'flute'],
    3: ['mask', 'doll', 'candle'],
    4: ['jacket', 'river', 'swimsuit', 'helmet'],
    5: ['cup', 'razor', 'dolphin']
}

# Swap the ship in Box 1 with the controller in Box 2.
boxes[1].remove('ship')
boxes[2].remove('controller')
boxes[1].append('controller')
boxes[2].append('ship')

# Put the toy into Box 4.
boxes[4].append('toy')

# Replace the note with the puzzle in Box 1.
boxes[1].remove('note')
boxes[1].append('puzzle')

# Move the bear and the dice and the controller from Box 1 to Box 4.
items_to_move = ['bear', 'dice', 'controller']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Put the lion and the key into Box 0.
boxes[0].append('lion')
boxes[0].append('key')

# Put the cow into Box 3.
boxes[3].append('cow')

# Remove the toy from Box 4.
boxes[4].remove('toy')

# Empty Box 0.
boxes[0] = []

# Swap the butterfly in Box 1 with the controller in Box 4.
boxes[1].remove('butterfly')
boxes[4].remove('controller')
boxes[1].append('controller')
boxes[4].append('butterfly')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")