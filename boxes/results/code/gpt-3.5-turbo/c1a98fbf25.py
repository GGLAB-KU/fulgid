# Initialize the boxes
boxes = {
    0: ['cream', 'phone'],
    1: [],
    2: ['cross', 'gift', 'plate'],
    3: ['ball', 'document'],
    4: ['bag', 'jacket', 'rose'],
    5: ['ice', 'knife'],
    6: ['egg'],
}

# Define the move
move = (6, 0, 'egg')  # Move the egg from Box 6 to Box 0

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove item from source box
boxes[dest].append(item)  # Add item to destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")