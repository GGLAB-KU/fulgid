# Initial state of boxes
boxes = {
    0: ['star', 'mirror', 'bell', 'branch', 'microwave'],
    1: ['wire', 'comb', 'train'],
    2: ['bracelet', 'oven', 'beach', 'forest', 'motorcycle'],
    3: [],
    4: ['game', 'elephant', 'battery', 'dress'],
    5: [],
    6: ['rock', 'key', 'starfish', 'cow', 'pen'],
    7: ['river', 'guitar', 'mask', 'coin'],
    8: ['glasses', 'phone'],
    9: ['sandals', 'card', 'keyboard', 'truck'],
    10: ['headphone', 'brush', 'console']
}

# Empty Box 2.
boxes[2] = []

# Remove the mask and the coin from Box 7.
boxes[7].remove('mask')
boxes[7].remove('coin')

# Put the grinder into Box 8.
boxes[8].append('grinder')

# Swap the river in Box 7 with the key in Box 6.
boxes[7].remove('river')
boxes[6].remove('key')
boxes[7].append('key')
boxes[6].append('river')

# Put the boot into Box 9.
boxes[9].append('boot')

# Empty Box 7.
boxes[7] = []

# Move the card and the truck and the sandals from Box 9 to Box 3.
items_to_move = ['card', 'truck', 'sandals']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Remove the glasses from Box 8.
boxes[8].remove('glasses')

# Remove the keyboard from Box 9.
boxes[9].remove('keyboard')

# Swap the river in Box 6 with the mirror in Box 0.
boxes[6].remove('river')
boxes[0].remove('mirror')
boxes[6].append('mirror')
boxes[0].append('river')

# Put the coin into Box 9.
boxes[9].append('coin')

# Replace the brush and the console and the headphone with the usb and the pan and the dolphin in Box 10.
boxes[10].remove('brush')
boxes[10].remove('console')
boxes[10].remove('headphone')
boxes[10].append('usb')
boxes[10].append('pan')
boxes[10].append('dolphin')

# Put the blender and the speaker and the horse into Box 1.
boxes[1].append('blender')
boxes[1].append('speaker')
boxes[1].append('horse')

# Replace the boot and the coin with the star and the game in Box 9.
boxes[9].remove('boot')
boxes[9].remove('coin')
boxes[9].append('star')
boxes[9].append('game')

# Move the game and the elephant and the battery from Box 4 to Box 2.
items_to_move = ['game', 'elephant', 'battery']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Swap the dress in Box 4 with the sandals in Box 3.
boxes[4].remove('dress')
boxes[3].remove('sandals')
boxes[4].append('sandals')
boxes[3].append('dress')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")