# Initial state of boxes
boxes = {
    0: [],
    1: ['bracelet', 'necklace', 'horn'],
    2: ['flower', 'elephant'],
    3: ['needle', 'leaf', 'frame'],
    4: ['mixer', 'perfume', 'makeup', 'boat'],
    5: ['piano', 'puzzle', 'train', 'zipper'],
    6: ['thread'],
    7: ['polish', 'microscope', 'dog', 'jacket', 'bird'],
    8: ['spoon', 'clock', 'shark', 'scissors', 'umbrella'],
    9: ['lamp', 'sculpture', 'wallet', 'flute'],
    10: ['meteor', 'glasses', 'wig', 'toothbrush'],
    11: ['coat', 'comet', 'shirt'],
    12: ['camera', 'rocket']
}

# Replace the camera with the tie in Box 12.
boxes[12].remove('camera')
boxes[12].append('tie')

# Replace the meteor and the glasses with the wire and the toothpaste in Box 10.
boxes[10].remove('meteor')
boxes[10].remove('glasses')
boxes[10].append('wire')
boxes[10].append('toothpaste')

# Replace the dog with the bird in Box 7.
boxes[7].remove('dog')
boxes[7].append('bird')

# Remove the necklace from Box 1.
boxes[1].remove('necklace')

# Swap the elephant in Box 2 with the toothbrush in Box 10.
boxes[2].remove('elephant')
boxes[10].remove('toothbrush')
boxes[2].append('toothbrush')
boxes[10].append('elephant')

# Put the bracelet and the lion into Box 1.
boxes[1].append('bracelet')
boxes[1].append('lion')

# Move the zipper and the piano from Box 5 to Box 3.
boxes[5].remove('zipper')
boxes[5].remove('piano')
boxes[3].append('zipper')
boxes[3].append('piano')

# Empty Box 2.
boxes[2] = []

# Swap the bird in Box 7 with the piano in Box 3.
boxes[7].remove('bird')
boxes[3].remove('piano')
boxes[7].append('piano')
boxes[3].append('bird')

# Move the lion and the bracelet and the necklace from Box 1 to Box 12.
items_to_move = ['lion', 'bracelet', 'necklace']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[12].append(item)

# Remove the train from Box 5.
boxes[5].remove('train')

# Remove the polish from Box 7.
boxes[7].remove('polish')

# Move the elephant and the wig and the toothpaste from Box 10 to Box 12.
items_to_move = ['elephant', 'wig', 'toothpaste']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[12].append(item)

# Put the soap into Box 12.
boxes[12].append('soap')

# Empty Box 1.
boxes[1] = []

# Put the butterfly and the tie into Box 4.
boxes[4].append('butterfly')
boxes[4].append('tie')

# Put the rock and the forest and the watch into Box 12.
boxes[12].append('rock')
boxes[12].append('forest')
boxes[12].append('watch')

# Put the rock and the sculpture and the phone into Box 7.
boxes[7].append('rock')
boxes[7].append('sculpture')
boxes[7].append('phone')

# Remove the zipper and the leaf from Box 3.
boxes[3].remove('zipper')
boxes[3].remove('leaf')

# Put the rocket and the watch into Box 10.
boxes[10].append('rocket')
boxes[10].append('watch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")