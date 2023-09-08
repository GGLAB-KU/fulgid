# Initial state of boxes
boxes = {
    0: ['wire', 'forest', 'paint', 'spoon', 'tie'],
    1: ['cat'],
    2: ['shark', 'pot', 'perfume', 'motorcycle'],
    3: ['ring', 'magnet', 'moon'],
    4: ['sculpture', 'belt', 'lamp'],
    5: ['candle', 'guitar', 'brush'],
    6: ['toy', 'microscope'],
    7: ['toothpaste', 'comet'],
    8: ['shirt', 'beach', 'chair', 'ocean', 'fish'],
    9: ['star', 'whistle', 'sun', 'soap', 'dice'],
    10: ['starfish'],
    11: ['horse', 'snow', 'headphone', 'violin', 'doll'],
    12: ['button', 'sandals', 'pan', 'desert'],
    13: ['clock', 'basket', 'jacket', 'oven', 'speaker']
}

# Swap the toothpaste in Box 7 with the ring in Box 3.
boxes[7].remove('toothpaste')
boxes[3].remove('ring')
boxes[7].append('ring')
boxes[3].append('toothpaste')

# Replace the belt with the makeup in Box 4.
boxes[4].remove('belt')
boxes[4].append('makeup')

# Replace the candle and the brush and the guitar with the cloud and the whistle and the phone in Box 5.
boxes[5].remove('candle')
boxes[5].remove('brush')
boxes[5].remove('guitar')
boxes[5].append('cloud')
boxes[5].append('whistle')
boxes[5].append('phone')

# Remove the ring and the comet from Box 7.
boxes[7].remove('ring')
boxes[7].remove('comet')

# Remove the makeup and the sculpture from Box 4.
boxes[4].remove('makeup')
boxes[4].remove('sculpture')

# Remove the desert and the sandals from Box 12.
boxes[12].remove('desert')
boxes[12].remove('sandals')

# Replace the shark and the perfume with the lipstick and the spoon in Box 2.
boxes[2].remove('shark')
boxes[2].remove('perfume')
boxes[2].append('lipstick')
boxes[2].append('spoon')

# Remove the dice and the sun from Box 9.
boxes[9].remove('dice')
boxes[9].remove('sun')

# Remove the button and the pan from Box 12.
boxes[12].remove('button')
boxes[12].remove('pan')

# Move the horse from Box 11 to Box 13.
boxes[11].remove('horse')
boxes[13].append('horse')

# Replace the starfish with the soap in Box 10.
boxes[10].remove('starfish')
boxes[10].append('soap')

# Move the whistle and the star from Box 9 to Box 4.
boxes[9].remove('whistle')
boxes[9].remove('star')
boxes[4].append('whistle')
boxes[4].append('star')

# Move the soap from Box 10 to Box 9.
boxes[10].remove('soap')
boxes[9].append('soap')

# Move the phone and the cloud and the whistle from Box 5 to Box 10.
boxes[5].remove('phone')
boxes[5].remove('cloud')
boxes[5].remove('whistle')
boxes[10].append('phone')
boxes[10].append('cloud')
boxes[10].append('whistle')

# Swap the doll in Box 11 with the soap in Box 9.
boxes[11].remove('doll')
boxes[9].remove('soap')
boxes[11].append('soap')
boxes[9].append('doll')

# Empty Box 2.
boxes[2] = []

# Swap the fish in Box 8 with the tie in Box 0.
boxes[8].remove('fish')
boxes[0].remove('tie')
boxes[8].append('tie')
boxes[0].append('fish')

# Move the violin from Box 11 to Box 7.
boxes[11].remove('violin')
boxes[7].append('violin')

# Move the violin from Box 7 to Box 0.
boxes[7].remove('violin')
boxes[0].append('violin')

# Put the camera and the starfish into Box 2.
boxes[2].append('camera')
boxes[2].append('starfish')

# Move the forest and the fish and the wire from Box 0 to Box 1.
items_to_move = ['forest', 'fish', 'wire']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")