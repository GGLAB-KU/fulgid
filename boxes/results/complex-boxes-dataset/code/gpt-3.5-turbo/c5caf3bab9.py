# Initial state of boxes
boxes = {
    0: ['sculpture', 'blanket'],
    1: ['basket', 'glove', 'glasses', 'car', 'blender'],
    2: ['sandals', 'moon', 'controller'],
    3: ['hat'],
    4: ['mixer'],
    5: ['dolphin', 'shampoo', 'book', 'helmet']
}

# Replace the blanket with the dress in Box 0.
boxes[0].remove('blanket')
boxes[0].append('dress')

# Move the glasses and the blender from Box 1 to Box 3.
items_to_move = ['glasses', 'blender']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Replace the mixer with the horse in Box 4.
boxes[4].remove('mixer')
boxes[4].append('horse')

# Remove the sculpture from Box 0.
boxes[0].remove('sculpture')

# Remove the hat and the blender and the glasses from Box 3.
items_to_remove = ['hat', 'blender', 'glasses']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the car in Box 1 with the horse in Box 4.
boxes[1].remove('car')
boxes[4].remove('horse')
boxes[1].append('horse')
boxes[4].append('car')

# Swap the dress in Box 0 with the dolphin in Box 5.
boxes[0].remove('dress')
boxes[5].remove('dolphin')
boxes[0].append('dolphin')
boxes[5].append('dress')

# Put the toy and the dog into Box 2.
boxes[2].append('toy')
boxes[2].append('dog')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")