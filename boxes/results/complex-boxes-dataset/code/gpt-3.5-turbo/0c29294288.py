# Initial state of boxes
boxes = {
    0: ['camera', 'bracelet', 'ring', 'toaster', 'pot'],
    1: ['keyboard', 'elephant', 'laptop', 'phone', 'toy'],
    2: ['scarf', 'piano'],
    3: ['earring', 'wig', 'frame'],
    4: ['bag', 'shoe', 'makeup', 'shirt'],
    5: ['cloud', 'mask', 'train', 'candle', 'bowl'],
    6: ['sock', 'necklace', 'doll']
}

# Replace the mask with the umbrella in Box 5.
boxes[5].remove('mask')
boxes[5].append('umbrella')

# Replace the piano with the flute in Box 2.
boxes[2].remove('piano')
boxes[2].append('flute')

# Put the butterfly and the truck into Box 6.
boxes[6].append('butterfly')
boxes[6].append('truck')

# Swap the candle in Box 5 with the frame in Box 3.
boxes[5].remove('candle')
boxes[3].remove('frame')
boxes[5].append('frame')
boxes[3].append('candle')

# Replace the butterfly and the truck with the lipstick and the forest in Box 6.
boxes[6].remove('butterfly')
boxes[6].remove('truck')
boxes[6].append('lipstick')
boxes[6].append('forest')

# Replace the shirt and the bag and the makeup with the star and the dress and the bowl in Box 4.
boxes[4].remove('shirt')
boxes[4].remove('bag')
boxes[4].remove('makeup')
boxes[4].append('star')
boxes[4].append('dress')
boxes[4].append('bowl')

# Move the toaster from Box 0 to Box 4.
boxes[0].remove('toaster')
boxes[4].append('toaster')

# Put the sock and the butterfly and the pan into Box 3.
boxes[3].append('sock')
boxes[3].append('butterfly')
boxes[3].append('pan')

# Put the boat into Box 2.
boxes[2].append('boat')

# Put the basket and the butterfly into Box 4.
boxes[4].append('basket')
boxes[4].append('butterfly')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")