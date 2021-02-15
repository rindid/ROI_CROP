# img_cropper

## USED

* python 3.9.1
* numpy 1.20.1
* opencv-python 4.5.1.48



## 목표

* ocr학습 및 인식을 위해 이미지를 적절한 ROI(Region of Interest)로 자르는 것.



## 제반사항

* 주어진 이미지는 노이즈가 없는 이미지를 가정한다. (이미지화 된 문서 파일 혹은 이미지화 된 pdf파일 등, 주로 사무자동화에 사용될 이미지를 가정하였다.)
* ROI는 텍스트와 로고(작은 이미지)이다.



## 참고자료

* 기반 코드(https://stackoverflow.com/questions/23506105/extracting-text-opencv/23565051#23565051)
* 위 코드를 찾은 포스팅(https://blog.naver.com/PostView.nhn?blogId=monkey5255&logNo=221598376164&redirect=Dlog&widgetTypeCall=true&directAccess=false)
* 코드의 전반적인 흐름 및 사용 기술을 파악하기에 좋은 자료(https://d2.naver.com/helloworld/8344782)
* 기타 블로그 및 포스팅등을 활용하여 기반 기술(opencv, numpy, python)을 이해하였다.



## 결과

|                             입력                             |                             출력                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src=".\image\test.png" alt="test" style="zoom: 50%;" /> | <img src=".\image\result.png" alt="result" style="zoom: 50%;" /> |



### 이 외에도...

프로젝트를 진행함에 있어 특정 색 강조, 필요없는 line제거, pdf파일(매우 큼)을 png로 변환을 진행하였다.