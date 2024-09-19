import cv2

class ImageCapture():
    def __init__(self, camera_id=0, width=480, height=640):
        self.cap = cv2.VideoCapture(camera_id)
        self.cap.set(3, width)
        self.cap.set(4, height)

    def capture(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None
    
    def capture_and_show(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.release()

    def release(self):
        self.cap.release()

    def close(self):
        self.release()
        cv2.destroyAllWindows()
