# Initial state of boxes
boxes = {
    0: ['earring', 'dice'],
    1: ['candle', 'desert', 'rocket'],
    2: [],
    3: [],
    4: ['freezer', 'butterfly', 'starfish', 'toothbrush', 'clock'],
    5: ['microscope', 'bowl', 'razor', 'paint', 'fridge'],
    6: ['horn', 'rain', 'pants', 'comb', 'forest'],
    7: [],
    8: ['swimsuit', 'wig', 'shirt'],
    9: ['laptop', 'ship', 'shoes'],
    10: ['magnet', 'cow'],
    11: ['doll', 'makeup'],
    12: ['glasses', 'game'],
    13: ['flower', 'polish', 'brush']
}

# Swap the cow in Box 10 with the wig in Box 8.
boxes[10].remove('cow')
boxes[8].remove('wig')
boxes[10].append('wig')
boxes[8].append('cow')

# Move the desert and the rocket and the candle from Box 1 to Box 12.
items_to_move = ['desert', 'rocket', 'candle']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[12].append(item)

# Remove the earring from Box 0.
boxes[0].remove('earring')

# Move the makeup from Box 11 to Box 6.
boxes[11].remove('makeup')
boxes[6].append('makeup')

# Swap the flower in Box 13 with the ship in Box 9.
boxes[13].remove('flower')
boxes[9].remove('ship')
boxes[13].append('ship')
boxes[9].append('flower')

# Move the doll from Box 11 to Box 5.
boxes[11].remove('doll')
boxes[5].append('doll')

# Put the shoe and the necklace and the glasses into Box 4.
items_to_move = ['shoe', 'necklace', 'glasses']
for item in items_to_move:
    boxes[4].append(item)

# Move the dice from Box 0 to Box 1.
boxes[0].remove('dice')
boxes[1].append('dice')

# Remove the swimsuit from Box 8.
boxes[8].remove('swimsuit')

# Move the necklace from Box 4 to Box 10.
boxes[4].remove('necklace')
boxes[10].append('necklace')

# Move the clock and the starfish and the freezer from Box 4 to Box 9.
items_to_move = ['clock', 'starfish', 'freezer']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Swap the bowl in Box 5 with the toothbrush in Box 4.
boxes[5].remove('bowl')
boxes[4].remove('toothbrush')
boxes[5].append('toothbrush')
boxes[4].append('bowl')

# Put the rain and the clock and the horse into Box 0.
items_to_move = ['rain', 'clock', 'horse']
for item in items_to_move:
    boxes[0].append(item)

# Remove the necklace from Box 10.
boxes[10].remove('necklace')

# Put the game and the card into Box 1.
items_to_move = ['game', 'card']
for item in items_to_move:
    boxes[1].append(item)

# Swap the dice in Box 1 with the cow in Box 8.
boxes[1].remove('dice')
boxes[8].remove('cow')
boxes[1].append('cow')
boxes[8].append('dice')

# Replace the paint with the fish in Box 5.
boxes[5].remove('paint')
boxes[5].append('fish')

# Remove the pants from Box 6.
boxes[6].remove('pants')

# Remove the game from Box 1.
boxes[1].remove('game')

# Replace the rain and the makeup and the comb with the coat and the elephant and the mask in Box 6.
boxes[6].remove('rain')
boxes[6].remove('makeup')
boxes[6].remove('comb')
boxes[6].append('coat')
boxes[6].append('elephant')
boxes[6].append('mask')

# Remove the microscope and the fish and the razor from Box 5.
items_to_remove = ['microscope', 'fish', 'razor']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")