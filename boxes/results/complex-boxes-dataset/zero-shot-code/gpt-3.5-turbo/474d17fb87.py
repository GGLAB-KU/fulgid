box_0 = ['sock', 'lipstick', 'speaker', 'shoes']
box_1 = ['pan', 'basket', 'violin', 'rock']
box_2 = ['umbrella', 'microscope', 'jacket']
box_3 = ['telescope', 'usb', 'pot', 'harmonica']
box_4 = ['phone', 'makeup', 'sandals', 'oven', 'bracelet']
box_5 = ['comet']
box_6 = ['butterfly', 'cup', 'starfish', 'dice', 'skirt']
box_7 = ['seaweed', 'desert', 'island', 'laptop']
box_8 = ['moon', 'wallet', 'truck', 'tree', 'rain']
box_9 = ['submarine', 'drum', 'boat']
box_10 = ['shampoo', 'plane', 'brush', 'game', 'perfume']
box_11 = ['lock', 'coin', 'storm']
box_12 = []
box_13 = ['helmet', 'comb', 'apple', 'elephant']
box_14 = ['thread', 'polish', 'bag']

box_6.remove('starfish')
box_6.remove('cup')
box_3.remove('harmonica')
box_3.remove('telescope')
box_13.remove('apple')
box_13.remove('comb')
box_10.remove('shampoo')
box_10.remove('perfume')
box_10.remove('plane')
box_14.remove('polish')
box_2.remove('umbrella')
box_2.append('polish')
box_3.remove('usb')
box_2.append('usb')
box_0.remove('shoes')
box_7.remove('desert')
box_0.append('desert')
box_6.remove('butterfly')
box_6.remove('skirt')
box_6.remove('dice')
box_9.remove('drum')
box_2.remove('microscope')
box_9.append('microscope')
box_3.remove('pot')
box_3.append('scarf')
box_5.extend(['boot', 'blender', 'bowl'])
box_1.remove('basket')
box_1.remove('rock')
box_0.remove('lipstick')
box_0.append('glasses')
box_14.remove('thread')
box_8.remove('tree')
box_14.append('tree')
box_2.remove('jacket')
box_1.extend(['drum', 'jacket', 'polish'])
box_14.remove('bag')
box_14.remove('umbrella')
box_14.remove('tree')
box_3.remove('scarf')
box_5.append('scarf')
box_1.extend(['ocean', 'glove', 'necklace'])
box_10.remove('game')
box_10.remove('brush')
box_9.remove('submarine')
box_9.append('lipstick')
box_6.append('charger')
box_14.extend(['bag', 'bird', 'moon'])

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")