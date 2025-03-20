import qrcode

data = 'Porashuna bhalo lagena'
img = qrcode.make(data)
img.save('E:/Python/Pycharm/myqr.png')

