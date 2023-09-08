# Initial state of boxes
boxes = {
    0: [],
    1: ['thread', 'comb', 'freezer', 'grass', 'doll'],
    2: ['jacket'],
    3: ['lipstick', 'ring', 'dog', 'boat'],
    4: ['shoe', 'wallet', 'glove', 'fridge', 'shelf'],
    5: ['helmet'],
    6: ['cat'],
    7: ['elephant', 'car', 'lamp', 'rock'],
    8: ['basket', 'dolphin', 'fork', 'game', 'sun'],
    9: [],
    10: ['bowl', 'star', 'key', 'motorcycle'],
    11: ['skirt', 'frame', 'piano', 'pants', 'flower']
}

# Replace the frame with the submarine in Box 11.
boxes[11].remove('frame')
boxes[11].append('submarine')

# Replace the freezer and the doll with the storm and the basket in Box 1.
boxes[1].remove('freezer')
boxes[1].remove('doll')
boxes[1].append('storm')
boxes[1].append('basket')

# Remove the grass and the comb and the basket from Box 1.
items_to_remove = ['grass', 'comb', 'basket']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the star and the motorcycle from Box 10.
boxes[10].remove('star')
boxes[10].remove('motorcycle')

# Move the key from Box 10 to Box 3.
boxes[10].remove('key')
boxes[3].append('key')

# Swap the helmet in Box 5 with the jacket in Box 2.
boxes[5].remove('helmet')
boxes[2].remove('jacket')
boxes[5].append('jacket')
boxes[2].append('helmet')

# Put the basket and the thunder and the tape into Box 1.
boxes[1].append('basket')
boxes[1].append('thunder')
boxes[1].append('tape')

# Move the lipstick and the ring and the key from Box 3 to Box 1.
items_to_move = ['lipstick', 'ring', 'key']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Put the camera and the clock into Box 5.
boxes[5].append('camera')
boxes[5].append('clock')

# Move the tape and the thunder and the storm from Box 1 to Box 4.
items_to_move = ['tape', 'thunder', 'storm']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Replace the bowl with the key in Box 10.
boxes[10].remove('bowl')
boxes[10].append('key')

# Replace the jacket with the swimsuit in Box 5.
boxes[5].remove('jacket')
boxes[5].append('swimsuit')

# Swap the glove in Box 4 with the basket in Box 8.
boxes[4].remove('glove')
boxes[8].remove('basket')
boxes[4].append('basket')
boxes[8].append('glove')

# Put the star and the clock into Box 1.
boxes[1].append('star')
boxes[1].append('clock')

# Put the rain and the soap into Box 3.
boxes[3].append('rain')
boxes[3].append('soap')

# Move the key from Box 10 to Box 9.
boxes[10].remove('key')
boxes[9].append('key')

# Put the bird and the microwave into Box 2.
boxes[2].append('bird')
boxes[2].append('microwave')

# Swap the game in Box 8 with the rock in Box 7.
boxes[8].remove('game')
boxes[7].remove('rock')
boxes[8].append('rock')
boxes[7].append('game')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")