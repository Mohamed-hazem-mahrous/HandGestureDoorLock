import cv2
import mediapipe as mp
import time



class HandDetector():
    def __init__(self, mode = False, maxHands = 2, model_complexity=1,
                 detectioncon = 0.5, trackcon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectioncon = detectioncon
        self.trackcon = trackcon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode ,self.maxHands ,self.model_complexity ,self.detectioncon ,self.trackcon)
        self.mpDraw = mp.solutions.drawing_utils

    def finhands(self, img, draw = True):
        imgRGB = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print (results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for HandLMS in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, HandLMS, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo = 0, draw = True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myhand.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                lmlist.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        return lmlist

    def numbhands(self, img):
        num_hands = 0
        if self.results.multi_hand_landmarks:
            num_hands = len(self.results.multi_hand_landmarks)
        return num_hands
    

    def get_up_fingers(self, img,handNo=0):
        fingers = []
        self.tipids = [4, 8, 12, 16, 20]

        lmlist = self.findPosition(img, draw=False, handNo=0)
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]
            # Thumb
            if lmlist[self.tipids[0]][1] > lmlist[self.tipids[4] - 1][1]:
                if lmlist[self.tipids[0]][1] > lmlist[self.tipids[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if lmlist[self.tipids[0]][1] < lmlist[self.tipids[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)     
            
            # Rest of the fingers
            for id in range(1, 5):
                if myhand.landmark[self.tipids[id]].y < myhand.landmark[self.tipids[id] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers








def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        img = detector.finhands(img)
        lmlist = detector.findPosition(img)

        if len(lmlist) != 0:
            print(lmlist[0])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        # Check for the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 






if __name__ == "__main__":
    main()














