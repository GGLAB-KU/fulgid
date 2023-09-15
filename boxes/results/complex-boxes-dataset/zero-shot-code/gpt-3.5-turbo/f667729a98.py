box_0 = ['lock', 'button', 'planet', 'charger', 'camera']
box_1 = []
box_2 = ['magnet', 'desert', 'clock']
box_3 = ['candle', 'crown']
box_4 = []
box_5 = ['usb', 'whistle', 'pants']
box_6 = ['tape', 'moon', 'submarine', 'table', 'leaf']
box_7 = []
box_8 = ['guitar', 'frame', 'fridge', 'flower']
box_9 = []
box_10 = ['thunder', 'beach']
box_11 = ['lipstick', 'pan', 'brush']
box_12 = []
box_13 = []

# Swap the crown in Box 3 with the moon in Box 6
box_3.remove('crown')
box_6.remove('moon')
box_3.append('moon')
box_6.append('crown')

# Replace the candle and the moon with the shoes and the plate in Box 3
box_3.remove('candle')
box_3.remove('moon')
box_3.append('shoes')
box_3.append('plate')

# Replace the plate and the shoes with the beach and the car in Box 3
box_3.remove('plate')
box_3.remove('shoes')
box_3.append('beach')
box_3.append('car')

# Swap the tape in Box 6 with the brush in Box 11
box_6.remove('tape')
box_11.remove('brush')
box_6.append('brush')
box_11.append('tape')

# Replace the thunder with the flute in Box 10
box_10.remove('thunder')
box_10.append('flute')

# Swap the button in Box 0 with the flute in Box 10
box_0.remove('button')
box_10.remove('flute')
box_0.append('flute')
box_10.append('button')

# Put the lion and the swimsuit and the grinder into Box 9
box_9.extend(['lion', 'swimsuit', 'grinder'])

# Remove the lipstick and the tape from Box 11
box_11.remove('lipstick')
box_11.remove('tape')

# Put the wig and the island and the pants into Box 4
box_4.extend(['wig', 'island', 'pants'])

# Empty Box 10
box_10.clear()

# Move the desert from Box 2 to Box 4
box_2.remove('desert')
box_4.append('desert')

# Remove the charger from Box 0
box_0.remove('charger')

# Replace the crown with the plane in Box 6
box_6.remove('crown')
box_6.append('plane')

# Put the magnet and the card and the tie into Box 5
box_5.extend(['magnet', 'card', 'tie'])

# Remove the clock from Box 2
box_2.remove('clock')

# Put the lion into Box 0
box_0.append('lion')

# Put the camera and the boat into Box 13
box_13.extend(['camera', 'boat'])

# Move the plane and the leaf from Box 6 to Box 10
box_6.remove('plane')
box_6.remove('leaf')
box_10.extend(['plane', 'leaf'])

# Put the scissors into Box 1
box_1.append('scissors')

# Remove the lion and the grinder from Box 9
box_9.remove('lion')
box_9.remove('grinder')

# Empty Box 3
box_3.clear()

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")