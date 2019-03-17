import cv2
import time
import base64
import hashlib

i = 1
while i < 1000:
    cap = cv2.VideoCapture(0)
    time.sleep(2)
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('frame', rgb)
    cv2.imwrite('capture.jpg', frame)
    cap.release()
    cv2.destroyAllWindows()

    with open('capture.jpg', 'rb') as imageFile:
        nonce = base64.b64encode(imageFile.read())
        hash_object = hashlib.sha512(nonce)
        hash_digest = hash_object.hexdigest()
        print("Hash: " + hash_digest)       
        f = open('hashes.txt','a')
        f.write(hash_digest + "\n")
        f.close()
    time.sleep(5)
    i += 1