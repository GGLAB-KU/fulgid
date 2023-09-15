box_0 = ['makeup', 'cup', 'usb', 'dog', 'button']
box_1 = ['table', 'belt']
box_2 = ['island', 'note', 'tiger', 'sculpture']
box_3 = ['wig', 'coral', 'lock', 'tie']
box_4 = ['butterfly', 'bird']
box_5 = ['comb', 'boot']
box_6 = []
box_7 = ['mixer', 'phone', 'ocean', 'cat', 'swimsuit']
box_8 = ['mask']
box_9 = ['candle', 'needle', 'battery', 'fish']
box_10 = ['soap', 'river', 'rocket', 'controller', 'starfish']
box_11 = ['brush']
box_12 = []

box_9 = []
box_4.remove('butterfly')
box_4.remove('bird')
box_9.append('guitar')
box_7[box_7.index('swimsuit')], box_8[0] = box_8[0], box_7[box_7.index('swimsuit')]
box_0[box_0.index('button')], box_2[box_2.index('note')] = box_2[box_2.index('note')], box_0[box_0.index('button')]
box_2[box_2.index('sculpture')] = 'fork'
box_3[box_3.index('coral')], box_0[box_0.index('usb')] = box_0[box_0.index('usb')], box_3[box_3.index('coral')]
box_4.extend(['soap', 'starfish', 'controller'])
box_4.remove('soap')
box_4.remove('starfish')
box_10.append('swimsuit')
box_7[box_7.index('phone')], box_3[box_3.index('ocean')] = box_3[box_3.index('ocean')], box_7[box_7.index('phone')]
box_2[box_2.index('fork')], box_9[0] = box_9[0], box_2[box_2.index('fork')]
box_4.remove('controller')
box_5.append('controller')
box_1.extend(['makeup', 'note'])
box_7[box_7.index('mixer')], box_7[box_7.index('phone')] = box_7[box_7.index('phone')], box_7[box_7.index('mixer')]
box_3 = []
box_7[box_7.index('cat')], box_9[0] = box_9[0], box_7[box_7.index('cat')]
box_9 = []
box_12.extend(['tiger', 'island', 'button'])
box_1 = []