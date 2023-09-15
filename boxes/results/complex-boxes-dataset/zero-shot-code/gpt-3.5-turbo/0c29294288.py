box_0 = ['camera', 'bracelet', 'ring', 'toaster', 'pot']
box_1 = ['keyboard', 'elephant', 'laptop', 'phone', 'toy']
box_2 = ['scarf', 'flute']
box_3 = ['earring', 'wig', 'frame', 'sock', 'butterfly', 'pan']
box_4 = ['bag', 'shoe', 'makeup', 'shirt', 'star', 'dress', 'bowl', 'basket', 'butterfly']
box_5 = ['cloud', 'umbrella', 'train', 'candle']
box_6 = ['sock', 'necklace', 'doll', 'butterfly', 'lipstick', 'forest']

box_5.remove('mask')
box_5.append('umbrella')
box_2.remove('piano')
box_2.append('flute')
box_6.extend(['butterfly', 'truck'])
box_5.remove('candle')
box_3.remove('frame')
box_3.append('candle')
box_6.remove('butterfly')
box_6.remove('truck')
box_6.extend(['lipstick', 'forest'])
box_4.remove('shirt')
box_4.remove('bag')
box_4.remove('makeup')
box_4.extend(['star', 'dress', 'bowl'])
box_0.remove('toaster')
box_4.append('toaster')
box_3.extend(['sock', 'butterfly', 'pan'])
box_2.append('boat')
box_4.extend(['basket', 'butterfly'])

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")