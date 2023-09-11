# Initial state of boxes
boxes = {
    0: ['ocean', 'spoon', 'rock', 'pot'],
    1: ['ship', 'belt', 'skirt', 'boat', 'soap'],
    2: [],
    3: ['dolphin', 'watch', 'button'],
    4: [],
    5: ['thunder', 'shampoo', 'rain', 'wire', 'crown'],
    6: ['moon', 'card', 'tape'],
    7: [],
    8: ['horse', 'coral', 'cloud', 'laptop'],
    9: ['cup', 'leaf', 'basket', 'camera'],
    10: ['charger', 'piano']
}

# Swap the cloud in Box 8 with the rock in Box 0.
boxes[0].remove('rock')
boxes[8].remove('cloud')
boxes[0].append('cloud')
boxes[8].append('rock')

# Swap the tape in Box 6 with the piano in Box 10.
boxes[6].remove('tape')
boxes[10].remove('piano')
boxes[6].append('piano')
boxes[10].append('tape')

# Put the clock and the puzzle into Box 7.
boxes[7].append('clock')
boxes[7].append('puzzle')

# Move the clock from Box 7 to Box 10.
boxes[7].remove('clock')
boxes[10].append('clock')

# Swap the spoon in Box 0 with the puzzle in Box 7.
boxes[0].remove('spoon')
boxes[7].remove('puzzle')
boxes[0].append('puzzle')
boxes[7].append('spoon')

# Move the thunder from Box 5 to Box 7.
boxes[5].remove('thunder')
boxes[7].append('thunder')

# Swap the card in Box 6 with the spoon in Box 7.
boxes[6].remove('card')
boxes[7].remove('spoon')
boxes[6].append('spoon')
boxes[7].append('card')

# Move the horse from Box 8 to Box 2.
boxes[8].remove('horse')
boxes[2].append('horse')

# Swap the card in Box 7 with the horse in Box 2.
boxes[7].remove('card')
boxes[2].remove('horse')
boxes[7].append('horse')
boxes[2].append('card')

# Remove the spoon and the piano from Box 6.
boxes[6].remove('spoon')
boxes[6].remove('piano')

# Move the cup and the camera and the basket from Box 9 to Box 1.
items_to_move = ['cup', 'camera', 'basket']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Put the bag and the wire and the phone into Box 6.
boxes[6].append('bag')
boxes[6].append('wire')
boxes[6].append('phone')

# Replace the ocean and the pot and the puzzle with the microwave and the forest and the mirror in Box 0.
boxes[0].remove('ocean')
boxes[0].remove('pot')
boxes[0].remove('puzzle')
boxes[0].append('microwave')
boxes[0].append('forest')
boxes[0].append('mirror')

# Replace the dolphin and the watch with the cow and the bicycle in Box 3.
boxes[3].remove('dolphin')
boxes[3].remove('watch')
boxes[3].append('cow')
boxes[3].append('bicycle')

# Replace the soap and the camera and the boat with the glasses and the thunder and the apple in Box 1.
boxes[1].remove('soap')
boxes[1].remove('camera')
boxes[1].remove('boat')
boxes[1].append('glasses')
boxes[1].append('thunder')
boxes[1].append('apple')

# Move the charger and the tape from Box 10 to Box 7.
boxes[10].remove('charger')
boxes[10].remove('tape')
boxes[7].append('charger')
boxes[7].append('tape')

# Empty Box 5.
boxes[5] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")