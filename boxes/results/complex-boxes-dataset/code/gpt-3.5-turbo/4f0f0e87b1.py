# Initial state of boxes
boxes = {
    0: ['flute'],
    1: ['controller', 'shirt'],
    2: ['dice', 'polish', 'soap'],
    3: ['jacket', 'apple', 'phone', 'speaker'],
    4: ['coral', 'river', 'swimsuit']
}

# Put the rocket and the rock and the dolphin into Box 1.
boxes[1].append('rocket')
boxes[1].append('rock')
boxes[1].append('dolphin')

# Put the swimsuit into Box 0.
boxes[0].append('swimsuit')

# Move the swimsuit and the flute from Box 0 to Box 1.
items_to_move = ['swimsuit', 'flute']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Remove the soap from Box 2.
boxes[2].remove('soap')

# Move the jacket and the speaker and the phone from Box 3 to Box 1.
items_to_move = ['jacket', 'speaker', 'phone']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Swap the apple in Box 3 with the coral in Box 4.
boxes[3].remove('apple')
boxes[4].remove('coral')
boxes[3].append('coral')
boxes[4].append('apple')

# Swap the controller in Box 1 with the polish in Box 2.
boxes[1].remove('controller')
boxes[2].remove('polish')
boxes[1].append('polish')
boxes[2].append('controller')

# Put the bracelet into Box 2.
boxes[2].append('bracelet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")