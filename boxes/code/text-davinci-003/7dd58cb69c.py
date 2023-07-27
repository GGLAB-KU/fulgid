# Initialize the boxes
boxes = {
    0: ['coat', 'medicine'],
    1: ['apple', 'guitar', 'shell'],
    2: ['bag', 'drink', 'tie'],
    3: ['machine', 'paper', 'watch'],
    4: ['camera', 'seed'],
    5: ['clock'],
    6: ['computer', 'note', 'plant'],
}

# Define the move
move = (2, 0, 'tie')  # Move the tie from Box 2 to Box 0

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove the item from the source box
boxes[dest].append(item)  # Add the item to the destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")