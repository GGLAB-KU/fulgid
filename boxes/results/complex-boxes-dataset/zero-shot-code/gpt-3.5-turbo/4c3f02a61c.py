box_0 = ['bird', 'umbrella']
box_1 = ['violin', 'towel', 'beach']
box_2 = ['desert', 'glasses', 'submarine', 'coral']
box_3 = ['swimsuit', 'zipper']
box_4 = ['plate', 'thunder', 'glove']
box_5 = ['toaster']
box_6 = ['bag', 'tape']
box_7 = ['piano', 'wallet']
box_8 = ['microscope', 'jacket', 'rock', 'mask', 'cloud']
box_9 = ['shelf', 'butterfly', 'clock', 'paint']
box_10 = ['candle', 'harmonica', 'shark']
box_11 = ['whistle']
box_12 = ['sculpture', 'brush', 'grass', 'guitar']
box_13 = ['bus', 'sock']
box_14 = ['usb']

box_14 = ['scarf']
box_9 = ['grass']
box_11.append('leaf')
box_12.remove('sculpture')
box_12.extend(['needle', 'charger', 'grass'])
box_13.append('wallet')
box_6.remove('scarf')
box_14.remove('bag')
box_14.append('toaster')
box_12.remove('brush')
box_8.remove('cloud')
box_8.remove('mask')
box_8.remove('jacket')
box_12.extend(['battery', 'charger', 'grass'])
box_7.extend(['wallet', 'cloud', 'lightning'])
box_4.remove('microscope')
box_4.remove('thunder')
box_4.remove('glove')
box_12.remove('butterfly')
box_12.remove('needle')
box_12.remove('charger')
box_12.extend(['bus', 'soap', 'umbrella'])
box_1.remove('beach')
box_0.remove('umbrella')
box_14.extend(['ocean', 'cat', 'vase'])
box_12.append('tiger')
box_1.extend(['card', 'shoe', 'usb'])
box_13.remove('microscope')
box_13.remove('thunder')
box_13.remove('glove')
box_7.remove('wallet')
box_7.append('cloud')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")