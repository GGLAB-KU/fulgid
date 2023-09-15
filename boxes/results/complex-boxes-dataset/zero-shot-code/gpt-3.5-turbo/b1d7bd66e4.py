box_0 = []
box_1 = ['train']
box_2 = ['toaster', 'bracelet', 'storm', 'fridge']
box_3 = ['usb', 'fish', 'note', 'coral']
box_4 = ['thunder', 'lightning']
box_5 = ['doll', 'pillow']
box_6 = ['wig']
box_7 = ['earring', 'thread', 'mountain', 'coin', 'game']
box_8 = ['dress', 'mask', 'dice']
box_9 = ['guitar', 'jungle', 'puzzle', 'flute', 'microscope']
box_10 = []
box_11 = ['comet', 'jacket', 'star', 'basket']
box_12 = ['island', 'pants', 'sun', 'grinder']
box_13 = ['ship', 'blender', 'controller', 'leaf']
box_14 = ['spoon', 'scissors', 'horn', 'horse']

box_2 = ['scissors', 'polish', 'rocket']
box_8 = []
box_3 = ['bag', 'bicycle']
box_5 = ['rocket']
box_14 = []
box_1 = []
box_13 = []
box_3 = ['ring', 'bag']
box_5 = ['grass', 'boot']
box_2 = []
box_10 = ['truck']
box_5 = ['star']
box_13 = ['leaf', 'pen', 'whistle']
box_10 = []
box_6, box_9 = box_9, box_6
box_9 = []
box_7.append('jungle')
box_7.extend(box_3)
box_8.append('river')
box_6.append('pants')
box_7 = []
box_8.remove('river')
box_3[0] = 'tie'

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")