# Initial state of boxes
boxes = {
    0: ['headphone', 'necklace', 'flute', 'wire', 'towel'],
    1: ['pillow', 'lock'],
    2: ['violin'],
    3: ['submarine'],
    4: ['book', 'glasses', 'button', 'tree'],
    5: [],
    6: [],
    7: ['jacket', 'dolphin', 'bicycle'],
    8: ['cat', 'telescope', 'lamp', 'bag', 'apple'],
    9: ['thread', 'dress'],
    10: ['charger'],
    11: ['pen', 'skirt', 'toaster', 'forest', 'branch']
}

# Put the makeup and the coat and the sock into Box 11.
items_to_put = ['makeup', 'coat', 'sock']
for item in items_to_put:
    boxes[11].append(item)

# Swap the bag in Box 8 with the violin in Box 2.
boxes[8].remove('bag')
boxes[2].remove('violin')
boxes[8].append('violin')
boxes[2].append('bag')

# Remove the glasses and the tree and the button from Box 4.
items_to_remove = ['glasses', 'tree', 'button']
for item in items_to_remove:
    boxes[4].remove(item)

# Replace the toaster with the apple in Box 11.
boxes[11].remove('toaster')
boxes[11].append('apple')

# Put the dog and the earring and the tree into Box 3.
items_to_put = ['dog', 'earring', 'tree']
for item in items_to_put:
    boxes[3].append(item)

# Replace the sock and the branch with the comb and the zipper in Box 11.
boxes[11].remove('sock')
boxes[11].remove('branch')
boxes[11].append('comb')
boxes[11].append('zipper')

# Swap the towel in Box 0 with the apple in Box 8.
boxes[0].remove('towel')
boxes[8].remove('apple')
boxes[0].append('apple')
boxes[8].append('towel')

# Replace the flute and the necklace and the headphone with the umbrella and the candle and the oven in Box 0.
boxes[0].remove('flute')
boxes[0].remove('necklace')
boxes[0].remove('headphone')
boxes[0].append('umbrella')
boxes[0].append('candle')
boxes[0].append('oven')

# Put the key into Box 9.
boxes[9].append('key')

# Swap the jacket in Box 7 with the earring in Box 3.
boxes[7].remove('jacket')
boxes[3].remove('earring')
boxes[7].append('earring')
boxes[3].append('jacket')

# Swap the submarine in Box 3 with the pillow in Box 1.
boxes[3].remove('submarine')
boxes[1].remove('pillow')
boxes[3].append('pillow')
boxes[1].append('submarine')

# Replace the bicycle and the earring and the dolphin with the island and the rock and the mask in Box 7.
boxes[7].remove('bicycle')
boxes[7].remove('earring')
boxes[7].remove('dolphin')
boxes[7].append('island')
boxes[7].append('rock')
boxes[7].append('mask')

# Put the drum into Box 3.
boxes[3].append('drum')

# Swap the submarine in Box 1 with the pillow in Box 3.
boxes[1].remove('submarine')
boxes[3].remove('pillow')
boxes[1].append('pillow')
boxes[3].append('submarine')

# Replace the bag with the earring in Box 2.
boxes[2].remove('bag')
boxes[2].append('earring')

# Remove the wire from Box 0.
boxes[0].remove('wire')

# Swap the apple in Box 11 with the key in Box 9.
boxes[11].remove('apple')
boxes[9].remove('key')
boxes[11].append('key')
boxes[9].append('apple')

# Replace the charger with the bag in Box 10.
boxes[10].remove('charger')
boxes[10].append('bag')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")