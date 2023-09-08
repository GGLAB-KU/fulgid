# Initial state of boxes
boxes = {
    0: ['bowl', 'doll'],
    1: ['scarf', 'horn', 'desert', 'beach'],
    2: ['console', 'rain', 'charger', 'pen'],
    3: ['camera'],
    4: ['car', 'watch', 'seaweed', 'fish', 'belt']
}

# Replace the bowl and the doll with the razor and the toothbrush in Box 0.
boxes[0].remove('bowl')
boxes[0].remove('doll')
boxes[0].append('razor')
boxes[0].append('toothbrush')

# Remove the camera from Box 3.
boxes[3].remove('camera')

# Remove the fish and the seaweed and the watch from Box 4.
items_to_remove = ['fish', 'seaweed', 'watch']
for item in items_to_remove:
    boxes[4].remove(item)

# Replace the desert and the beach with the fridge and the candle in Box 1.
boxes[1].remove('desert')
boxes[1].remove('beach')
boxes[1].append('fridge')
boxes[1].append('candle')

# Move the scarf from Box 1 to Box 0.
boxes[1].remove('scarf')
boxes[0].append('scarf')

# Put the towel and the paint and the tie into Box 1.
items_to_add = ['towel', 'paint', 'tie']
for item in items_to_add:
    boxes[1].append(item)

# Replace the toothbrush and the razor with the bell and the frame in Box 0.
boxes[0].remove('toothbrush')
boxes[0].remove('razor')
boxes[0].append('bell')
boxes[0].append('frame')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")