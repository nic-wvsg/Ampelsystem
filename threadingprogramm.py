import threading
import subprocess

def run_yolo():
    subprocess.Popen(["python3", "YOLO2.py"])

def run_ampelschaltung():
    subprocess.Popen(["python3", "Ampelschaltung.py"])

yolo_thread = threading.Thread(target=run_yolo)
ampel_thread = threading.Thread(target=run_ampelschaltung)

yolo_thread.start()
ampel_thread.start()

yolo_thread.join()
ampel_thread.join()
