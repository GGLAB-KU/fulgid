# Initialize the boxes
boxes = {
    0: [],
    1: ['bell', 'bill', 'brain'],
    2: ['camera'],
    3: ['crown', 'pipe'],
    4: ['knife', 'phone', 'plant'],
    5: ['glass', 'key', 'television'],
    6: ['cross', 'flower', 'jacket'],
}

# Define the move
move = (None, 2, 'guitar')  # Put the guitar into Box 2

# Execute the move
src, dest, item = move

if src is not None:  # If there's a source box, remove item from it
    boxes[src].remove(item)

if dest is not None:  # If there's a destination box, add item to it
    boxes[dest].append(item)

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")