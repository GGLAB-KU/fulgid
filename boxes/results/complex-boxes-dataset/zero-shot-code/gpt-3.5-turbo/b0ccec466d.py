box_0 = ['telescope', 'candle']
box_1 = ['lamp', 'glasses', 'zipper']
box_2 = ['dice', 'tie', 'scissors', 'magnet']
box_3 = []
box_4 = []
box_5 = ['vase', 'mountain', 'key']
box_6 = ['drum', 'skirt']
box_7 = ['usb', 'dolphin', 'pillow']
box_8 = ['tape', 'shorts']
box_9 = ['headphone']
box_10 = []
box_11 = ['octopus', 'branch']
box_12 = ['pants', 'shoe', 'bear']

box_9 = []
box_12.remove('shoe')
box_12.append('glove')
box_6.append('planet')
box_8.remove('tape')
box_8.append('shoe')
box_2.append('lamp')
box_11.remove('octopus')
box_11.remove('branch')
box_12.append('drum')
box_8.remove('shorts')
box_9.append('lock')
box_8.remove('shoe')
box_8.extend(['dress', 'tiger', 'snow'])
box_6.extend(['belt', 'dog', 'console'])
box_0.remove('candle')
box_0.append('zipper')
box_1.remove('zipper')
box_1.append('candle')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")