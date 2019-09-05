from PIL import Image
from StringIO import StringIO

@app.route('/image')
def genere_image():
    mon_image = StringIO()
    Image.new("RGB", (300,300), "#92C41D").save(mon_image, 'BMP')
    return mon_image.getvalue()
