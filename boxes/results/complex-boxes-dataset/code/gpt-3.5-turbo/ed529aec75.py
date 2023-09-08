# Initial state of boxes
boxes = {
    0: ['telescope', 'forest', 'planet', 'moon', 'crown'],
    1: ['headphone', 'star', 'card'],
    2: [],
    3: ['tie', 'pillow'],
    4: ['butterfly', 'belt', 'snow', 'coral']
}

# Move the headphone and the star from Box 1 to Box 3.
boxes[1].remove('headphone')
boxes[1].remove('star')
boxes[3].append('headphone')
boxes[3].append('star')

# Remove the butterfly from Box 4.
boxes[4].remove('butterfly')

# Empty Box 4.
boxes[4] = []

# Swap the forest in Box 0 with the pillow in Box 3.
boxes[0].remove('forest')
boxes[3].remove('pillow')
boxes[0].append('pillow')
boxes[3].append('forest')

# Replace the planet and the telescope with the doll and the bag in Box 0.
boxes[0].remove('planet')
boxes[0].remove('telescope')
boxes[0].append('doll')
boxes[0].append('bag')

# Remove the bag from Box 0.
boxes[0].remove('bag')

# Remove the headphone from Box 3.
boxes[3].remove('headphone')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")