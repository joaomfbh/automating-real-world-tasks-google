from PIL import Image
import glob
import os

def process_images(src_files, dst_path):
    source_files = src_files
    destination_path = dst_path
    for image in source_files:
        with Image.open(image) as img:
            filename, format, size = img.filename, img.format, img.size
            print(f"Processing image {filename} with {format} format and {size} size")
            rt, rs = -90, (128, 128)
            try:
                if img.mode != "RGB":
                    if format == "TIFF":
                       img = img.convert("RGB")
                       img.rotate(rt).resize(rs).save(os.path.join(destination_path, filename.split("/")[1] + ".jpeg"))
                       print("Completed")
            except Exception as e:
                print(f"Fail to process the image {filename}. Reason: {e}")
    return

if __name__ == "__main__":
    # Call function process_images
    process_images(glob.glob("images/*"), "/opt/icons")
    
