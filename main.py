import random
import string
import numpy as np
import cv2

# Crating the blank image to be used
blank_img = np.zeros([512, 1024, 1], dtype=np.uint8)
blank_img.fill(255)

# Generating random number/letter and getting its size to be aligned 
generated_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
string_font = cv2.FONT_HERSHEY_SIMPLEX
string_size = cv2.getTextSize(generated_string, string_font, 1, 2)[0]

# Setting the generated text -> image size
string_size_x = string_size[0]
string_size_y = string_size[1]

# Setting the X & Y positions of the generated text on the given image
text_x = int( (blank_img.shape[1] - string_size_x) / 2) 
text_y = int( (blank_img.shape[0] + string_size_y) / 2)

# Embedding the generated text into the image right in the center
cv2.putText(blank_img, generated_string, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Manipulating the image to confuse the CV models


cv2.imshow("Blank Image", blank_img)
cv2.waitKey(0)