# Initialize the boxes
boxes = {
    0: ['boat', 'medicine'],
    1: [],
    2: ['computer', 'crown', 'tape'],
    3: ['egg', 'string'],
    4: ['branch', 'drug', 'radio'],
    5: ['rock'],
    6: ['beer', 'letter'],
}

# Define the moves
moves = [
    (5, 3, 'rock'),         # Move the rock from Box 5 to Box 3
    (4, 1, 'drug'),         # Move the drug from Box 4 to Box 1
    (6, None, 'letter'),    # Remove the letter from Box 6
    (0, 1, 'medicine'),     # Move the medicine from Box 0 to Box 1
    (4, 0, 'branch'),       # Move the branch from Box 4 to Box 0
    (4, 0, 'radio'),        # Move the radio from Box 4 to Box 0
    (2, 4, 'crown'),        # Move the crown from Box 2 to Box 4
    (1, None, 'drug'),      # Remove the drug from Box 1
    (1, None, 'medicine'),  # Remove the medicine from Box 1
    (4, None, 'crown'),     # Remove the crown from Box 4
    (0, 4, 'radio'),        # Move the radio from Box 0 to Box 4
    (None, 2, 'ticket'),    # Put the ticket into Box 2
    (4, 1, 'radio'),        # Move the radio from Box 4 to Box 1
    (6, None, 'beer')       # Remove the beer from Box 6
]

# Execute the moves
for move in moves:
    src, dest, item = move

    if src is not None:  # If there's a source box, remove item from it
        boxes[src].remove(item)

    if dest is not None:  # If there's a destination box, add item to it
        boxes[dest].append(item)

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")