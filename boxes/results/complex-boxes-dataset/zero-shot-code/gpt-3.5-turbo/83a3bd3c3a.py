box = {
    0: ['tape'],
    1: [],
    2: ['controller'],
    3: [],
    4: ['headphone'],
    5: ['toaster', 'toy', 'grass'],
    6: ['blanket', 'moon', 'mask'],
    7: ['umbrella', 'sun', 'forest', 'thunder'],
    8: ['book', 'flute', 'helmet', 'ocean', 'cat'],
    9: ['desert', 'pants'],
    10: ['hat', 'card'],
    11: ['coin', 'drum', 'telescope', 'fridge', 'spoon'],
    12: []
}

def print_box_contents():
    for index, items in box.items():
        print(f"Box {index}: {items}")

def put_item_in_box(item, box_index):
    if box_index in box:
        box[box_index].append(item)
    else:
        box[box_index] = [item]

def remove_item_from_box(item, box_index):
    if box_index in box:
        if item in box[box_index]:
            box[box_index].remove(item)

def move_item_between_boxes(item, source_box_index, destination_box_index):
    remove_item_from_box(item, source_box_index)
    put_item_in_box(item, destination_box_index)

# Initial box contents
print_box_contents()

# Put the polish into Box 8
put_item_in_box('polish', 8)

# Put the jacket and the frame and the sculpture into Box 8
put_item_in_box('jacket', 8)
put_item_in_box('frame', 8)
put_item_in_box('sculpture', 8)

# Remove the frame and the ocean and the flute from Box 8
remove_item_from_box('frame', 8)
remove_item_from_box('ocean', 8)
remove_item_from_box('flute', 8)

# Put the star into Box 12
put_item_in_box('star', 12)

# Remove the tape from Box 0
remove_item_from_box('tape', 0)

# Move the star from Box 12 to Box 6
move_item_between_boxes('star', 12, 6)

# Remove the controller from Box 2
remove_item_from_box('controller', 2)

# Move the desert from Box 9 to Box 4
move_item_between_boxes('desert', 9, 4)

# Put the speaker and the razor into Box 7
put_item_in_box('speaker', 7)
put_item_in_box('razor', 7)

# Remove the razor from Box 7
remove_item_from_box('razor', 7)

# Move the pants from Box 9 to Box 5
move_item_between_boxes('pants', 9, 5)

# Remove the hat and the card from Box 10
remove_item_from_box('hat', 10)
remove_item_from_box('card', 10)

# Move the mask from Box 6 to Box 5
move_item_between_boxes('mask', 6, 5)

# Move the headphone and the desert from Box 4 to Box 7
move_item_between_boxes('headphone', 4, 7)
move_item_between_boxes('desert', 4, 7)

# Empty Box 6
box[6] = []

# Remove the spoon and the drum from Box 11
remove_item_from_box('spoon', 11)
remove_item_from_box('drum', 11)

# Move the book from Box 8 to Box 12
move_item_between_boxes('book', 8, 12)

# Put the butterfly and the drum and the boat into Box 5
put_item_in_box('butterfly', 5)
put_item_in_box('drum', 5)
put_item_in_box('boat', 5)

# Remove the fridge and the coin and the telescope from Box 11
remove_item_from_box('fridge', 11)
remove_item_from_box('coin', 11)
remove_item_from_box('telescope', 11)

# Final box contents
print_box_contents()