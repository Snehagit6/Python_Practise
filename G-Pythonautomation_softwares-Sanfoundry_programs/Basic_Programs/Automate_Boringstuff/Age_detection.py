import cv2
from deepface import DeepFace
result = DeepFace.analyze("C//Users//Sneha Mazumder//Pictures//Profile_Pic.jpg", actions=["age"])
print(result)
print(result['age'])
