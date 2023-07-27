# Initialize the boxes
boxes = {
    0: ['guitar', 'magazine'],
    1: ['fig', 'sheet'],
    2: ['tea'],
    3: ['bell', 'cross', 'watch'],
    4: ['cheese', 'fish', 'phone'],
    5: ['brick'],
    6: ['drink', 'painting', 'ring'],
}

# Define the move
move = (None, 5, 'cash')  # Put the cash into Box 5

# Execute the move
src, dest, item = move

if src is not None:  # If there's a source box, remove item from it
    boxes[src].remove(item)

if dest is not None:  # If there's a destination box, add item to it
    boxes[dest].append(item)

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")