import json
import os
import base64

notebook_path = "recipe_analysis.ipynb"
output_dir = "extracted_images"
os.makedirs(output_dir, exist_ok=True)

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

image_count = 0
for cell in nb.get('cells', []):
    # Only look at code cells with outputs
    if cell.get('cell_type') == 'code' and 'outputs' in cell:
        for output in cell['outputs']:
            # Check if output contains image data in 'image/png' format
            if 'data' in output and 'image/png' in output['data']:
                image_data = output['data']['image/png']
                # If list of strings, join them
                if isinstance(image_data, list):
                    image_data = ''.join(image_data)
                # Decode base64 string
                img_bytes = base64.b64decode(image_data)
                # Save to file
                image_count += 1
                img_filename = os.path.join(output_dir, f"image_{image_count}.png")
                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_bytes)
                print(f"Saved {img_filename}")

print(f"Extracted {image_count} images.")
