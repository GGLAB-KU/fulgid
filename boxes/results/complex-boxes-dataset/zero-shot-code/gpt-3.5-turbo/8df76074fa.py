box = {
    0: ['rain', 'bicycle', 'truck'],
    1: ['bag', 'butterfly'],
    2: ['book'],
    3: ['zipper', 'belt'],
    4: ['river', 'train', 'toothpaste', 'bracelet', 'basket'],
    5: ['battery', 'vase', 'clock'],
    6: ['boot'],
    7: [],
    8: ['towel', 'ring', 'pan'],
    9: ['octopus', 'flower', 'whistle', 'skirt'],
    10: [],
    11: []
}

def print_box_contents():
    for index, items in box.items():
        print(f"Box {index}: {items}")

# Initial state
print_box_contents()

# Put the key and the usb into Box 8
box[8].extend(['key', 'usb'])

# Remove the pan from Box 8
box[8].remove('pan')

# Put the telescope and the plate into Box 5
box[5].extend(['telescope', 'plate'])

# Remove the towel from Box 8
box[8].remove('towel')

# Remove the boot from Box 6
box[6].remove('boot')

# Move the usb from Box 8 to Box 0
box[0].append(box[8].pop(box[8].index('usb')))

# Move the bag from Box 1 to Box 7
box[7].append(box[1].pop(box[1].index('bag')))

# Swap the usb in Box 0 with the river in Box 4
box[0].append(box[4].pop(box[4].index('river')))
box[4].append(box[0].pop(box[0].index('usb')))

# Move the book from Box 2 to Box 8
box[8].append(box[2].pop(box[2].index('book')))

# Replace the bracelet and the train and the basket with the charger and the plane and the toothpaste in Box 4
box[4].remove('bracelet')
box[4].remove('train')
box[4].remove('basket')
box[4].extend(['charger', 'plane', 'toothpaste'])

# Swap the butterfly in Box 1 with the zipper in Box 3
box[1].append(box[3].pop(box[3].index('zipper')))
box[3].append(box[1].pop(box[1].index('butterfly')))

# Replace the zipper with the comb in Box 1
box[1].remove('zipper')
box[1].append('comb')

# Remove the belt and the butterfly from Box 3
box[3].remove('belt')
box[3].remove('butterfly')

# Replace the comb with the toaster in Box 1
box[1].remove('comb')
box[1].append('toaster')

# Move the octopus and the flower and the skirt from Box 9 to Box 4
box[4].extend(['octopus', 'flower', 'skirt'])
box[9].remove('octopus')
box[9].remove('flower')
box[9].remove('skirt')

# Replace the ring with the bear in Box 8
box[8].remove('ring')
box[8].append('bear')

# Swap the telescope in Box 5 with the river in Box 0
box[5].append(box[0].pop(box[0].index('river')))
box[0].append(box[5].pop(box[5].index('telescope')))

# Move the book from Box 8 to Box 5
box[5].append(box[8].pop(box[8].index('book')))

# Final state
print_box_contents()