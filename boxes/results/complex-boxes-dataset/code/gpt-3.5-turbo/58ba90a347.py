# Initial state of boxes
boxes = {
    0: ['console', 'thread', 'tree'],
    1: [],
    2: [],
    3: [],
    4: ['sock'],
    5: ['razor', 'drum', 'sculpture', 'earring'],
    6: ['polish', 'doll', 'card', 'bag'],
    7: ['sandals', 'swimsuit', 'blanket', 'boot']
}

# Remove the sock from Box 4.
boxes[4].remove('sock')

# Swap the thread in Box 0 with the boot in Box 7.
boxes[0].remove('thread')
boxes[7].remove('boot')
boxes[0].append('boot')
boxes[7].append('thread')

# Replace the earring and the sculpture and the razor with the tie and the forest and the speaker in Box 5.
boxes[5].remove('earring')
boxes[5].remove('sculpture')
boxes[5].remove('razor')
boxes[5].append('tie')
boxes[5].append('forest')
boxes[5].append('speaker')

# Replace the swimsuit with the controller in Box 7.
boxes[7].remove('swimsuit')
boxes[7].append('controller')

# Replace the speaker and the tie with the car and the gloves in Box 5.
boxes[5].remove('speaker')
boxes[5].remove('tie')
boxes[5].append('car')
boxes[5].append('gloves')

# Put the dress and the razor and the brush into Box 6.
items_to_move = ['dress', 'razor', 'brush']
for item in items_to_move:
    boxes[6].append(item)

# Swap the thread in Box 7 with the console in Box 0.
boxes[7].remove('thread')
boxes[0].remove('console')
boxes[7].append('console')
boxes[0].append('thread')

# Put the cow and the crown and the seaweed into Box 0.
items_to_move = ['cow', 'crown', 'seaweed']
for item in items_to_move:
    boxes[0].append(item)

# Swap the cow in Box 0 with the brush in Box 6.
boxes[0].remove('cow')
boxes[6].remove('brush')
boxes[0].append('brush')
boxes[6].append('cow')

# Move the dress from Box 6 to Box 5.
boxes[6].remove('dress')
boxes[5].append('dress')

# Move the controller from Box 7 to Box 4.
boxes[7].remove('controller')
boxes[4].append('controller')

# Remove the razor from Box 6.
boxes[6].remove('razor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")