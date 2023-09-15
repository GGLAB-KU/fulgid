box_0 = ['toothbrush', 'helmet', 'lion']
box_1 = ['shelf']
box_2 = ['charger', 'rocket', 'frame', 'toothpaste', 'clock']
box_3 = ['submarine', 'cloud']
box_4 = ['tiger', 'coin', 'rain', 'boot', 'telescope']
box_5 = []
box_6 = ['river']
box_7 = ['belt', 'dress', 'star']
box_8 = ['wig', 'starfish', 'mixer', 'microscope', 'mask']
box_9 = ['swimsuit', 'flower', 'lock', 'shorts', 'speaker']
box_10 = ['umbrella', 'camera', 'fish']
box_11 = ['glove', 'beach', 'shark']
box_12 = ['cup']

def move_items():
    box_4.extend([box_7.pop(box_7.index('belt')), box_7.pop(box_7.index('dress')), box_7.pop(box_7.index('star'))])
    box_6.remove('river')
    box_10.remove('camera')
    box_10.remove('umbrella')
    box_7.extend(['shorts', 'note', 'tie', 'coral'])
    box_4[box_4.index('boot')], box_10[box_10.index('fish')] = box_10[box_10.index('fish')], box_4[box_4.index('boot')]
    box_7.remove('coral')
    box_7.remove('note')
    box_7.remove('shorts')
    box_8.remove('wig')
    box_8.remove('microscope')
    box_12[box_12.index('cup')], box_11[box_11.index('glove')] = box_11[box_11.index('glove')], box_12[box_12.index('cup')]
    box_0.extend([box_12.pop(box_12.index('toothbrush')), box_12.pop(box_12.index('helmet'))])
    box_4.remove('rain')
    box_4.remove('telescope')
    box_0.extend(['brush', 'paint', 'razor'])
    box_4.extend(['shark', 'shelf'])
    box_1.remove('shelf')
    box_11.append('shelf')
    box_7[box_7.index('tie')] = 'tree'
    box_8.extend([box_11.pop(box_11.index('beach')), box_11.pop(box_11.index('shelf'))])
    box_11.extend([box_0.pop(box_0.index('lion')), box_0.pop(box_0.index('paint')), box_0.pop(box_0.index('brush'))])
    box_10.append('laptop')
    box_9[box_9.index('flower')], box_4[box_4.index('tiger')] = box_4[box_4.index('tiger')], box_9[box_9.index('flower')]

def print_boxes():
    for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
        print(f"Box {i}: {box}")

move_items()
print_boxes()