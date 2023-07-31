# Initialize the boxes
boxes = {
    0: ['coat'],
    1: ['card', 'crown', 'newspaper'],
    2: ['shoe'],
    3: ['brain', 'chemical', 'cream'],
    4: ['wheel'],
    5: ['fan'],
    6: ['picture', 'ticket'],
}

# Define the moves
moves = [
    (0, 4, 'coat'),         # Move the coat from Box 0 to Box 4
    (3, 2, 'chemical'),     # Move the chemical from Box 3 to Box 2
    (3, 2, 'cream'),        # Move the cream from Box 3 to Box 2
    (5, 3, 'fan'),          # Move the fan from Box 5 to Box 3
]

# Execute the moves
for move in moves:
    src, dest, item = move

    boxes[src].remove(item)  # Remove item from source box
    boxes[dest].append(item)  # Add item to destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")