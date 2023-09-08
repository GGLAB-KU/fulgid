# Initial state of boxes
boxes = {
    0: ['motorcycle', 'river'],
    1: ['lamp', 'polish', 'game', 'button', 'submarine'],
    2: ['belt', 'boat', 'island'],
    3: [],
    4: [],
    5: []
}

# Swap the button in Box 1 with the river in Box 0.
boxes[0].remove('river')
boxes[1].remove('button')
boxes[0].append('button')
boxes[1].append('river')

# Put the coin and the lipstick and the boat into Box 5.
items_to_move = ['coin', 'lipstick', 'boat']
for item in items_to_move:
    boxes[5].append(item)

# Remove the motorcycle from Box 0.
boxes[0].remove('motorcycle')

# Replace the lamp with the dice in Box 1.
boxes[1].remove('lamp')
boxes[1].append('dice')

# Replace the boat and the island with the thunder and the soap in Box 2.
boxes[2].remove('boat')
boxes[2].remove('island')
boxes[2].append('thunder')
boxes[2].append('soap')

# Swap the polish in Box 1 with the button in Box 0.
boxes[0].remove('button')
boxes[1].remove('polish')
boxes[0].append('polish')
boxes[1].append('button')

# Move the thunder and the soap from Box 2 to Box 1.
items_to_move = ['thunder', 'soap']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Move the lipstick and the coin and the boat from Box 5 to Box 4.
items_to_move = ['lipstick', 'coin', 'boat']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Swap the lipstick in Box 4 with the polish in Box 0.
boxes[0].remove('polish')
boxes[4].remove('lipstick')
boxes[0].append('lipstick')
boxes[4].append('polish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")