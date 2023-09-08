# Initial state of boxes
boxes = {
    0: ['grinder', 'shirt'],
    1: ['violin'],
    2: [],
    3: ['bear', 'mixer', 'star', 'ring', 'plane'],
    4: ['cloud', 'fridge', 'wallet', 'pillow'],
    5: ['needle']
}

# Swap the shirt in Box 0 with the violin in Box 1.
boxes[0].remove('shirt')
boxes[1].remove('violin')
boxes[0].append('violin')
boxes[1].append('shirt')

# Put the blender into Box 1.
boxes[1].append('blender')

# Swap the mixer in Box 3 with the shirt in Box 1.
boxes[3].remove('mixer')
boxes[1].remove('shirt')
boxes[3].append('shirt')
boxes[1].append('mixer')

# Put the dress and the lipstick into Box 5.
boxes[5].append('dress')
boxes[5].append('lipstick')

# Swap the blender in Box 1 with the grinder in Box 0.
boxes[1].remove('blender')
boxes[0].remove('grinder')
boxes[1].append('grinder')
boxes[0].append('blender')

# Replace the pillow with the sun in Box 4.
boxes[4].remove('pillow')
boxes[4].append('sun')

# Put the wire and the phone into Box 5.
boxes[5].append('wire')
boxes[5].append('phone')

# Move the grinder and the mixer from Box 1 to Box 0.
items_to_move = ['grinder', 'mixer']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Swap the star in Box 3 with the dress in Box 5.
boxes[3].remove('star')
boxes[5].remove('dress')
boxes[3].append('dress')
boxes[5].append('star')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")