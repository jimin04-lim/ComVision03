#01 Sobel edge
import cv2 as cv # OpenCV 라이브러리 임포트
import matplotlib.pyplot as plt # 시각화를 위한 Matplotlib 임포트

# 1. 이미지 로드 (edgeDetectionImage 대신 예시 파일명 사용)
img = cv.imread('edgeDetectionImage.jpg') # 이미지를 불러옴

# 2. 그레이스케일 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 이미지를 흑백으로 변환

# 3. Sobel 필터를 사용하여 x축과 y축 에지 검출
grad_x = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3) # x축 방향 미분 (3x3 커널)
grad_y = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3) # y축 방향 미분 (3x3 커널)

# 4. 에지 강도(Magnitude) 계산
mag = cv.magnitude(grad_x, grad_y) # x, y 미분값을 합쳐 에지 강도 계산

# 5. 시각화를 위해 uint8 타입으로 변환
sobel_final = cv.convertScaleAbs(mag) # 에지 강도를 8비트 이미지로 변환

# 6. Matplotlib 시각화
plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray'), plt.title('Original') # 원본 출력
plt.subplot(1, 2, 2), plt.imshow(sobel_final, cmap='gray'), plt.title('Sobel Edge') # 에지 출력
plt.show() # 화면에 표시