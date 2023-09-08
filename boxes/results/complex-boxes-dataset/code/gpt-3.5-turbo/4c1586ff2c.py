# Initial state of boxes
boxes = {
    0: [],
    1: ['microscope', 'needle', 'tiger'],
    2: ['cloud', 'sock', 'scarf'],
    3: ['sun', 'sandals', 'mirror'],
    4: ['butterfly', 'bell', 'plane'],
    5: ['boat'],
    6: ['table']
}

# Swap the bell in Box 4 with the boat in Box 5.
boxes[4].remove('bell')
boxes[5].remove('boat')
boxes[4].append('boat')
boxes[5].append('bell')

# Replace the tiger and the needle and the microscope with the glasses and the plane and the polish in Box 1.
boxes[1].remove('tiger')
boxes[1].remove('needle')
boxes[1].remove('microscope')
boxes[1].append('glasses')
boxes[1].append('plane')
boxes[1].append('polish')

# Move the polish and the glasses and the plane from Box 1 to Box 2.
items_to_move = ['polish', 'glasses', 'plane']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Move the scarf from Box 2 to Box 3.
boxes[2].remove('scarf')
boxes[3].append('scarf')

# Empty Box 2.
boxes[2] = []

# Move the bell from Box 5 to Box 6.
boxes[5].remove('bell')
boxes[6].append('bell')

# Move the butterfly and the boat from Box 4 to Box 1.
boxes[4].remove('butterfly')
boxes[4].remove('boat')
boxes[1].append('butterfly')
boxes[1].append('boat')

# Remove the boat from Box 1.
boxes[1].remove('boat')

# Replace the butterfly with the beach in Box 1.
boxes[1].remove('butterfly')
boxes[1].append('beach')

# Put the fridge into Box 1.
boxes[1].append('fridge')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")