from ultralytics import YOLO
 
 
model = YOLO('/home/mjy/ultralytics/yaml/yolov8n-obb.yaml').load('/home/mjy/ultralytics/runs/obb/train/weights/best.pt')  # build from YAML and transfer weights

# Train the model
#results = model.train(data='/home/mjy/ultralytics/coco8.yaml', epochs=100, imgsz=640,resume=False)
metrics = model.val(data='/home/mjy/ultralytics/coco8.yaml',imgsz=640)