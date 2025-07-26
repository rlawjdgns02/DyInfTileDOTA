from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Windows 지원
    
    model = YOLO('yolov8n.pt')
    results = model.train(
        data='dota.yaml',
        epochs=10,  # 테스트용으로 줄임
        imgsz=640,
        batch=16,
        device=0,
        workers=0
    )