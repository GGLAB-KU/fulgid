box = {
    0: ['zipper'],
    1: ['planet', 'cup', 'piano', 'fish'],
    2: ['toaster', 'belt'],
    3: ['perfume', 'freezer', 'horn', 'toy'],
    4: ['earring'],
    5: [],
    6: ['wire', 'shorts', 'pillow', 'elephant'],
    7: ['lightning', 'shirt', 'shelf', 'jacket', 'makeup'],
    8: ['scissors', 'bracelet', 'candle'],
    9: ['whistle', 'grass', 'starfish', 'dress', 'glove'],
    10: [],
    11: ['console', 'speaker', 'shoes'],
    12: ['flower']
}

# Swap the flower in Box 12 with the jacket in Box 7
box[12], box[7] = box[7], box[12]

# Move the jacket from Box 12 to Box 5
box[5].append(box[12].pop())

# Move the scissors from Box 8 to Box 3
box[3].append(box[8].pop())

# Move the zipper from Box 0 to Box 6
box[6].append(box[0].pop())

# Remove the toaster from Box 2
box[2].remove('toaster')

# Swap the elephant in Box 6 with the earring in Box 4
box[6], box[4] = box[4], box[6]

# Swap the shoes in Box 11 with the jacket in Box 5
box[11], box[5] = box[5], box[11]

# Move the fish from Box 1 to Box 6
box[6].extend(box[1])
box[1].clear()

# Replace the planet and the cup and the piano with the shark and the mask and the ocean in Box 1
box[1] = ['shark', 'mask', 'ocean']

# Replace the lightning and the flower and the shirt with the hat and the bag and the violin in Box 7
box[7] = ['hat', 'bag', 'violin']

# Swap the grass in Box 9 with the bracelet in Box 8
box[9], box[8] = box[8], box[9]

# Put the basket into Box 5
box[5].append('basket')

# Put the dice into Box 3
box[3].append('dice')

# Remove the starfish and the dress and the glove from Box 9
box[9].remove('starfish')
box[9].remove('dress')
box[9].remove('glove')

# Move the mask and the ocean from Box 1 to Box 2
box[2].extend(box[1])
box[1].clear()

# Swap the makeup in Box 7 with the whistle in Box 9
box[7], box[9] = box[9], box[7]

# Put the shirt and the clock into Box 9
box[9].extend(['shirt', 'clock'])

# Move the speaker and the jacket from Box 11 to Box 5
box[5].extend(box[11])
box[11].clear()

# Replace the clock with the earring in Box 9
box[9].remove('clock')
box[9].append('earring')

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {box[i]}")