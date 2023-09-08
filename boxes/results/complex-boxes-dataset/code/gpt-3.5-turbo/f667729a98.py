# Initial state of boxes
boxes = {
    0: ['lock', 'button', 'planet', 'charger', 'camera'],
    1: [],
    2: ['magnet', 'desert', 'clock'],
    3: ['candle', 'crown'],
    4: [],
    5: ['usb', 'whistle', 'pants'],
    6: ['tape', 'moon', 'submarine', 'table', 'leaf'],
    7: [],
    8: ['guitar', 'frame', 'fridge', 'flower'],
    9: [],
    10: ['thunder', 'beach'],
    11: ['lipstick', 'pan', 'brush'],
    12: [],
    13: []
}

# Swap the crown in Box 3 with the moon in Box 6.
boxes[3].remove('crown')
boxes[6].remove('moon')
boxes[3].append('moon')
boxes[6].append('crown')

# Replace the candle and the moon with the shoes and the plate in Box 3.
boxes[3].remove('candle')
boxes[3].remove('moon')
boxes[3].append('shoes')
boxes[3].append('plate')

# Replace the plate and the shoes with the beach and the car in Box 3.
boxes[3].remove('plate')
boxes[3].remove('shoes')
boxes[3].append('beach')
boxes[3].append('car')

# Swap the tape in Box 6 with the brush in Box 11.
boxes[6].remove('tape')
boxes[11].remove('brush')
boxes[6].append('brush')
boxes[11].append('tape')

# Replace the thunder with the flute in Box 10.
boxes[10].remove('thunder')
boxes[10].append('flute')

# Swap the button in Box 0 with the flute in Box 10.
boxes[0].remove('button')
boxes[10].remove('flute')
boxes[0].append('flute')
boxes[10].append('button')

# Put the lion and the swimsuit and the grinder into Box 9.
items_to_put = ['lion', 'swimsuit', 'grinder']
for item in items_to_put:
    boxes[9].append(item)

# Remove the lipstick and the tape from Box 11.
boxes[11].remove('lipstick')
boxes[11].remove('tape')

# Put the wig and the island and the pants into Box 4.
items_to_put = ['wig', 'island', 'pants']
for item in items_to_put:
    boxes[4].append(item)

# Empty Box 10.
boxes[10] = []

# Move the desert from Box 2 to Box 4.
boxes[4].append(boxes[2].pop(1))

# Remove the charger from Box 0.
boxes[0].remove('charger')

# Replace the crown with the plane in Box 6.
boxes[6].remove('crown')
boxes[6].append('plane')

# Put the magnet and the card and the tie into Box 5.
items_to_put = ['magnet', 'card', 'tie']
for item in items_to_put:
    boxes[5].append(item)

# Remove the clock from Box 2.
boxes[2].remove('clock')

# Put the lion into Box 0.
boxes[0].append('lion')

# Put the camera and the boat into Box 13.
items_to_put = ['camera', 'boat']
for item in items_to_put:
    boxes[13].append(item)

# Move the plane and the leaf from Box 6 to Box 10.
boxes[10].append(boxes[6].pop(1))
boxes[10].append(boxes[6].pop(2))

# Put the scissors into Box 1.
boxes[1].append('scissors')

# Remove the lion and the grinder from Box 9.
boxes[9].remove('lion')
boxes[9].remove('grinder')

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")