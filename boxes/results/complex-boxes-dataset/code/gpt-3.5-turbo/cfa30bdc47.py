# Initial state of boxes
boxes = {
    0: ['lipstick'],
    1: ['laptop', 'hat', 'puzzle', 'microwave', 'dress'],
    2: ['bracelet', 'desert'],
    3: ['sock', 'crown', 'piano'],
    4: ['toothpaste'],
    5: ['leaf', 'river', 'earring'],
    6: ['fridge', 'chair', 'storm', 'watch']
}

# Replace the desert and the bracelet with the grinder and the vase in Box 2.
boxes[2].remove('desert')
boxes[2].remove('bracelet')
boxes[2].append('grinder')
boxes[2].append('vase')

# Move the storm from Box 6 to Box 3.
boxes[6].remove('storm')
boxes[3].append('storm')

# Put the key and the mask into Box 2.
boxes[2].append('key')
boxes[2].append('mask')

# Put the butterfly and the glove and the desert into Box 2.
boxes[2].append('butterfly')
boxes[2].append('glove')
boxes[2].append('desert')

# Replace the earring and the river and the leaf with the jacket and the comb and the octopus in Box 5.
boxes[5].remove('earring')
boxes[5].remove('river')
boxes[5].remove('leaf')
boxes[5].append('jacket')
boxes[5].append('comb')
boxes[5].append('octopus')

# Swap the chair in Box 6 with the toothpaste in Box 4.
boxes[6].remove('chair')
boxes[4].remove('toothpaste')
boxes[6].append('toothpaste')
boxes[4].append('chair')

# Empty Box 2.
boxes[2] = []

# Remove the chair from Box 4.
boxes[4].remove('chair')

# Replace the laptop and the microwave and the dress with the grinder and the thunder and the pen in Box 1.
boxes[1].remove('laptop')
boxes[1].remove('microwave')
boxes[1].remove('dress')
boxes[1].append('grinder')
boxes[1].append('thunder')
boxes[1].append('pen')

# Empty Box 5.
boxes[5] = []

# Move the fridge and the toothpaste and the watch from Box 6 to Box 1.
items_to_move = ['fridge', 'toothpaste', 'watch']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")