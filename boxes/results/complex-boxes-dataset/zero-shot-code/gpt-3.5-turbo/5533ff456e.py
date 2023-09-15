box_0 = ['mirror', 'doll', 'puzzle', 'wire', 'oven']
box_1 = ['brush', 'bicycle', 'dress', 'blanket']
box_2 = ['phone', 'sock', 'basket']
box_3 = ['cat']
box_4 = ['mountain', 'note', 'glove', 'starfish', 'bag']
box_5 = ['elephant', 'tiger', 'comb', 'lion', 'bracelet']
box_6 = ['island']
box_7 = ['whistle', 'plate', 'grinder', 'branch']
box_8 = ['dice', 'zipper', 'guitar']
box_9 = ['toothbrush', 'pillow']
box_10 = ['comet', 'harmonica', 'rain', 'submarine']

box_8 = ['dice', 'zipper', 'guitar']
box_10 = []

box_9 = ['glasses']

box_10 = box_8 + box_10
box_8 = []

box_1.remove('bicycle')
box_1.remove('blanket')

box_5[2], box_4[1] = box_4[1], box_5[2]

box_0.remove('doll')

box_3[0], box_7[3] = box_7[3], box_3[0]

box_7.remove('grinder')

box_10 = []

box_6.append(box_4.pop(2))
box_6.append(box_4.pop(2))

box_7.append('meteor')

box_5.extend(['toothbrush', 'button', 'spoon'])

box_10.append('bracelet')

box_1 = ['scarf', 'desert']

box_3.extend(['glasses', 'pillow'])

box_1[1], box_2[2] = box_2[2], box_1[1]

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")