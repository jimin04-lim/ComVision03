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

  ```
- **주요코드**
  ```python

  ```
- **결과물**:


