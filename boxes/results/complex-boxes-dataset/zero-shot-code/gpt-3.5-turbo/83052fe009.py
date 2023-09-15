box_0 = ['bowl', 'doll']
box_1 = ['scarf', 'horn', 'desert', 'beach']
box_2 = ['console', 'rain', 'charger', 'pen']
box_3 = ['camera']
box_4 = ['car', 'watch', 'seaweed', 'fish', 'belt']

# Replace the bowl and the doll with the razor and the toothbrush in Box 0
box_0 = ['razor', 'toothbrush']

# Remove the camera from Box 3
box_3 = []

# Remove the fish and the seaweed and the watch from Box 4
box_4 = []

# Replace the desert and the beach with the fridge and the candle in Box 1
box_1 = ['fridge', 'candle']

# Move the scarf from Box 1 to Box 0
box_0.append('scarf')
box_1.remove('scarf')

# Put the towel and the paint and the tie into Box 1
box_1.extend(['towel', 'paint', 'tie'])

# Replace the toothbrush and the razor with the bell and the frame in Box 0
box_0 = ['bell', 'frame']

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)