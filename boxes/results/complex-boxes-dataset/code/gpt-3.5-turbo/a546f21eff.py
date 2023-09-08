# Initial state of boxes
boxes = {
    0: ['seaweed', 'controller', 'toothbrush', 'console', 'dolphin'],
    1: ['frame'],
    2: ['octopus', 'grass', 'coin'],
    3: ['truck', 'glove', 'river', 'cloud', 'forest'],
    4: ['sculpture', 'rocket', 'needle', 'freezer'],
    5: ['dice', 'shorts'],
    6: ['zipper', 'plate', 'pot', 'gloves', 'pillow'],
    7: ['button', 'tiger'],
    8: ['card', 'star', 'grinder'],
    9: ['phone', 'sock', 'crown', 'necklace', 'blender'],
    10: ['perfume', 'headphone', 'violin'],
    11: ['book'],
    12: ['usb', 'boat', 'wig', 'meteor', 'vase'],
    13: ['horn', 'elephant', 'flower', 'rain']
}

# Put the hat and the boot and the razor into Box 11.
boxes[11].extend(['hat', 'boot', 'razor'])

# Remove the seaweed and the toothbrush from Box 0.
boxes[0].remove('seaweed')
boxes[0].remove('toothbrush')

# Swap the razor in Box 11 with the wig in Box 12.
boxes[11].remove('razor')
boxes[12].remove('wig')
boxes[11].append('wig')
boxes[12].append('razor')

# Put the octopus and the harmonica and the sculpture into Box 5.
boxes[5].extend(['octopus', 'harmonica', 'sculpture'])

# Move the console and the dolphin and the controller from Box 0 to Box 12.
items_to_move = ['console', 'dolphin', 'controller']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[12].append(item)

# Swap the vase in Box 12 with the frame in Box 1.
boxes[12].remove('vase')
boxes[1].remove('frame')
boxes[12].append('frame')
boxes[1].append('vase')

# Remove the coin and the grass and the octopus from Box 2.
items_to_remove = ['coin', 'grass', 'octopus']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the pillow and the plate and the zipper from Box 6.
items_to_remove = ['pillow', 'plate', 'zipper']
for item in items_to_remove:
    boxes[6].remove(item)

# Replace the crown and the blender and the necklace with the earring and the forest and the towel in Box 9.
boxes[9].remove('crown')
boxes[9].remove('blender')
boxes[9].remove('necklace')
boxes[9].append('earring')
boxes[9].append('forest')
boxes[9].append('towel')

# Move the phone from Box 9 to Box 0.
boxes[9].remove('phone')
boxes[0].append('phone')

# Swap the grinder in Box 8 with the tiger in Box 7.
boxes[8].remove('grinder')
boxes[7].remove('tiger')
boxes[8].append('tiger')
boxes[7].append('grinder')

# Move the violin and the perfume and the headphone from Box 10 to Box 9.
items_to_move = ['violin', 'perfume', 'headphone']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[9].append(item)

# Put the butterfly and the pot into Box 12.
boxes[12].extend(['butterfly', 'pot'])

# Swap the perfume in Box 9 with the vase in Box 1.
boxes[9].remove('perfume')
boxes[1].remove('vase')
boxes[9].append('vase')
boxes[1].append('perfume')

# Put the freezer and the star into Box 0.
boxes[0].extend(['freezer', 'star'])

# Empty Box 5.
boxes[5] = []

# Replace the meteor and the razor and the pot with the coral and the desert and the button in Box 12.
boxes[12].remove('meteor')
boxes[12].remove('razor')
boxes[12].remove('pot')
boxes[12].extend(['coral', 'desert', 'button'])

# Empty Box 1.
boxes[1] = []

# Put the lipstick into Box 8.
boxes[8].append('lipstick')

# Move the button and the grinder from Box 7 to Box 9.
boxes[7].remove('button')
boxes[9].append('button')
boxes[9].remove('grinder')
boxes[9].append('grinder')

# Replace the forest and the towel and the violin with the meteor and the octopus and the swimsuit in Box 9.
boxes[9].remove('forest')
boxes[9].remove('towel')
boxes[9].remove('violin')
boxes[9].append('meteor')
boxes[9].append('octopus')
boxes[9].append('swimsuit')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")