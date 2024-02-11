import qrcode
import base64
from io import BytesIO

class QRcode():
    def __init__(self, link):
        self.link = link

    def GenerateCode(self):
        code = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )

        code.add_data(self.link)
        code.make(fit = True)
        image = code.make_image(fill_color = 'black', back_color = 'white')

        buffered = BytesIO()
        image.save(buffered)
        base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return base64_image
