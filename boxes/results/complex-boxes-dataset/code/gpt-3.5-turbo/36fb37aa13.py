# Initial state of boxes
boxes = {
    0: ['watch', 'perfume', 'makeup'],
    1: ['frame', 'cow', 'chair', 'rock', 'bicycle'],
    2: [],
    3: ['pot', 'piano', 'freezer'],
    4: ['toy', 'towel', 'glove', 'flower'],
    5: ['seaweed', 'island', 'truck'],
    6: ['train'],
    7: ['dice'],
    8: ['lamp', 'usb'],
    9: ['motorcycle', 'drum', 'toothpaste', 'rocket', 'gloves'],
    10: ['game', 'whistle', 'scissors'],
    11: ['scarf'],
    12: ['oven'],
    13: ['submarine', 'boat', 'sock', 'mask', 'console'],
    14: ['toothbrush', 'pillow', 'cup', 'jacket', 'rain']
}

# Swap the frame in Box 1 with the train in Box 6.
boxes[1].remove('frame')
boxes[6].remove('train')
boxes[1].append('train')
boxes[6].append('frame')

# Move the pot and the freezer from Box 3 to Box 5.
boxes[3].remove('pot')
boxes[3].remove('freezer')
boxes[5].append('pot')
boxes[5].append('freezer')

# Remove the pot and the seaweed from Box 5.
boxes[5].remove('pot')
boxes[5].remove('seaweed')

# Remove the oven from Box 12.
boxes[12].remove('oven')

# Swap the flower in Box 4 with the cow in Box 1.
boxes[4].remove('flower')
boxes[1].remove('cow')
boxes[4].append('cow')
boxes[1].append('flower')

# Replace the makeup and the watch and the perfume with the shampoo and the bus and the headphone in Box 0.
boxes[0].remove('makeup')
boxes[0].remove('watch')
boxes[0].remove('perfume')
boxes[0].append('shampoo')
boxes[0].append('bus')
boxes[0].append('headphone')

# Move the motorcycle and the gloves from Box 9 to Box 2.
boxes[9].remove('motorcycle')
boxes[9].remove('gloves')
boxes[2].append('motorcycle')
boxes[2].append('gloves')

# Move the cow and the toy and the towel from Box 4 to Box 3.
boxes[4].remove('cow')
boxes[4].remove('toy')
boxes[4].remove('towel')
boxes[3].append('cow')
boxes[3].append('toy')
boxes[3].append('towel')

# Replace the bus with the moon in Box 0.
boxes[0].remove('bus')
boxes[0].append('moon')

# Swap the jacket in Box 14 with the usb in Box 8.
boxes[14].remove('jacket')
boxes[8].remove('usb')
boxes[14].append('usb')
boxes[8].append('jacket')

# Move the drum and the toothpaste and the rocket from Box 9 to Box 0.
boxes[9].remove('drum')
boxes[9].remove('toothpaste')
boxes[9].remove('rocket')
boxes[0].append('drum')
boxes[0].append('toothpaste')
boxes[0].append('rocket')

# Remove the scarf from Box 11.
boxes[11].remove('scarf')

# Move the rock and the bicycle from Box 1 to Box 5.
boxes[1].remove('rock')
boxes[1].remove('bicycle')
boxes[5].append('rock')
boxes[5].append('bicycle')

# Put the telescope and the lipstick and the fork into Box 14.
boxes[14].append('telescope')
boxes[14].append('lipstick')
boxes[14].append('fork')

# Swap the dice in Box 7 with the motorcycle in Box 2.
boxes[7].remove('dice')
boxes[2].remove('motorcycle')
boxes[7].append('motorcycle')
boxes[2].append('dice')

# Swap the glove in Box 4 with the console in Box 13.
boxes[4].remove('glove')
boxes[13].remove('console')
boxes[4].append('console')
boxes[13].append('glove')

# Put the pen and the microscope and the laptop into Box 1.
boxes[1].append('pen')
boxes[1].append('microscope')
boxes[1].append('laptop')

# Move the microscope from Box 1 to Box 5.
boxes[1].remove('microscope')
boxes[5].append('microscope')

# Swap the mask in Box 13 with the frame in Box 6.
boxes[13].remove('mask')
boxes[6].remove('frame')
boxes[13].append('frame')
boxes[6].append('mask')

# Replace the shampoo and the headphone and the moon with the button and the ocean and the octopus in Box 0.
boxes[0].remove('shampoo')
boxes[0].remove('headphone')
boxes[0].remove('moon')
boxes[0].append('button')
boxes[0].append('ocean')
boxes[0].append('octopus')

# Put the cat and the book and the sock into Box 12.
boxes[12].append('cat')
boxes[12].append('book')
boxes[12].append('sock')

# Move the whistle from Box 10 to Box 9.
boxes[10].remove('whistle')
boxes[9].append('whistle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")