import base64
import xmlrpc.client as client

def photo(image):
        uploaded_file = image
        BinaryImage = client.Binary(uploaded_file.read())
        BytesImage = BinaryImage.data
        ImageBase64 = base64.b64encode(BytesImage)
        ImageSend = ImageBase64.decode('ascii')
        return ImageSend