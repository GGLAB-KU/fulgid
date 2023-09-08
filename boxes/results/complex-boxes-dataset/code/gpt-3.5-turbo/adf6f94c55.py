# Initial state of boxes
boxes = {
    0: ['ocean', 'chair', 'vase', 'leaf'],
    1: ['grinder'],
    2: ['sculpture', 'elephant', 'jacket', 'blanket', 'shorts'],
    3: ['plate', 'umbrella', 'toothpaste', 'pillow', 'cow'],
    4: [],
    5: ['shelf', 'clock', 'octopus', 'comet'],
    6: [],
    7: [],
    8: ['whistle', 'lightning', 'boat'],
    9: []
}

# Replace the blanket and the shorts with the helmet and the console in Box 2.
boxes[2].remove('blanket')
boxes[2].remove('shorts')
boxes[2].append('helmet')
boxes[2].append('console')

# Move the lightning and the whistle from Box 8 to Box 3.
boxes[8].remove('lightning')
boxes[8].remove('whistle')
boxes[3].append('lightning')
boxes[3].append('whistle')

# Swap the vase in Box 0 with the grinder in Box 1.
boxes[0].remove('vase')
boxes[1].remove('grinder')
boxes[0].append('grinder')
boxes[1].append('vase')

# Swap the comet in Box 5 with the pillow in Box 3.
boxes[5].remove('comet')
boxes[3].remove('pillow')
boxes[5].append('pillow')
boxes[3].append('comet')

# Remove the elephant and the helmet and the sculpture from Box 2.
items_to_remove = ['elephant', 'helmet', 'sculpture']
for item in items_to_remove:
    boxes[2].remove(item)

# Move the umbrella from Box 3 to Box 9.
boxes[3].remove('umbrella')
boxes[9].append('umbrella')

# Remove the console from Box 2.
boxes[2].remove('console')

# Put the book and the comb into Box 9.
boxes[9].append('book')
boxes[9].append('comb')

# Remove the jacket from Box 2.
boxes[2].remove('jacket')

# Remove the plate from Box 3.
boxes[3].remove('plate')

# Put the fish and the drum into Box 9.
boxes[9].append('fish')
boxes[9].append('drum')

# Replace the boat with the freezer in Box 8.
boxes[8].remove('boat')
boxes[8].append('freezer')

# Replace the comet and the cow and the toothpaste with the dog and the headphone and the shoes in Box 3.
boxes[3].remove('comet')
boxes[3].remove('cow')
boxes[3].remove('toothpaste')
boxes[3].append('dog')
boxes[3].append('headphone')
boxes[3].append('shoes')

# Move the comb from Box 9 to Box 2.
boxes[9].remove('comb')
boxes[2].append('comb')

# Move the comb from Box 2 to Box 1.
boxes[2].remove('comb')
boxes[1].append('comb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")