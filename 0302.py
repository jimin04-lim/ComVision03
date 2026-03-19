#02 Canny edge & HoughtLine

import cv2 as cv # OpenCV 라이브러리 임포트
import numpy as np # 행렬 연산을 위한 numpy 임포트
import matplotlib.pyplot as plt # 시각화 임포트

# 1. 이미지 로드 및 에지 맵 생성
img = cv.imread('dabo.jpg') # 이미지 로드
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 그레이스케일 변환
edges = cv.Canny(gray, 100, 200) # 하단 임계값 100, 상단 임계값 200으로 에지 검출

# 2. 허프 변환을 이용한 직선 검출
# rho=1, theta=pi/180, threshold=100, minLineLength=50, maxLineGap=10
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10) # 확률적 허프 변환 수행

# 3. 검출된 직선을 원본 이미지에 그리기
img_line = img.copy() # 원본 복사본 생성
if lines is not None: # 직선이 검출되었다면
    for line in lines: # 각 직선에 대해 반복
        x1, y1, x2, y2 = line[0] # 시작점과 끝점 좌표 추출
        cv.line(img_line, (x1, y1), (x2, y2), (0, 0, 255), 2) # 빨간색(BGR), 두께 2로 그리기

# 4. 시각화
plt.subplot(1, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original') # 원본
plt.subplot(1, 2, 2), plt.imshow(cv.cvtColor(img_line, cv.COLOR_BGR2RGB)), plt.title('Hough Lines') # 직선 검출 결과
plt.show() # 출력