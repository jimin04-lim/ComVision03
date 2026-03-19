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
  ```
- **주요코드**
  ```python
  ```
- **결과물**:

## 0302. 캐니 에지 및 허프 변환을 이용하여 직선 검출
- **설명**:
 - dabo 이미지에 캐니 에지 검출을 사용하여 에지 맵 생성
 - 허츠 변환을 사용하여 이미지에서 직선 검출
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
  
  ```
- **주요코드**
  ```python

  ```
- **결과물**: 


## 0303. GrabCut을 이용한 대화식 영역 분할 및 객체 추
- **설명**:
  - coffee cup 이미지로 사용자가 지정한 사각형 영역을 바탕으로 GrabCut 알고리즘을 통한 객체 추출
  - 객체 추출 결과를 마스크 형태로 시각화
  - 원본 이미지에서 배경 제거 및 객체만 남은 이미지 출력
- **요구사항**:
  - cv.grabCut():대화식 분할 수행
    - bgdModel과 fgdModel은 np.zeros((1,65),np.float64)로 초기화
  - 초기 사각형 영역은 (x,y,width,height) 형싱으로 설정
  - 마스크를 사용하여 원본 이미지에서 배경 제거
    - cv.GC_BGD,cv.GC_FGD,cv.GC_PR_BGD,cv.GC_PR_FGD를 사용
  - np.where()로 마스크 값을 0 혹은 1로 변경 후 원본 이미지에 곱해 배경 제거
  - Matplotlib를 사용하여 원본 이미지, 마스크 이미지, 배경 제거 이미지 세 개를 나란히 시각화

- **코드**
  ```python
  import cv2 as cv # OpenCV 라이브러리 임포트 
  import numpy as np
  import sys # 프로그램 종료 기능을 위해 임포트

  # 전역 변수 설정
  is_dragging = False # 마우스 드래그 상태 확인 
  x_start, y_start = -1, -1 # 드래그 시작 좌표 
  roi_img = None # 잘라낸 이미지 저장 변수

  def on_mouse(event, x, y, flags, param):
      global is_dragging, x_start, y_start, img_copy, roi_img # 전역 변수 사용

      if event == cv.EVENT_LBUTTONDOWN: # 왼쪽 버튼 클릭 시 시작 
          is_dragging = True
          x_start, y_start = x, y
        
      elif event == cv.EVENT_MOUSEMOVE: # 마우스 이동 중 
          if is_dragging:
              img_draw = img_copy.copy() # 원본 복사본 위에 사각형 그림
              cv.rectangle(img_draw, (x_start, y_start), (x, y), (0, 255, 0), 2) # 초록색 사각형 시각화
              cv.imshow('ROI Selection', img_draw)
            
      elif event == cv.EVENT_LBUTTONUP: # 마우스 버튼을 떼면 완료 
          is_dragging = False
          # 드래그 방향에 상관없이 좌표 설정 (슬라이싱을 위해)
          x_min, x_max = min(x_start, x), max(x_start, x)
          y_min, y_max = min(y_start, y), max(y_start, y)
        
          if x_max - x_min > 0 and y_max - y_min > 0:
              roi_img = img_copy[y_min:y_max, x_min:x_max] # numpy 슬라이싱으로 ROI 추출 
              cv.imshow('Cropped ROI', roi_img) # 추출된 영역 별도 창 표시

  # 이미지 로드 (경로 주의!) 
  img = cv.imread('girl_laughing.jpg')
  img_copy = img.copy() # 수정을 위한 이미지 복사본

  cv.imshow('ROI Selection', img_copy) # 초기 화면 출력 
  cv.setMouseCallback('ROI Selection', on_mouse) # 마우스 이벤트 처리 등록 

  while True:
      key = cv.waitKey(1) & 0xFF # 키 입력 대기
    
      if key == ord('r'): # 'r' 키: 초기화 
          img_copy = img.copy()
          cv.imshow('ROI Selection', img_copy)
          print("영역 선택 리셋")
        
      elif key == ord('s'): # 's' 키: ROI 저장
          if roi_img is not None:
              cv.imwrite('cropped_result.jpg', roi_img) # 파일로 저장
              print("ROI 이미지가 성공적으로 저장되었습니다.")
            
      elif key == ord('q'): # 'q' 키: 종료
          break

  cv.destroyAllWindows()
  ```
- **주요코드**
  ```python
  img.copy() # 원본을 훼손하지 않기 위해 사본 생성 (사각형 시각화용)
  cv.EVENT_LBUTTONDOWN # 마우스 왼쪽 버튼을 누른 순간의 좌표 저장
  cv.rectangle(img, pt1, pt2, color, thickness) # 드래그 중인 사각형 영역 표시
  img[y1:y2, x1:x2] # (핵심) 넘파이 슬라이싱을 이용해 관심영역(ROI)만 잘라내기
  cv.EVENT_LBUTTONUP # 마우스를 떼는 순간 최종 ROI 영역 확정
  ```
- **결과물**:
<img width="2807" height="1651" alt="image" src="https://github.com/user-attachments/assets/464e49c5-f099-4f86-aa9b-882522d9c916" />
<img width="1805" height="1474" alt="image" src="https://github.com/user-attachments/assets/269e71c5-7c22-4fef-bc4a-26165a52e88b" />



