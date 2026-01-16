import cv2

class VideoProcessor:
    def __init__(self, video_path, width, height):
        self.cap = cv2.VideoCapture(video_path)
        self.width = width
        self.height = height

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (self.width, self.height), interpolation=cv2.INTER_NEAREST)
        _, binary = cv2.threshold(resized, 127, 1, cv2.THRESH_BINARY_INV)
        return binary.astype(int).tolist()

    def skip_frames(self, count):
        for _ in range(count):
            self.cap.grab()

    def release(self):
        self.cap.release()
