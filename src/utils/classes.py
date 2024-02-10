import os
import qrcode

class QRcode():
    def __init__(self, link, fileName):
        self.link = link
        self.fileName = fileName
        self.directory = 'src/qrcodes'
        self.filePath = f'{self.directory}/{self.fileName}.png'

    def GenerateCode(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        code.add_data(self.link)
        code.make(fit=True)
        image = code.make_image(fill_color='black', back_color='white')
        image.save(self.filePath)
