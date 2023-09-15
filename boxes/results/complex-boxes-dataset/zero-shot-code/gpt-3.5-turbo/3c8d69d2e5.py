box_0 = ['thread', 'bus', 'train', 'meteor', 'flute']
box_1 = ['coral']
box_2 = ['sock', 'toothpaste', 'bell']
box_3 = ['vase', 'scarf', 'moon']
box_4 = ['jacket']
box_5 = []
box_6 = ['truck', 'bag', 'river', 'dice']
box_7 = ['thunder', 'fork', 'fridge', 'harmonica', 'frame']
box_8 = ['toothbrush']
box_9 = ['blanket', 'wallet', 'shorts', 'wire', 'soap']
box_10 = []
box_11 = ['tiger', 'lamp', 'skirt', 'wig', 'bowl']
box_12 = ['rock', 'plate']

def print_boxes():
    boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]
    for i, box in enumerate(boxes):
        print(f"Box {i}: {box}")

def remove_item(box, item):
    if item in box:
        box.remove(item)

def move_item(source_box, destination_box, item):
    if item in source_box:
        source_box.remove(item)
        destination_box.append(item)

# Remove the river from Box 6
remove_item(box_6, 'river')

# Replace the plate with the drum in Box 12
remove_item(box_12, 'plate')
box_12.append('drum')

# Remove the drum from Box 12
remove_item(box_12, 'drum')

# Move the vase and the scarf from Box 3 to Box 5
move_item(box_3, box_5, 'vase')
move_item(box_3, box_5, 'scarf')

# Move the train and the thread and the meteor from Box 0 to Box 2
move_item(box_0, box_2, 'train')
move_item(box_0, box_2, 'thread')
move_item(box_0, box_2, 'meteor')

# Put the laptop and the chair and the mountain into Box 1
box_1.extend(['laptop', 'chair', 'mountain'])

# Replace the harmonica and the frame with the shoes and the soap in Box 7
remove_item(box_7, 'harmonica')
remove_item(box_7, 'frame')
box_7.extend(['shoes', 'soap'])

# Move the bus from Box 0 to Box 4
move_item(box_0, box_4, 'bus')

# Remove the vase and the scarf from Box 5
remove_item(box_5, 'vase')
remove_item(box_5, 'scarf')

# Remove the jacket from Box 4
remove_item(box_4, 'jacket')

# Remove the tiger from Box 11
remove_item(box_11, 'tiger')

# Replace the wallet and the soap and the blanket with the boot and the rocket and the button in Box 9
remove_item(box_9, 'wallet')
remove_item(box_9, 'soap')
remove_item(box_9, 'blanket')
box_9.extend(['boot', 'rocket', 'button'])

# Remove the laptop from Box 1
remove_item(box_1, 'laptop')

# Replace the soap with the bag in Box 7
remove_item(box_7, 'soap')
box_7.append('bag')

# Put the cup and the shampoo into Box 9
box_9.extend(['cup', 'shampoo'])

# Replace the skirt and the lamp with the plate and the horn in Box 11
remove_item(box_11, 'skirt')
remove_item(box_11, 'lamp')
box_11.extend(['plate', 'horn'])

# Replace the bus with the submarine in Box 4
remove_item(box_4, 'bus')
box_4.append('submarine')

# Remove the submarine from Box 4
remove_item(box_4, 'submarine')

# Move the rock from Box 12 to Box 7
move_item(box_12, box_7, 'rock')

# Move the toothpaste and the meteor from Box 2 to Box 1
move_item(box_2, box_1, 'toothpaste')
move_item(box_2, box_1, 'meteor')

# Print the updated boxes
print_boxes()