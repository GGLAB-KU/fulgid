# Initialize the boxes
boxes = {
    0: ['dress', 'tape', 'tie'],
    1: ['picture'],
    2: ['document', 'drug', 'glass'],
    3: ['meat'],
    4: [],
    5: ['brain', 'pipe'],
    6: ['boat', 'boot'],
}

# Define the move
move = (2, 4, 'drug')  # Move the drug from Box 2 to Box 4

# Execute the move
src, dest, item = move

boxes[src].remove(item)  # Remove the item from the source box
boxes[dest].append(item)  # Add the item to the destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")