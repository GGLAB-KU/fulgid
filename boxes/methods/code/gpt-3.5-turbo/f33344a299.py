# Initialize the boxes
boxes = {
    0: ['gift'],
    1: ['ball', 'bone', 'sheet'],
    2: ['game', 'map', 'tissue'],
    3: [],
    4: ['document'],
    5: ['key'],
    6: ['bomb', 'machine', 'picture'],
}

# Define the move
move = (5, 0, 'key')  # Move the key from Box 5 to Box 0

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove the item from the source box
boxes[dest].append(item)  # Add the item to the destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")