# Initial state of boxes
boxes = {
    0: [],
    1: ['flower', 'boat'],
    2: [],
    3: ['fork', 'microwave'],
    4: [],
    5: ['grass', 'lamp'],
    6: ['scarf', 'dolphin', 'mirror', 'river', 'coral'],
    7: ['swimsuit', 'apple', 'truck', 'toothbrush', 'oven'],
    8: ['headphone', 'ship', 'octopus', 'scissors', 'belt'],
    9: ['bell'],
    10: ['zipper', 'jungle'],
    11: ['card', 'cloud', 'dress', 'elephant'],
    12: ['fridge', 'dog', 'mountain', 'train', 'pan'],
    13: ['cup', 'razor', 'lipstick'],
    14: ['pillow', 'bag', 'doll', 'phone', 'plane']
}

# Move the zipper and the jungle from Box 10 to Box 7.
boxes[10].remove('zipper')
boxes[10].remove('jungle')
boxes[7].append('zipper')
boxes[7].append('jungle')

# Swap the scissors in Box 8 with the elephant in Box 11.
boxes[8].remove('scissors')
boxes[11].remove('elephant')
boxes[8].append('elephant')
boxes[11].append('scissors')

# Put the console and the glove and the comb into Box 13.
items_to_move = ['console', 'glove', 'comb']
for item in items_to_move:
    boxes[13].append(item)

# Move the bell from Box 9 to Box 13.
boxes[9].remove('bell')
boxes[13].append('bell')

# Remove the fork and the microwave from Box 3.
boxes[3].remove('fork')
boxes[3].remove('microwave')

# Move the train and the mountain and the pan from Box 12 to Box 1.
items_to_move = ['train', 'mountain', 'pan']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[1].append(item)

# Remove the fridge and the dog from Box 12.
boxes[12].remove('fridge')
boxes[12].remove('dog')

# Empty Box 8.
boxes[8] = []

# Replace the mountain and the pan with the dog and the bracelet in Box 1.
boxes[1].remove('mountain')
boxes[1].remove('pan')
boxes[1].append('dog')
boxes[1].append('bracelet')

# Put the violin and the usb into Box 0.
items_to_move = ['violin', 'usb']
for item in items_to_move:
    boxes[0].append(item)

# Put the button and the lightning and the glasses into Box 0.
items_to_move = ['button', 'lightning', 'glasses']
for item in items_to_move:
    boxes[0].append(item)

# Replace the cloud and the scissors with the basket and the island in Box 11.
boxes[11].remove('cloud')
boxes[11].remove('scissors')
boxes[11].append('basket')
boxes[11].append('island')

# Remove the card from Box 11.
boxes[11].remove('card')

# Replace the swimsuit with the coat in Box 7.
boxes[7].remove('swimsuit')
boxes[7].append('coat')

# Swap the razor in Box 13 with the violin in Box 0.
boxes[13].remove('razor')
boxes[0].remove('violin')
boxes[13].append('violin')
boxes[0].append('razor')

# Empty Box 0.
boxes[0] = []

# Empty Box 6.
boxes[6] = []

# Move the pillow and the bag and the phone from Box 14 to Box 5.
items_to_move = ['pillow', 'bag', 'phone']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[5].append(item)

# Put the piano and the sun and the candle into Box 6.
items_to_move = ['piano', 'sun', 'candle']
for item in items_to_move:
    boxes[6].append(item)

# Remove the bell and the violin from Box 13.
boxes[13].remove('bell')
boxes[13].remove('violin')

# Swap the lipstick in Box 13 with the lamp in Box 5.
boxes[13].remove('lipstick')
boxes[5].remove('lamp')
boxes[13].append('lamp')
boxes[5].append('lipstick')

# Remove the candle and the sun from Box 6.
boxes[6].remove('candle')
boxes[6].remove('sun')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")