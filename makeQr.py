"""for terminql code --> pip install qrcode"""

import qrcode

image = qrcode.make('https://pypi.org/project/qrcode/')

image.save("PipInstall.jpg")