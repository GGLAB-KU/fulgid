# Initialize the boxes
boxes = {
    0: [],
    1: ['plate', 'radio'],
    2: ['fish'],
    3: ['tissue'],
    4: [],
    5: ['boat', 'ring'],
    6: ['bill', 'plant', 'shell'],
}

# Define the move
move = (2, 4, 'fish')  # Move the fish from Box 2 to Box 4

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove the fish from source box
boxes[dest].append(item)  # Add the fish to destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")