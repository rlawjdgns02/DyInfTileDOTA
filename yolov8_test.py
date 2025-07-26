from ultralytics import YOLO

# 테스트용 모델 다운로드 (자동으로 다운됨)
model = YOLO('yolov8n.pt')

print("YOLOv8 설치 완료!")

results = model('https://ultralytics.com/images/bus.jpg')
results[0].show()