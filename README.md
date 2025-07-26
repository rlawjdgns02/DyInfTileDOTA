# DyInfTileDOTA
# DyInfTileDOTA

**Dynamic Inference for Tiled DOTA Object Detection**

고해상도 위성 이미지의 효율적인 객체 탐지를 위한 타일 기반 동적 추론 시스템

## 🎯 프로젝트 개요

위성 이미지와 같은 고해상도 이미지에서 **타일별 객체 존재 확률**을 예측하여, 확률이 낮은 타일에서는 연산을 건너뛰어 **inference 속도를 향상**시키는 연구입니다.

### 핵심 아이디어
- 고해상도 이미지를 타일로 분할
- 각 타일에 대해 객체 존재 확률 예측
- 확률이 임계값 이하인 타일은 객체 탐지 연산 스킵
- 전체적인 inference 시간 단축

## 🚀 현재 진행 상황

### ✅ 완료된 작업
- [x] YOLOv8 환경 설정
- [x] DOTA 데이터셋 YOLO 형식 변환
- [x] 기본 YOLOv8 모델로 DOTA 학습 테스트

### 🔄 다음 단계
- [ ] 타일 확률 예측 헤더 설계
- [ ] YOLOv8 모델 구조 수정
- [ ] 멀티 태스크 손실 함수 구현
- [ ] 동적 추론 파이프라인 구현

## 🛠 기술 스택

- **Deep Learning Framework**: PyTorch
- **Object Detection**: YOLOv8 (Ultralytics)
- **Dataset**: DOTA (Dataset for Object Detection in Aerial Images)
- **Language**: Python 3.11

## 📊 예상 효과

- **기존 방식**: 모든 타일에 대해 객체 탐지 수행
- **제안 방식**: 확률 기반 선택적 객체 탐지
- **목표**: 정확도 유지하면서 **30-50% inference 시간 단축**

---

*학부생 실습 프로젝트 - 고해상도 이미지 처리의 효율성 향상*