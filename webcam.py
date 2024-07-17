# 2분으로 바꾸고 웹캠으로 바꿔서 사용
from flask import Flask, render_template, Response
import cv2
import threading
import os
import time

app = Flask(__name__)

# 비디오 저장 디렉토리 설정
SAVE_DIR = "video_outputs"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

started = False
recording = False
frame = None

def save_video():
    global out, frame, recording
    while True:
        if recording:
            timestamp = int(time.time())
            filename = os.path.join(SAVE_DIR, f'output_{timestamp}.avi')
            out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640, 480))

            print(f"Started recording to {filename}")
            start_time = time.time()
            frame_count = 0

            while recording and time.time() - start_time < 120:  # 2분 동안 기록
                if frame is not None:
                    out.write(frame)
                    frame_count += 1
                # 정확한 프레임 레이트 유지
                time.sleep(max(0, (1/30) - (time.time() - start_time - frame_count/30)))

            out.release()
            out = None
            print(f"Finished recording to {filename}")

video_thread = threading.Thread(target=save_video)
video_thread.start()

def generate_frames():
    global frame, started, recording
    cap = cv2.VideoCapture(0)

    try:
        while True:
            if not started:
                time.sleep(0.1)
                continue

            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                continue

            # 컬러 이미지를 JPEG 포맷으로 인코딩
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                print("Failed to encode frame")
                continue

            jpg_frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpg_frame + b'\r\n\r\n')
    except Exception as e:
        print(f"Exception during frame generation: {e}")
    finally:
        cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        started = True
        recording = True
        print("Camera started successfully")
        app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    except Exception as e:
        print(f"Camera initialization error: {e}")
    finally:
        recording = False
