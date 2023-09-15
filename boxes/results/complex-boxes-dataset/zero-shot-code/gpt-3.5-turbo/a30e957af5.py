box = {
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

def print_boxes():
    for i in range(9):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Move the octopus from Box 5 to Box 2
box[2].append(box[5].pop())

# Replace the doll and the violin with the glove and the perfume in Box 8
box[8] = ['glove', 'perfume']

# Remove the dolphin from Box 0
box.pop(0)

# Replace the rain and the dress with the needle and the dice in Box 7
box[7] = ['needle', 'dice']

# Move the oven and the camera and the meteor from Box 4 to Box 7
box[7].extend(box[4].pop(2))
box[7].extend(box[4].pop(1))
box[7].extend(box[4].pop(0))

# Replace the wig and the gloves with the dice and the battery in Box 6
box[6] = ['dice', 'battery']

# Empty Box 8
box.pop(8)

# Remove the octopus from Box 2
box[2].remove('octopus')

# Empty Box 7
box.pop(7)

# Replace the battery and the dice and the button with the plane and the mirror and the snow in Box 6
box[6] = ['plane', 'mirror', 'snow']

# Swap the lion in Box 6 with the flute in Box 3
box[6], box[3] = box[3], box[6]

# Move the blender from Box 1 to Box 6
box[6].append(box[1].pop())

# Remove the harmonica and the tape from Box 4
box[4].remove('harmonica')
box[4].remove('tape')

# Move the needle from Box 3 to Box 1
box[1].append(box[3].pop())

# Print the final state of the boxes
print_boxes()