# Initial state of boxes
boxes = {
    0: [],
    1: ['note', 'star'],
    2: ['shoes', 'cat', 'storm'],
    3: ['motorcycle'],
    4: ['meteor'],
    5: ['bird', 'boot', 'wig', 'horse'],
    6: ['bicycle', 'wire', 'shampoo', 'freezer', 'oven'],
    7: ['skirt'],
    8: ['jacket', 'lightning', 'rain', 'pants'],
    9: ['clock'],
    10: []
}

# Put the battery and the shampoo and the bear into Box 6.
boxes[6].extend(['battery', 'shampoo', 'bear'])

# Swap the clock in Box 9 with the note in Box 1.
boxes[9], boxes[1] = boxes[1], boxes[9]

# Swap the wig in Box 5 with the meteor in Box 4.
boxes[5], boxes[4] = boxes[4], boxes[5]

# Remove the note from Box 9.
boxes[9].remove('note')

# Move the bicycle and the battery and the lock from Box 6 to Box 5.
items_to_move = ['bicycle', 'battery', 'lock']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Remove the clock and the star from Box 1.
boxes[1].remove('clock')
boxes[1].remove('star')

# Remove the skirt from Box 7.
boxes[7].remove('skirt')

# Empty Box 6.
boxes[6] = []

# Put the razor and the submarine and the pan into Box 0.
boxes[0].extend(['razor', 'submarine', 'pan'])

# Swap the bird in Box 5 with the cat in Box 2.
boxes[5], boxes[2] = boxes[2], boxes[5]

# Swap the bicycle in Box 5 with the motorcycle in Box 3.
boxes[5], boxes[3] = boxes[3], boxes[5]

# Move the lock and the motorcycle from Box 5 to Box 7.
items_to_move = ['lock', 'motorcycle']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Put the tiger and the tape into Box 1.
boxes[1].extend(['tiger', 'tape'])

# Move the bicycle from Box 3 to Box 5.
boxes[3].remove('bicycle')
boxes[5].append('bicycle')

# Put the whistle and the button into Box 1.
boxes[1].extend(['whistle', 'button'])

# Move the button and the tiger and the whistle from Box 1 to Box 2.
items_to_move = ['button', 'tiger', 'whistle']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")