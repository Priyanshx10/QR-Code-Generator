 **QR Code Generator in Python**

This Python script generates a QR code image for a given URL using the `qrcode` and `PIL` libraries. The generated QR code is saved as a PNG image file.

**Step-by-Step Explanation:**

1. **Importing the Required Libraries**:
   ```python
   import qrcode
   from PIL import Image
   ```
   - We import the `qrcode` library to generate the QR code and the `PIL` (Python Imaging Library) to save the QR code as an image.

2. **Creating the QR Code Object**:
   ```python
   qr = qrcode.QRCode(version=1,
                      error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=10,
                      border=4,)
   ```
   - We create a `QRCode` object using the `qrcode.QRCode()` function.
   - The `version` parameter specifies the version of the QR code. A higher version can hold more data but results in a larger QR code.
   - The `error_correction` parameter specifies the level of error correction. A higher level of error correction allows the QR code to be reconstructed even if some parts are damaged.
   - The `box_size` parameter specifies the size of each QR code module in pixels.
   - The `border` parameter specifies the width of the border around the QR code in pixels.

3. **Adding Data to the QR Code**:
   ```python
   qr.add_data("https://www.w3schools.com/")
   ```
   - We use the `add_data()` method to add the URL to the QR code.

4. **Making the QR Code**:
   ```python
   qr.make(fit=True)
   ```
   - We use the `make()` method to generate the QR code.
   - The `fit=True` parameter ensures that the QR code fits within the specified size.

5. **Creating the QR Code Image**:
   ```python
   img = qr.make_image(fill_color="red", back_color="blue")
   ```
   - We use the `make_image()` method to create the QR code image.
   - The `fill_color` parameter specifies the color of the QR code modules.
   - The `back_color` parameter specifies the

