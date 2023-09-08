# Initial state of boxes
boxes = {
    0: ['bag'],
    1: ['frame', 'shoe', 'toaster'],
    2: ['glove', 'candle', 'button', 'coat', 'plane'],
    3: ['butterfly', 'cloud', 'bell', 'ship', 'tie'],
    4: ['star', 'apple'],
    5: ['toothbrush'],
    6: ['shelf'],
    7: [],
    8: ['camera', 'rock', 'coin'],
    9: ['usb'],
    10: ['moon', 'seaweed', 'vase', 'dolphin', 'toy']
}

# Swap the glove in Box 2 with the shelf in Box 6.
boxes[2].remove('glove')
boxes[6].remove('shelf')
boxes[2].append('shelf')
boxes[6].append('glove')

# Swap the shelf in Box 2 with the frame in Box 1.
boxes[2].remove('shelf')
boxes[1].remove('frame')
boxes[2].append('frame')
boxes[1].append('shelf')

# Swap the toy in Box 10 with the toothbrush in Box 5.
boxes[10].remove('toy')
boxes[5].remove('toothbrush')
boxes[10].append('toothbrush')
boxes[5].append('toy')

# Remove the apple from Box 4.
boxes[4].remove('apple')

# Remove the bag from Box 0.
boxes[0].remove('bag')

# Put the plate into Box 0.
boxes[0].append('plate')

# Replace the plate with the book in Box 0.
boxes[0].remove('plate')
boxes[0].append('book')

# Remove the book from Box 0.
boxes[0].remove('book')

# Swap the vase in Box 10 with the rock in Box 8.
boxes[10].remove('vase')
boxes[8].remove('rock')
boxes[10].append('rock')
boxes[8].append('vase')

# Move the usb from Box 9 to Box 3.
boxes[9].remove('usb')
boxes[3].append('usb')

# Move the toy from Box 5 to Box 4.
boxes[5].remove('toy')
boxes[4].append('toy')

# Put the toy and the laptop into Box 3.
boxes[3].append('toy')
boxes[3].append('laptop')

# Move the toy and the star from Box 4 to Box 2.
boxes[4].remove('toy')
boxes[4].remove('star')
boxes[2].append('toy')
boxes[2].append('star')

# Remove the camera and the vase from Box 8.
boxes[8].remove('camera')
boxes[8].remove('vase')

# Replace the candle and the frame and the button with the flute and the fish and the thunder in Box 2.
boxes[2].remove('candle')
boxes[2].remove('frame')
boxes[2].remove('button')
boxes[2].append('flute')
boxes[2].append('fish')
boxes[2].append('thunder')

# Remove the glove from Box 6.
boxes[6].remove('glove')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")