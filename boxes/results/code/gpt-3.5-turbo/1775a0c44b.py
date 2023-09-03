# Initialize the boxes
boxes = {
    0: ['bell'],
    1: ['bread', 'drink', 'engine'],
    2: ['bone'],
    3: ['cigarette', 'ring'],
    4: ['cake', 'newspaper', 'phone'],
    5: ['bowl', 'crown'],
    6: ['plant'],
}

# Define the move
move = (5, 3, 'bowl')  # Move the bowl from Box 5 to Box 3

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove item from source box
boxes[dest].append(item)  # Add item to destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")