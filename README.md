# ComVision 03주차 실습
# OpenCV 실습 과제

## 0301. 소벨 에지 검출 및 결과 시각화
- **설명**:
  - edgeDetectionImage를 그레이스케일로 변화
  - Sobel 필터를 사용하여 x축과 y축 방향의 에지 검출
  - 검출된 에지 강도 이미지를 시각화
- **요구사항**:
  - cv.imread()              :이미지 로드
  - cv.cvtColor()            :이미지를 그레이스케일로 변환
  - cvSobel()                :x축(cv.CV_64F, 1, 0)과 y축(cv.CV_64F, 0,1) 방향의 에지 검출
    - ksize는 3 또는 5
  - cv.magnitude()           :에지 강도 계산
  - Matplotlib               :원본 이미지와 에지 강도 이미지를 나란히 시각화
  - cv.convertScaleAbs()     :에지 강도 이미지를 uint8로 변환
  - plt.imshow()             :시각화
    - cmap='gray'를 사용하여 흑백으로 시각화
- **코드**
  ```python
  import cv2 as cv # OpenCV 라이브러리 임포트
  import matplotlib.pyplot as plt # 시각화를 위한 Matplotlib 임포트
  
  # 1. 이미지 로드 (edgeDetectionImage 대신 예시 파일명 사용)
  img = cv.imread('soccer.jpg') # 이미지를 불러옴
  
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
  ```
- **주요코드**
  ```python
  cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3): x축 방향으로 기울기(미분값)를 계산
  cv.magnitude(grad_x, grad_y)            : 검출된 x, y축 에지를 통합하여 전체 에지 세기를 구함
  cv.convertScaleAbs(mag)                 : 계산된 실수형 에지 강도를 화면 표시가 가능한 양수 정수 형태로 변환함
  ```
- **결과물**:
<img width="1272" height="1068" alt="image" src="https://github.com/user-attachments/assets/69a0f840-701c-463c-b566-1fd06b1f9705" />



## 0302. 캐니 에지 및 허프 변환을 이용하여 직선 검출
- **설명**:
 - dabo 이미지에 캐니 에지 검출을 사용하여 에지 맵 생성
 - 허프 변환을 사용하여 이미지에서 직선 검출
 - 검출된 직선을 원본 이미지에서 빨간색으로 표시
- **요구사항**:
  - cv.Canny()        :에지 맵 생성
    - threshold1 = 100, threshold2 = 200
  - cv.HoughLinesP()  :직선 검출
    - rho, theta, threshold, minLineLength, maxLineGap 값 조정
  - cv.line()         :검출된 직선을 원본 이미지에 그림
    - 빨간색(0,0,255)과 두께는 2로 설정
  - Matplotlib를 사용하여 원본 이미지와 직선이 그려진 이미지를 나란히 시각화
- **코드**
  ```python
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
  ```
- **주요코드**
  ```python
  cv.Canny(gray, 100, 200)            : 두 개의 임계값을 사용하여 노이즈를 제거하고 정교한 에지만 추출
  cv.HoughLinesP(...)                 : 에지 픽셀들을 모아 실제 직선의 방정식을 만족하는 선분 좌표를 검출
  cv.line(img_line, ..., (0,0,255), 2): 찾아낸 좌표를 따라 원본에 빨간색 선을 그림
  ```
- **결과물**:
<img width="1259" height="1076" alt="image" src="https://github.com/user-attachments/assets/62aaa616-39a7-4b18-b79e-473e4eda4953" />



## 0303. GrabCut을 이용한 대화식 영역 분할 및 객체 추
- **설명**:
  - coffee cup 이미지로 사용자가 지정한 사각형 영역을 바탕으로 GrabCut 알고리즘을 통한 객체 추출
  - 객체 추출 결과를 마스크 형태로 시각화
  - 원본 이미지에서 배경 제거 및 객체만 남은 이미지 출력
- **요구사항**:
  - cv.grabCut():대화식 분할 수행
    - bgdModel과 fgdModel은 np.zeros((1,65),np.float64)로 초기화
  - 초기 사각형 영역은 (x,y,width,height) 형식으로 설정
  - 마스크를 사용하여 원본 이미지에서 배경 제거
    - cv.GC_BGD,cv.GC_FGD,cv.GC_PR_BGD,cv.GC_PR_FGD를 사용
  - np.where()로 마스크 값을 0 혹은 1로 변경 후 원본 이미지에 곱해 배경 제거
  - Matplotlib를 사용하여 원본 이미지, 마스크 이미지, 배경 제거 이미지 세 개를 나란히 시각화

- **코드**
  ```python
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
  ```
- **주요코드**
  ```python
  cv.grabCut(..., cv.GC_INIT_WITH_RECT): 사용자가 지정한 사각형 내부에서 객체와 배경의 경계를 검출
  np.where(...)                        : GrabCut 결과 마스크에서 확실한 전경과 전경일 확률이 높은 부분만 골라내어 배경을 분리
  img * mask2[:, :, np.newaxis]        : 원본 픽셀에 0(배경) 또는 1(전경)을 곱해 배경 부분을 검게 지움
  ```
- **결과물**:
<img width="1480" height="1130" alt="image" src="https://github.com/user-attachments/assets/56f16d29-b0a3-406d-8818-701f668e9225" />



