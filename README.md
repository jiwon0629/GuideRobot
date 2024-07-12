# 시각장애인을 위한 위험 대처 반려로봇  

## 개요  
### 배경  
현재 장애인들을 위해 시스템이 많이 구성되고 있지만 아직까지도 장애인들이 혼자서 살아가기에는  
현재까지는 위험요소가 많은건 사실적인 요인이다. 이런 부분들이 어느 정도 해결이  
될 수 있는 세상을 만들어 주고 싶다는 관전에서 시작하였다.  

해당 프로젝트는 시각장애인과 반려 동물에 대한 시각에서 부터 시작되었다. 현재 시각장애인들을  
위한 시스템이 많이 생겨나고 있지만 위험에 대처 할 수 없는 부분이 있어 그런 부분들을 
적용시켜 생각해보았다.  또한 위험대처뿐 아니라 사랑스러운 반려동물과 같은 반려로봇을  
생각하여 일석이조의 효과를 생각하였다.  

반려로봇은 앞을 보지못하는 시각장애인과의 대화를 나눌 수 있게 만들며, 반려로서의 역할을  
수행해 나갈 수 있게하며 시각장애인들은 골든 리트리버를 데리고 다니며 길 안내를 받지만  
로봇이 그러한 일도 수행하며 안내 및 대화를 할 수 있어 귀가 밝은 시각장애인들이 편리한  
환경이 되어 지낼 수 있는 세상을 만들자는 취지에서 생각해보았다.  

## 프로젝트 개요  

이 프로젝트는 반려 로봇에 설치 된 카메라를 통해 사용자의 안전을 생각하며 충돌 될 수 있  
는 부분을 데이터셋을 통하여 학습시켜 시각장애인이 위험요소에서부터 피할 수 있는 환경을  
만들고 대응해주는 취지에서 시작된 프로젝트이다. 또한 혼자있는 시각장애인들을 위해 반려  
로봇으로써 같이 대화를 할 수 있으며, 언제 어디서든 사용자와 함께 붙어 다닐 수 있는 반려  
로봇이 될 것 이다. 블랙박스 기능 탑재하여 카메라 영상을 DB에 동영상 데이터를 저장할 수  
있게 해주는 시스템 구성 예정.  

## 반려 로봇의 기능 구현  
- 로봇 컨트롤러 : 로봇을 컨트롤러로도 제어할 수 있으며, 사용자 옆에 따라다니게 컨트롤  
할 수 있게 구성.

- 영상 및 기록 : 로봇에 카메라 기능을 탑재하여 카메라를 통하여 사물 인지 및 등록된 상황  
에 대한 대처 능력을 결과값으로 도출 및 블랙박스 기능을 탑재하여 영상 데이터를 DB에 저장.

- 이미지 트레이닝 데이터 : 상황에 맞는 데이터 셋을 구현하여 로봇의 행동 및 대화 형식으  
로 결과값 도출 할 수 있는 환경 제공.

- 보호자 안심 서비스 웹앱 제공 : NativeAPP제작하여 상시로 보호자가 로봇 카메라로 출력  
된 영상을 웹앱으로 확인 할 수 있는 서비스 제공.

- 대화 기능 탑재 : 사용자와 대화를 할 수 있는 기능 탑재하여 반려 로봇의 역할 수행.  
행동 구현 : 위험한 상황이 발생될 시 로봇이 안내 음성으로 안내하고 사용자의 길을 막아 위  
험한 상황을 대처 할 수 있게 해주는 서비스 제공.  

### 사용 도구  
Anaconda 가상환경과 Visual Studio Code를 활용하여 개발 예정.  
(협의 후 변경 가능)  

### 환경 설정  
프론트 엔드  
(협의 후 작성)  
백엔드  
(협의 후 작성)  

### 프로젝트 필요 조건  
- Git과 github을 이용한 협업 예정  
- Android Studio, C, Python, Roboflow를 이용한 상황인지에 대한 로봇 행동 구현 예정 (변동 가능성 有)  
2024.06.24. ~ 진행중

<hr>

2024.7.2.   
WAP server를 이용하기  
영상에 비춰진 얼굴을 인식하고 등록된 사람인지 파익한다.  
등록이 되어있지 않다면 등록을 할 수 있고 데이터가 저장이 된다.  
저장된 후에는 등록된 사람이면 음성으로 누구인지 알려준다.  

<hr>

2024.7.4.  
mariaDB, wampserver, MySQL, svn설치  
svn 서버 연결(코드 공유 가능)  

<hr>

2024.7.9.  
Flutter를 이용하여 실시간 스트리밍 가능한 기능 앱 구현

<hr>

2024.7.11.  
Depth카메라로 보여지는 화면 웹으로 실시간 스트리밍  





















