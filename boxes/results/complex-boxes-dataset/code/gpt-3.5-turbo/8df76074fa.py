# Initial state of boxes
boxes = {
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

# Put the key and the usb into Box 8.
boxes[8].append('key')
boxes[8].append('usb')

# Remove the pan from Box 8.
boxes[8].remove('pan')

# Put the telescope and the plate into Box 5.
boxes[5].append('telescope')
boxes[5].append('plate')

# Remove the towel from Box 8.
boxes[8].remove('towel')

# Remove the boot from Box 6.
boxes[6].remove('boot')

# Move the usb from Box 8 to Box 0.
boxes[8].remove('usb')
boxes[0].append('usb')

# Move the bag from Box 1 to Box 7.
boxes[1].remove('bag')
boxes[7].append('bag')

# Swap the usb in Box 0 with the river in Box 4.
boxes[0].remove('usb')
boxes[4].remove('river')
boxes[0].append('river')
boxes[4].append('usb')

# Move the book from Box 2 to Box 8.
boxes[2].remove('book')
boxes[8].append('book')

# Replace the bracelet and the train and the basket with the charger and the plane and the toothpaste in Box 4.
boxes[4].remove('bracelet')
boxes[4].remove('train')
boxes[4].remove('basket')
boxes[4].append('charger')
boxes[4].append('plane')
boxes[4].append('toothpaste')

# Swap the butterfly in Box 1 with the zipper in Box 3.
boxes[1].remove('butterfly')
boxes[3].remove('zipper')
boxes[1].append('zipper')
boxes[3].append('butterfly')

# Replace the zipper with the comb in Box 1.
boxes[1].remove('zipper')
boxes[1].append('comb')

# Remove the belt and the butterfly from Box 3.
boxes[3].remove('belt')
boxes[3].remove('butterfly')

# Replace the comb with the toaster in Box 1.
boxes[1].remove('comb')
boxes[1].append('toaster')

# Move the octopus and the flower and the skirt from Box 9 to Box 4.
items_to_move = ['octopus', 'flower', 'skirt']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[4].append(item)

# Replace the ring with the bear in Box 8.
boxes[8].remove('ring')
boxes[8].append('bear')

# Swap the telescope in Box 5 with the river in Box 0.
boxes[5].remove('telescope')
boxes[0].remove('river')
boxes[5].append('river')
boxes[0].append('telescope')

# Move the book from Box 8 to Box 5.
boxes[8].remove('book')
boxes[5].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")