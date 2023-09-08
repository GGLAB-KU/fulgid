# Initial state of boxes
boxes = {
    0: ['shorts', 'earring', 'mixer', 'battery'],
    1: ['blender', 'planet'],
    2: ['needle', 'rain', 'game', 'perfume'],
    3: ['console', 'shark', 'island', 'controller', 'mountain'],
    4: [],
    5: [],
    6: ['fork', 'boot', 'lamp'],
    7: ['candle', 'umbrella', 'lion', 'lightning', 'ship'],
    8: ['belt', 'piano'],
    9: ['mirror', 'leaf'],
    10: ['basket', 'glove', 'ocean']
}

# Remove the planet and the blender from Box 1.
boxes[1].remove('planet')
boxes[1].remove('blender')

# Remove the basket and the glove from Box 10.
boxes[10].remove('basket')
boxes[10].remove('glove')

# Put the plane into Box 4.
boxes[4].append('plane')

# Swap the belt in Box 8 with the mirror in Box 9.
boxes[8].remove('belt')
boxes[9].remove('mirror')
boxes[8].append('mirror')
boxes[9].append('belt')

# Empty Box 4.
boxes[4] = []

# Empty Box 6.
boxes[6] = []

# Remove the candle and the ship and the umbrella from Box 7.
items_to_remove = ['candle', 'ship', 'umbrella']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the puzzle and the towel into Box 2.
boxes[2].append('puzzle')
boxes[2].append('towel')

# Empty Box 7.
boxes[7] = []

# Put the doll into Box 2.
boxes[2].append('doll')

# Move the battery from Box 0 to Box 9.
boxes[0].remove('battery')
boxes[9].append('battery')

# Remove the piano from Box 8.
boxes[8].remove('piano')

# Remove the battery and the belt from Box 9.
boxes[9].remove('battery')
boxes[9].remove('belt')

# Remove the mixer from Box 0.
boxes[0].remove('mixer')

# Replace the mountain and the controller with the glasses and the ocean in Box 3.
boxes[3].remove('mountain')
boxes[3].remove('controller')
boxes[3].append('glasses')
boxes[3].append('ocean')

# Replace the glasses and the ocean with the perfume and the flower in Box 3.
boxes[3].remove('glasses')
boxes[3].remove('ocean')
boxes[3].append('perfume')
boxes[3].append('flower')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")