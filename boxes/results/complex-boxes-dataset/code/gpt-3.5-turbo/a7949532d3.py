# Initial state of boxes
boxes = {
    0: ['belt', 'chair', 'bear', 'button', 'forest'],
    1: [],
    2: ['island'],
    3: ['coral', 'butterfly', 'basket'],
    4: [],
    5: ['clock', 'shelf', 'note', 'thread'],
    6: ['submarine', 'zipper', 'meteor'],
    7: ['scissors', 'coin'],
    8: ['razor', 'cup'],
    9: ['makeup', 'bracelet'],
    10: ['gloves', 'microwave', 'truck', 'controller', 'comb']
}

# Replace the submarine and the zipper and the meteor with the pot and the dice and the mixer in Box 6.
boxes[6].remove('submarine')
boxes[6].remove('zipper')
boxes[6].remove('meteor')
boxes[6].append('pot')
boxes[6].append('dice')
boxes[6].append('mixer')

# Put the planet into Box 9.
boxes[9].append('planet')

# Remove the shelf and the clock and the thread from Box 5.
boxes[5].remove('shelf')
boxes[5].remove('clock')
boxes[5].remove('thread')

# Put the plane into Box 10.
boxes[10].append('plane')

# Remove the planet and the bracelet from Box 9.
boxes[9].remove('planet')
boxes[9].remove('bracelet')

# Put the butterfly and the tiger into Box 6.
boxes[6].append('butterfly')
boxes[6].append('tiger')

# Move the island from Box 2 to Box 1.
boxes[1].append(boxes[2].pop())

# Remove the cup from Box 8.
boxes[8].remove('cup')

# Replace the truck with the toothbrush in Box 10.
boxes[10].remove('truck')
boxes[10].append('toothbrush')

# Remove the scissors and the coin from Box 7.
boxes[7].remove('scissors')
boxes[7].remove('coin')

# Move the island from Box 1 to Box 10.
boxes[10].append(boxes[1].pop())

# Remove the makeup from Box 9.
boxes[9].remove('makeup')

# Remove the note from Box 5.
boxes[5].remove('note')

# Put the thread and the bear and the tape into Box 7.
boxes[7].append('thread')
boxes[7].append('bear')
boxes[7].append('tape')

# Swap the tape in Box 7 with the butterfly in Box 6.
boxes[7].remove('tape')
boxes[6].remove('butterfly')
boxes[7].append('butterfly')
boxes[6].append('tape')

# Put the toaster and the moon and the charger into Box 0.
boxes[0].append('toaster')
boxes[0].append('moon')
boxes[0].append('charger')

# Remove the button and the toaster and the moon from Box 0.
boxes[0].remove('button')
boxes[0].remove('toaster')
boxes[0].remove('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")