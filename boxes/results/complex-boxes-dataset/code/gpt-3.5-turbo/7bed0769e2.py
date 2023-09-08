# Initial state of boxes
boxes = {
    0: [],
    1: ['mask', 'river', 'tie'],
    2: ['lipstick', 'shark', 'dolphin', 'fish', 'rocket'],
    3: ['octopus', 'pillow', 'perfume', 'controller', 'bag'],
    4: ['phone', 'horse'],
    5: ['makeup', 'harmonica', 'toothbrush'],
    6: ['whistle', 'wig', 'desert', 'rock', 'chair'],
    7: ['mixer', 'puzzle', 'moon', 'scarf'],
    8: ['crown', 'glasses', 'flute'],
    9: ['zipper'],
    10: ['cloud', 'snow', 'guitar', 'bear'],
    11: ['planet', 'shirt', 'pan', 'fridge'],
    12: ['basket', 'umbrella', 'truck']
}

# Remove the snow and the guitar and the cloud from Box 10.
boxes[10].remove('snow')
boxes[10].remove('guitar')
boxes[10].remove('cloud')

# Move the crown and the flute and the glasses from Box 8 to Box 1.
items_to_move = ['crown', 'flute', 'glasses']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[1].append(item)

# Put the bowl and the desert into Box 3.
boxes[3].append('bowl')
boxes[3].append('desert')

# Empty Box 5.
boxes[5] = []

# Remove the whistle and the wig from Box 6.
boxes[6].remove('whistle')
boxes[6].remove('wig')

# Replace the fish and the rocket with the dress and the guitar in Box 2.
boxes[2].remove('fish')
boxes[2].remove('rocket')
boxes[2].append('dress')
boxes[2].append('guitar')

# Swap the bear in Box 10 with the guitar in Box 2.
boxes[10].remove('bear')
boxes[2].remove('guitar')
boxes[10].append('guitar')
boxes[2].append('bear')

# Move the planet from Box 11 to Box 12.
boxes[11].remove('planet')
boxes[12].append('planet')

# Move the chair from Box 6 to Box 12.
boxes[6].remove('chair')
boxes[12].append('chair')

# Swap the shirt in Box 11 with the phone in Box 4.
boxes[11].remove('shirt')
boxes[4].remove('phone')
boxes[11].append('phone')
boxes[4].append('shirt')

# Move the zipper from Box 9 to Box 5.
boxes[9].remove('zipper')
boxes[5].append('zipper')

# Empty Box 1.
boxes[1] = []

# Put the frame and the vase into Box 5.
boxes[5].append('frame')
boxes[5].append('vase')

# Remove the pillow and the bag from Box 3.
boxes[3].remove('pillow')
boxes[3].remove('bag')

# Put the microwave into Box 8.
boxes[8].append('microwave')

# Move the bear and the dress from Box 2 to Box 8.
boxes[2].remove('bear')
boxes[2].remove('dress')
boxes[8].append('bear')
boxes[8].append('dress')

# Swap the dolphin in Box 2 with the zipper in Box 5.
boxes[2].remove('dolphin')
boxes[5].remove('zipper')
boxes[2].append('zipper')
boxes[5].append('dolphin')

# Swap the rock in Box 6 with the guitar in Box 10.
boxes[6].remove('rock')
boxes[10].remove('guitar')
boxes[6].append('guitar')
boxes[10].append('rock')

# Move the rock from Box 10 to Box 3.
boxes[10].remove('rock')
boxes[3].append('rock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")