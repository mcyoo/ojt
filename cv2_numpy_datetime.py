import cv2
import datetime
import time
import numpy as np
import os

# 폴더 생성 함수


def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print('폴더 생성 에러' + path)


def video_run():
    try:
        print("카메라 구동")
        cap = cv2.VideoCapture(0)
    except:
        print("카메라 구동실패")
        return

    # 윈도우 사이즈 조절
    cv2.namedWindow('ojt_2', flags=cv2.WINDOW_NORMAL)

    prev_time = 0
    while (True):
        ret, frame = cap.read()

        if not ret:
            print("비디오 읽기 오류")
            continue

        cur_time = time.time()
        sec = cur_time - prev_time
        prev_time = cur_time
        fps = 1/(sec)
        str_fps = f"FPS : %0.1f" % fps

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey_3 = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)

        # 상단 컬러, 하단 흑백
        combine_frame = np.concatenate((frame, grey_3), axis=0)

        # FPS 표시
        cv2.putText(combine_frame, str_fps, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))

        # 화면 표시
        cv2.imshow('ojt_2', combine_frame)

        k = cv2.waitKey(1)
        # q 누르면 종료
        if (k == 113):
            print('종료')
            break
        # s 누르면 캡쳐
        elif (k == 115):
            print("캡쳐")
            # image_20220831T112132.png 파일명으로 저장
            now = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
            # 캡처 화면 854x900 으로 저장
            combine_frame = cv2.resize(combine_frame, (854, 900))
            create_folder('images')
            cv2.imwrite("images/image_" + now + ".png", combine_frame)

    cap.release()
    cv2.destroyAllWindows()


video_run()
