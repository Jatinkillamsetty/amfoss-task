import pytesseract
from PIL import Image
import re

# Image path
image_path = "/home/jatin-killamsetty/jatin python visual code/jatin.png"

# Open the image
img = Image.open(image_path)

# Extract text using Tesseract OCR
extracted_text = pytesseract.image_to_string(img).strip()
print(f"Extracted Text: '{extracted_text}'")

# Define a regex pattern to find the numbers and operator
pattern = re.compile(r"(\d+)\s*([+\-*/])\s*(\d+)")

# Match the pattern in the extracted text
match = pattern.search(extracted_text)

if match:
    num1, operator, num2 = match.groups()
    num1, num2 = int(num1), int(num2)

    # Perform the operation based on the operator
    if operator == '+':
        result = num1 + num2
    

    print(f"Result: {result}")
