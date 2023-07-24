# Initialize the boxes
boxes = {
    0: [],
    1: ['cigarette'],
    2: ['beer', 'tie'],
    3: [],
    4: ['cream', 'egg', 'knife'],
    5: ['bone'],
    6: ['plate'],
}

# Define the move
move = (2, 5, 'tie')  # Move the tie from Box 2 to Box 5

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove the item from the source box
boxes[dest].append(item)  # Add the item to the destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")