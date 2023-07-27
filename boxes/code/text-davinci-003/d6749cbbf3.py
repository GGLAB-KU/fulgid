# Initialize the boxes
boxes = {
    0: ['bottle', 'picture'],
    1: ['bowl', 'rose'],
    2: ['letter', 'shirt', 'television'],
    3: ['brain', 'branch', 'sheet'],
    4: ['block', 'cigarette', 'drink'],
    5: [],
    6: ['engine'],
}

# Define the move
move = (None, 0, 'book')  # Put the book into Box 0

# Execute the move
src, dest, item = move

if src is not None:  # If there's a source box, remove item from it
    boxes[src].remove(item)

if dest is not None:  # If there's a destination box, add item to it
    boxes[dest].append(item)

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")