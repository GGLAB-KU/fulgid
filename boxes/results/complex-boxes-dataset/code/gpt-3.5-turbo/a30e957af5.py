# Initial state of boxes
boxes = {
    0: ['dolphin'],
    1: ['blender'],
    2: ['sun', 'forest'],
    3: ['sandals', 'flute', 'needle'],
    4: ['meteor', 'camera', 'oven', 'harmonica', 'tape'],
    5: ['octopus'],
    6: ['lion', 'button', 'gloves', 'wig', 'pillow'],
    7: ['dress', 'rain'],
    8: ['doll', 'violin']
}

# Move the octopus from Box 5 to Box 2.
boxes[5].remove('octopus')
boxes[2].append('octopus')

# Replace the doll and the violin with the glove and the perfume in Box 8.
boxes[8].remove('doll')
boxes[8].remove('violin')
boxes[8].append('glove')
boxes[8].append('perfume')

# Remove the dolphin from Box 0.
boxes[0].remove('dolphin')

# Replace the rain and the dress with the needle and the dice in Box 7.
boxes[7].remove('rain')
boxes[7].remove('dress')
boxes[7].append('needle')
boxes[7].append('dice')

# Move the oven and the camera and the meteor from Box 4 to Box 7.
items_to_move = ['oven', 'camera', 'meteor']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[7].append(item)

# Replace the wig and the gloves with the dice and the battery in Box 6.
boxes[6].remove('wig')
boxes[6].remove('gloves')
boxes[6].append('dice')
boxes[6].append('battery')

# Empty Box 8.
boxes[8] = []

# Remove the octopus from Box 2.
boxes[2].remove('octopus')

# Empty Box 7.
boxes[7] = []

# Replace the battery and the dice and the button with the plane and the mirror and the snow in Box 6.
boxes[6].remove('battery')
boxes[6].remove('dice')
boxes[6].remove('button')
boxes[6].append('plane')
boxes[6].append('mirror')
boxes[6].append('snow')

# Swap the lion in Box 6 with the flute in Box 3.
boxes[6].remove('lion')
boxes[3].remove('flute')
boxes[6].append('flute')
boxes[3].append('lion')

# Move the blender from Box 1 to Box 6.
boxes[1].remove('blender')
boxes[6].append('blender')

# Remove the harmonica and the tape from Box 4.
boxes[4].remove('harmonica')
boxes[4].remove('tape')

# Move the needle from Box 3 to Box 1.
boxes[3].remove('needle')
boxes[1].append('needle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")