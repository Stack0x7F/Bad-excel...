import time
import os
import sys
from src.excel_handler import ExcelRenderer
from src.video_processor import VideoProcessor
from src.audio_player import AudioPlayer

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    VIDEO_FILE = resource_path("assets/bad-apple.mp4")
    WIDTH, HEIGHT = 80, 60
    TARGET_FPS = 30

    if not os.path.exists(VIDEO_FILE):
        return

    renderer = ExcelRenderer(WIDTH, HEIGHT)
    video = VideoProcessor(VIDEO_FILE, WIDTH, HEIGHT)
    audio = AudioPlayer(VIDEO_FILE)

    time.sleep(1)
    audio.play()
    
    start_time = time.time()
    last_frame_idx = -1

    try:
        while True:
            if not renderer.is_alive():
                break

            ms = audio.get_pos_ms()
            current_time = ms / 1000.0 if ms >= 0 else (time.time() - start_time)
            target_frame_idx = int(current_time * TARGET_FPS)

            if target_frame_idx <= last_frame_idx:
                time.sleep(0.001)
                continue

            skip = target_frame_idx - last_frame_idx - 1
            if skip > 0:
                video.skip_frames(skip)

            frame_data = video.get_frame()
            if frame_data is None:
                break

            renderer.update_frame(frame_data)
            last_frame_idx = target_frame_idx

    except (KeyboardInterrupt, Exception):
        pass
    finally:
        audio.stop()
        video.release()
        try:
            renderer.stop()
        except:
            pass
        os._exit(0)

if __name__ == "__main__":
    main()
