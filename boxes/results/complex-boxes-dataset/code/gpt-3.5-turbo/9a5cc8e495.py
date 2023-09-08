# Initial state of boxes
boxes = {
    0: [],
    1: ['forest', 'rocket'],
    2: ['comb', 'dolphin', 'river', 'guitar'],
    3: ['camera', 'frame', 'glasses', 'moon'],
    4: [],
    5: ['lion', 'battery', 'chair'],
    6: [],
    7: [],
    8: ['magnet'],
    9: ['fridge', 'tiger']
}

# Remove the dolphin from Box 2.
boxes[2].remove('dolphin')

# Put the cow into Box 0.
boxes[0].append('cow')

# Swap the fridge in Box 9 with the magnet in Box 8.
boxes[8], boxes[9] = boxes[9], boxes[8]

# Replace the moon and the frame with the shampoo and the vase in Box 3.
boxes[3].remove('moon')
boxes[3].remove('frame')
boxes[3].append('shampoo')
boxes[3].append('vase')

# Replace the fridge with the headphone in Box 8.
boxes[8].remove('fridge')
boxes[8].append('headphone')

# Empty Box 2.
boxes[2] = []

# Put the dog and the table into Box 2.
boxes[2].append('dog')
boxes[2].append('table')

# Replace the magnet with the camera in Box 9.
boxes[9].remove('magnet')
boxes[9].append('camera')

# Put the shampoo and the swimsuit and the laptop into Box 3.
boxes[3].append('shampoo')
boxes[3].append('swimsuit')
boxes[3].append('laptop')

# Put the octopus and the ring and the seaweed into Box 2.
boxes[2].append('octopus')
boxes[2].append('ring')
boxes[2].append('seaweed')

# Put the scarf and the battery and the horse into Box 9.
boxes[9].append('scarf')
boxes[9].append('battery')
boxes[9].append('horse')

# Replace the shampoo with the fork in Box 3.
boxes[3].remove('shampoo')
boxes[3].append('fork')

# Remove the lion from Box 5.
boxes[5].remove('lion')

# Swap the swimsuit in Box 3 with the chair in Box 5.
boxes[3], boxes[5] = boxes[5], boxes[3]

# Replace the swimsuit and the battery with the desert and the button in Box 5.
boxes[5].remove('swimsuit')
boxes[5].remove('battery')
boxes[5].append('desert')
boxes[5].append('button')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")