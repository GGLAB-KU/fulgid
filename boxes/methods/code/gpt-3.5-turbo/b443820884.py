# Initialize the boxes
boxes = {
    0: ['bone', 'television'],
    1: ['drink', 'fig'],
    2: ['glass'],
    3: ['pot'],
    4: ['key', 'plate', 'shoe'],
    5: ['beer', 'egg'],
    6: [],
}

# Define the move
move = (3, 2, 'pot')  # Move the pot from Box 3 to Box 2

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove the item from the source box
boxes[dest].append(item)  # Add the item to the destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")