box = {
    0: ['comet'],
    1: ['wallet', 'toy'],
    2: ['ring', 'basket', 'river', 'earring', 'charger'],
    3: ['plane', 'motorcycle', 'usb', 'freezer', 'table'],
    4: ['towel', 'storm', 'tie', 'octopus', 'rock'],
    5: ['scissors', 'shoes', 'blanket', 'card'],
    6: ['makeup', 'cow', 'branch'],
    7: ['ocean'],
    8: ['car', 'cat', 'mirror'],
    9: ['seaweed', 'pen', 'mask'],
    10: []
}

def empty_box(box_index):
    box[box_index] = []

def move_items(source_box, target_box, items):
    for item in items:
        box[source_box].remove(item)
        box[target_box].append(item)

def swap_items(box1, box2):
    box[box1], box[box2] = box[box2], box[box1]

empty_box(3)
move_items(1, 10, ['wallet', 'toy'])
move_items(2, 6, ['basket', 'earring', 'charger'])
move_items(9, 4, ['seaweed', 'pen', 'mask'])
swap_items(8, 7)
move_items(0, 2, ['comet'])
box[2].extend(['octopus', 'coin', 'magnet'])
swap_items(2, 4)
empty_box(8)
box[7] = ['tree']
box[8] = ['towel']
box[3].extend(['guitar', 'candle'])
box[1].append('cup')
swap_items(4, 4)
swap_items(10, 4)
move_items(10, 4, ['toy', 'flute'])
move_items(6, 2, ['cow'])

for box_index, items in box.items():
    print(f"Box {box_index}: {items}")