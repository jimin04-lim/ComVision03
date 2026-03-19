# 03 GrabCut

import cv2 as cv # OpenCV 임포트
import numpy as np # 배열 처리를 위한 numpy 임포트
import matplotlib.pyplot as plt # 시각화 임포트

# 1. 이미지 로드 및 초기화
img = cv.imread('coffee cup.jpg') # 커피 이미지 로드
mask = np.zeros(img.shape[:2], np.uint8) # 이미지 크기의 마스크 생성
bgdModel = np.zeros((1, 65), np.float64) # 배경 모델 초기화
fgdModel = np.zeros((1, 65), np.float64) # 전경 모델 초기화

# 이미지 사이즈 확인
height = img.shape[0]                         
width = img.shape[1] 

# 2. 초기 사각형 설정 (x, y, w, h)
rect = (50, 50, width, height) # 추출하고 싶은 객체가 포함된 사각형 지정

# 3. GrabCut 실행
cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT) # 사각형 기반 분할 수행

# 4. 마스크 처리 (0: 배경, 2: 배경일 가능성 있는 곳을 0으로 처리)
# 1: 전경, 3: 전경일 가능성 있는 곳을 1로 처리
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8') # 배경은 0, 전경은 1로 변경

# 5. 배경 제거 이미지 생성
img_result = img * mask2[:, :, np.newaxis] # 원본에 마스크를 곱해 객체만 남김

# 6. 시각화
plt.subplot(1, 3, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original') # 원본
plt.subplot(1, 3, 2), plt.imshow(mask, cmap='gray'), plt.title('Mask') # 마스크
plt.subplot(1, 3, 3), plt.imshow(cv.cvtColor(img_result, cv.COLOR_BGR2RGB)), plt.title('Result') # 결과물
plt.show() # 출력