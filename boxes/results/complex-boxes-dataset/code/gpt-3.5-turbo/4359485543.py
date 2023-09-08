# Initial state of boxes
boxes = {
    0: ['comb', 'belt', 'lock'],
    1: ['game', 'pillow', 'violin'],
    2: ['bus'],
    3: ['toothpaste', 'butterfly', 'car', 'dress', 'beach'],
    4: [],
    5: [],
    6: ['console', 'planet', 'fish', 'cat'],
    7: ['button', 'fork'],
    8: ['ocean', 'charger', 'lightning', 'mirror'],
    9: ['gloves', 'pants', 'flower', 'branch', 'submarine'],
    10: ['bracelet', 'drum', 'island', 'lion'],
    11: ['skirt', 'harmonica', 'river'],
    12: ['speaker', 'jacket', 'truck'],
    13: ['glove'],
    14: ['piano', 'polish', 'thread', 'seaweed', 'horse']
}

# Remove the ocean and the charger and the mirror from Box 8.
boxes[8].remove('ocean')
boxes[8].remove('charger')
boxes[8].remove('mirror')

# Move the bus from Box 2 to Box 13.
boxes[2].remove('bus')
boxes[13].append('bus')

# Replace the piano with the controller in Box 14.
boxes[14].remove('piano')
boxes[14].append('controller')

# Remove the jacket from Box 12.
boxes[12].remove('jacket')

# Remove the planet and the console and the cat from Box 6.
boxes[6].remove('planet')
boxes[6].remove('console')
boxes[6].remove('cat')

# Put the jungle and the sun and the river into Box 8.
items_to_put = ['jungle', 'sun', 'river']
for item in items_to_put:
    boxes[8].append(item)

# Remove the thread and the polish from Box 14.
boxes[14].remove('thread')
boxes[14].remove('polish')

# Swap the lock in Box 0 with the glove in Box 13.
boxes[0].remove('lock')
boxes[13].remove('glove')
boxes[0].append('glove')
boxes[13].append('lock')

# Move the speaker and the truck from Box 12 to Box 2.
boxes[12].remove('speaker')
boxes[12].remove('truck')
boxes[2].append('speaker')
boxes[2].append('truck')

# Replace the button with the river in Box 7.
boxes[7].remove('button')
boxes[7].append('river')

# Swap the pillow in Box 1 with the seaweed in Box 14.
boxes[1].remove('pillow')
boxes[14].remove('seaweed')
boxes[1].append('seaweed')
boxes[14].append('pillow')

# Put the gloves and the dolphin into Box 5.
boxes[5].append('gloves')
boxes[5].append('dolphin')

# Put the puzzle and the gloves into Box 14.
boxes[14].append('puzzle')
boxes[14].append('gloves')

# Replace the gloves and the dolphin with the book and the pan in Box 5.
boxes[5].remove('gloves')
boxes[5].remove('dolphin')
boxes[5].append('book')
boxes[5].append('pan')

# Put the keyboard and the towel and the frame into Box 10.
items_to_put = ['keyboard', 'towel', 'frame']
for item in items_to_put:
    boxes[10].append(item)

# Move the seaweed from Box 1 to Box 9.
boxes[1].remove('seaweed')
boxes[9].append('seaweed')

# Replace the pants and the submarine with the soap and the lightning in Box 9.
boxes[9].remove('pants')
boxes[9].remove('submarine')
boxes[9].append('soap')
boxes[9].append('lightning')

# Put the camera and the plate into Box 13.
boxes[13].append('camera')
boxes[13].append('plate')

# Remove the sun and the lightning from Box 8.
boxes[8].remove('sun')
boxes[8].remove('lightning')

# Swap the glove in Box 0 with the pan in Box 5.
boxes[0].remove('glove')
boxes[5].remove('pan')
boxes[0].append('pan')
boxes[5].append('glove')

# Put the forest into Box 5.
boxes[5].append('forest')

# Replace the speaker with the sun in Box 2.
boxes[2].remove('speaker')
boxes[2].append('sun')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")