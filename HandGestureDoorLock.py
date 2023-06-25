import cv2
import time
import HandTrackingModule as htm
from collections import Counter, OrderedDict

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

cTime, pTime = 0, 0


detector = htm.HandDetector(detectioncon=0.75)

tipids = [4, 8, 12, 16, 20]


totalfingers = -1
fing0 = [0, 0, 0, 0, 0]

fing1 = [0, 1, 0, 0, 0]

fing2 = [0, 1, 1, 0, 0]

fing3 = [1, 1, 1, 0, 0]

fing4 = [0, 1, 1, 1, 1]

fing5 = [1, 1, 1, 1, 1]

fing6 = [0, 1, 1, 1, 0]

fing7 = [0, 1, 1, 0, 1]

fing8 = [0, 1, 0, 1, 1]

fing9 = [0, 0, 1, 1, 1]

fing10 = [1, 1, 0, 0, 0]


unlocked = []

password = [5, 3, 9, 4]

door_unlocked = False

while True:
    if totalfingers == 10:
        totalfingers = -1
        unlocked = []
        continue
    success , img = cap.read()

    img = detector.finhands(img)
    num_hands = detector.numbhands(img)


    # print(lmlist)
    if num_hands == 1:
        lmlist = detector.findPosition(img, draw=False, handNo=0)
        if len(lmlist) != 0:
            fingers = []

            fingers = detector.get_up_fingers(img=img)
            # print("Fingers Up:", fingers)


            if fingers == fing0:
                totalfingers = 0
                unlocked.append(0)

            elif fingers == fing1:
                totalfingers = 1
                unlocked.append(1)

            elif fingers == fing2:
                totalfingers = 2
                unlocked.append(2)

            elif fingers == fing3:
                totalfingers = 3
                unlocked.append(3)

            elif fingers == fing4:
                totalfingers = 4
                unlocked.append(4)

            elif fingers == fing5:
                totalfingers = 5
                unlocked.append(5)

            elif fingers == fing6:
                totalfingers = 6
                unlocked.append(6)

            elif fingers == fing7:
                totalfingers = 7
                unlocked.append(7)

            elif fingers == fing8:
                totalfingers = 8
                unlocked.append(8)

            elif fingers == fing9:
                totalfingers = 9
                unlocked.append(9)

            elif fingers == fing10:
                totalfingers = 10

            else:
                totalfingers = -1

            def get_most_frequent_numbers(input_list, num_numbers):
                counter = Counter(input_list)
                ordered_counter = OrderedDict(counter.most_common())
                selected_numbers = []
                for num in input_list:
                    if num in ordered_counter and ordered_counter[num] > 1 and num not in selected_numbers:
                        selected_numbers.append(num)
                        if len(selected_numbers) == num_numbers:
                            break
                return selected_numbers
            
            num_numbers = 4
            list2 = get_most_frequent_numbers(unlocked, num_numbers)

            print(list2)

            if list2 == password:
               door_unlocked = True
               print(door_unlocked)


            if door_unlocked:
                break

            cv2.rectangle(img, (20, 20), (150, 80), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(totalfingers), (45, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 10)


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