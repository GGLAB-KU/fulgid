box_0 = []
box_1 = []
box_2 = ['chair', 'bracelet', 'usb']
box_3 = ['comb', 'watch', 'meteor', 'earring']
box_4 = ['cup', 'car']
box_5 = ['frame']
box_6 = []
box_7 = []
box_8 = []
box_9 = ['dog', 'scissors']
box_10 = ['submarine', 'mask', 'piano']
box_11 = ['charger', 'ocean']
box_12 = []

box_11.remove('rock')
box_11.remove('lamp')
box_11.extend(['charger', 'ocean'])
box_4.remove('dolphin')
box_4.append('bicycle')
box_2.extend(['helmet', 'moon'])
box_6.remove('bird')
box_6.append('clock')
box_5.append('frame')
box_11.remove('ocean')
box_3.append('ocean')
box_2.remove('moon')
box_2.append('horn')
box_11.append('bicycle')
box_4.extend(['blanket', 'dress', 'dog'])
box_5.remove('candle')
box_5.remove('tie')
box_5.remove('grinder')
box_5.extend(['pants', 'basket', 'jungle'])
box_5.remove('pants')
box_5.append('earring')
box_5.append('grinder')
box_6.remove('dice')
box_6.remove('doll')
box_1.extend(['dice', 'doll'])
box_6.clear()
box_1.clear()
box_4.remove('dress')
box_4.remove('blanket')
box_4.remove('rain')
box_4.extend(['lightning', 'microscope', 'butterfly'])
box_10.remove('fridge')
box_3.remove('earring')
box_7.extend(['watch', 'thread'])

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")