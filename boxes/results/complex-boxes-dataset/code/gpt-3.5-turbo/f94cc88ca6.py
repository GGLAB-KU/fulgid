# Initial state of boxes
boxes = {
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

# Swap the flower in Box 12 with the jacket in Box 7.
boxes[12].remove('flower')
boxes[7].remove('jacket')
boxes[12].append('jacket')
boxes[7].append('flower')

# Move the jacket from Box 12 to Box 5.
boxes[12].remove('jacket')
boxes[5].append('jacket')

# Move the scissors from Box 8 to Box 3.
boxes[8].remove('scissors')
boxes[3].append('scissors')

# Move the zipper from Box 0 to Box 6.
boxes[0].remove('zipper')
boxes[6].append('zipper')

# Remove the toaster from Box 2.
boxes[2].remove('toaster')

# Swap the elephant in Box 6 with the earring in Box 4.
boxes[6].remove('elephant')
boxes[4].remove('earring')
boxes[6].append('earring')
boxes[4].append('elephant')

# Swap the shoes in Box 11 with the jacket in Box 5.
boxes[11].remove('shoes')
boxes[5].remove('jacket')
boxes[11].append('jacket')
boxes[5].append('shoes')

# Move the fish from Box 1 to Box 6.
boxes[1].remove('fish')
boxes[6].append('fish')

# Replace the planet and the cup and the piano with the shark and the mask and the ocean in Box 1.
boxes[1].remove('planet')
boxes[1].remove('cup')
boxes[1].remove('piano')
boxes[1].append('shark')
boxes[1].append('mask')
boxes[1].append('ocean')

# Replace the lightning and the flower and the shirt with the hat and the bag and the violin in Box 7.
boxes[7].remove('lightning')
boxes[7].remove('flower')
boxes[7].remove('shirt')
boxes[7].append('hat')
boxes[7].append('bag')
boxes[7].append('violin')

# Swap the grass in Box 9 with the bracelet in Box 8.
boxes[9].remove('grass')
boxes[8].remove('bracelet')
boxes[9].append('bracelet')
boxes[8].append('grass')

# Put the basket into Box 5.
boxes[5].append('basket')

# Put the dice into Box 3.
boxes[3].append('dice')

# Remove the starfish and the dress and the glove from Box 9.
items_to_remove = ['starfish', 'dress', 'glove']
for item in items_to_remove:
    boxes[9].remove(item)

# Move the mask and the ocean from Box 1 to Box 2.
boxes[1].remove('mask')
boxes[1].remove('ocean')
boxes[2].append('mask')
boxes[2].append('ocean')

# Swap the makeup in Box 7 with the whistle in Box 9.
boxes[7].remove('makeup')
boxes[9].remove('whistle')
boxes[7].append('whistle')
boxes[9].append('makeup')

# Put the shirt and the clock into Box 9.
boxes[7].remove('shirt')
boxes[9].append('shirt')
boxes[9].append('clock')

# Move the speaker and the jacket from Box 11 to Box 5.
boxes[11].remove('speaker')
boxes[11].remove('jacket')
boxes[5].append('speaker')
boxes[5].append('jacket')

# Replace the clock with the earring in Box 9.
boxes[9].remove('clock')
boxes[9].append('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")