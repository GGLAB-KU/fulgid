# Initial state of boxes
boxes = {
    0: ['camera', 'horn', 'tiger', 'controller', 'lamp'],
    1: ['card', 'bell', 'hat', 'cup'],
    2: ['harmonica', 'perfume', 'phone', 'sandals'],
    3: ['sock', 'wig', 'pillow', 'polish'],
    4: [],
    5: ['microwave', 'basket', 'motorcycle', 'headphone']
}

# Put the ship into Box 4.
boxes[4].append('ship')

# Move the hat from Box 1 to Box 2.
boxes[1].remove('hat')
boxes[2].append('hat')

# Replace the harmonica and the sandals and the hat with the leaf and the soap and the freezer in Box 2.
boxes[2].remove('harmonica')
boxes[2].remove('sandals')
boxes[2].remove('hat')
boxes[2].append('leaf')
boxes[2].append('soap')
boxes[2].append('freezer')

# Swap the controller in Box 0 with the ship in Box 4.
boxes[0].remove('controller')
boxes[4].remove('ship')
boxes[0].append('ship')
boxes[4].append('controller')

# Swap the controller in Box 4 with the horn in Box 0.
boxes[4].remove('controller')
boxes[0].remove('horn')
boxes[4].append('horn')
boxes[0].append('controller')

# Replace the basket and the headphone with the frame and the umbrella in Box 5.
boxes[5].remove('basket')
boxes[5].remove('headphone')
boxes[5].append('frame')
boxes[5].append('umbrella')

# Replace the motorcycle with the card in Box 5.
boxes[5].remove('motorcycle')
boxes[5].append('card')

# Swap the microwave in Box 5 with the lamp in Box 0.
boxes[5].remove('microwave')
boxes[0].remove('lamp')
boxes[5].append('lamp')
boxes[0].append('microwave')

# Remove the freezer and the leaf and the soap from Box 2.
boxes[2].remove('freezer')
boxes[2].remove('leaf')
boxes[2].remove('soap')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")