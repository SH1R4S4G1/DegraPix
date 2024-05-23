import random
from PIL import Image

def analyze_jpeg(image_path):
    with open(image_path, 'rb') as file:
        data = bytearray(file.read())
    markers = {
        'SOI': data.find(bytes([0xFF, 0xD8])),  # Start of Image
        'EOI': data.find(bytes([0xFF, 0xD9])),  # End of Image
        'SOS': data.find(bytes([0xFF, 0xDA]))   # Start of Scan
    }
    return markers

def corrupt_jpeg_data(image_path, output_path, start, end, num_bytes_to_corrupt):
    with open(image_path, 'rb') as f:
        img_data = bytearray(f.read())
    for _ in range(num_bytes_to_corrupt):
        position = random.randint(start, end - 1)
        img_data[position] = random.randint(0, 255)
    with open(output_path, 'wb') as f:
        f.write(img_data)
    return output_path

def apply_compression(image, output_path, quality):
    image.save(output_path, 'JPEG', quality=quality)
    return output_path

def apply_resize_with_restore(image, output_path, scale_factor, iterations):
    original_size = image.size
    for _ in range(iterations):
        new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        image = image.resize(new_size, Image.LANCZOS)
        image = image.resize(original_size, Image.LANCZOS)
    image.save(output_path)
    return output_path

# 元の画像を読み込み
image_path = '/PATH/TO/YOUR/IMAGE.jpg'
output_path = '/PATH/TO/YOUR/final_output.jpg'
img = Image.open(image_path)

# 圧縮劣化を適用
if input("Apply compression degradation? (Y/N): ").lower() == 'y':
    quality = int(input("Enter compression quality (1-100, lower is more degraded): "))
    image_path = apply_compression(img, output_path, quality)
    img = Image.open(image_path)

# リサイズによる劣化を適用
if input("Apply resize with restoration degradation? (Y/N): ").lower() == 'y':
    scale_factor = float(input("Enter the scale factor for resizing (e.g., 0.5 for half size): "))
    iterations = int(input("How many times should the resize process be repeated? "))
    image_path = apply_resize_with_restore(img, output_path, scale_factor, iterations)
    img = Image.open(image_path)

# ノイズを加える前にJPEGファイルの構造を再分析
jpeg_markers = analyze_jpeg(image_path)

# ノイズを加える
if input("Apply noise corruption? (Y/N): ").lower() == 'y':
    num_bytes_to_corrupt = int(input("Enter the amount of bytes to corrupt: "))
    image_path = corrupt_jpeg_data(image_path, output_path, jpeg_markers['SOS'], jpeg_markers['EOI'], num_bytes_to_corrupt)

# 結果の表示
from IPython.display import Image, display
display(Image(filename=image_path))
