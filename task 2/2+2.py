import pytesseract
from PIL import Image
import re

# Image path
image_path = "/home/jatin-killamsetty/jatin python visual code/jatin.png"
img = Image.open(image_path)
extracted_text = pytesseract.image_to_string(img).strip()
print(f"Extracted Text: '{extracted_text}'")
pattern = re.compile(r"(\d+)\s*([+\-*/])\s*(\d+)")
match = pattern.search(extracted_text)

if match:
    num1, operator, num2 = match.groups()
    num1, num2 = int(num1), int(num2)
    if operator == '+':
        result = num1 + num2
    

    print(f"Result: {result}")
