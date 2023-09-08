# Initial state of boxes
boxes = {
    0: ['ocean'],
    1: ['cat', 'moon', 'island', 'shirt', 'hat'],
    2: [],
    3: ['dog', 'blender'],
    4: ['brush', 'star', 'bird', 'button'],
    5: ['boat', 'planet', 'jungle', 'battery', 'umbrella'],
    6: ['train', 'toy'],
    7: [],
    8: ['cow', 'cup', 'coral', 'toaster'],
    9: ['frame', 'truck'],
    10: ['mirror', 'violin', 'harmonica', 'pillow', 'towel'],
    11: [],
    12: [],
    13: ['whistle', 'speaker', 'bicycle', 'toothpaste', 'card']
}

# Put the sandals and the toothpaste into Box 8.
boxes[8].extend(['sandals', 'toothpaste'])

# Move the violin and the pillow from Box 10 to Box 1.
items_to_move = ['violin', 'pillow']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[1].append(item)

# Put the grinder and the coral into Box 6.
boxes[6].extend(['grinder', 'coral'])

# Swap the dog in Box 3 with the frame in Box 9.
boxes[3].remove('dog')
boxes[9].remove('frame')
boxes[3].append('frame')
boxes[9].append('dog')

# Move the harmonica and the towel from Box 10 to Box 1.
items_to_move = ['harmonica', 'towel']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[1].append(item)

# Put the paint and the watch and the mixer into Box 4.
boxes[4].extend(['paint', 'watch', 'mixer'])

# Move the towel and the pillow from Box 1 to Box 10.
items_to_move = ['towel', 'pillow']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[10].append(item)

# Replace the jungle with the candle in Box 5.
boxes[5].remove('jungle')
boxes[5].append('candle')

# Replace the ocean with the mask in Box 0.
boxes[0].remove('ocean')
boxes[0].append('mask')

# Move the mirror from Box 10 to Box 2.
boxes[10].remove('mirror')
boxes[2].append('mirror')

# Replace the mirror with the belt in Box 2.
boxes[2].remove('mirror')
boxes[2].append('belt')

# Replace the harmonica and the hat with the zipper and the puzzle in Box 1.
boxes[1].remove('harmonica')
boxes[1].remove('hat')
boxes[1].append('zipper')
boxes[1].append('puzzle')

# Replace the blender and the frame with the perfume and the dog in Box 3.
boxes[3].remove('blender')
boxes[3].remove('frame')
boxes[3].append('perfume')
boxes[3].append('dog')

# Empty Box 4.
boxes[4] = []

# Replace the toy and the train and the coral with the seaweed and the plane and the polish in Box 6.
boxes[6].remove('toy')
boxes[6].remove('train')
boxes[6].remove('coral')
boxes[6].append('seaweed')
boxes[6].append('plane')
boxes[6].append('polish')

# Replace the mask with the meteor in Box 0.
boxes[0].remove('mask')
boxes[0].append('meteor')

# Put the coat and the lock into Box 5.
boxes[5].extend(['coat', 'lock'])

# Replace the toothpaste and the cup with the coat and the comb in Box 8.
boxes[8].remove('toothpaste')
boxes[8].remove('cup')
boxes[8].append('coat')
boxes[8].append('comb')

# Swap the dog in Box 9 with the dog in Box 3.
boxes[9].remove('dog')
boxes[3].remove('dog')
boxes[9].append('dog')
boxes[3].append('dog')

# Remove the meteor from Box 0.
boxes[0].remove('meteor')

# Put the octopus and the note into Box 9.
boxes[9].extend(['octopus', 'note'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")