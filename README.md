# azure-metric-advisor-quickstart #
Azure SDK를 사용해 Metric Advisor를 사용하는 내용을 정리해보는 저장소

## 🛠 시작 전 개발 환경 설정 ##

### [Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=osscontributhon-event-juyoo) ###

### 💻 Azure ###

* Student 가입: https://azure.microsoft.com/ko-kr/free/students/?ocid=AID3035128
* Ubuntu 20.04 사용을 권장




### 💻 Linux ###

* Azure VM: Ubuntu 20.04 + venv 기본 설정 필요
*   sudo apt update
*   sudo apt install python3.8-venv
*   python3 -m venv a
*   source a/bin/activate
*   pip install azure-ai-metricsadvisor --pre


* Visual Studio Code: SSH 접속 확장팩 + Python 확장팩 설치
*   확장팩 설치 후 설정이 안 될 경우
*     - `which python` 으로 python 설치 경로 찾기
*       Ctrl+Shift+p: command palette 실행 
*       python interpreter 클릭 후 설정




# 🛠 .NET 실행 방법
(우분투 리눅스 기준 / 터미널에 입력 ! activate 상태인지 꼭 확인)

1. .NET 설치 전 패키지 추가
  wget https://packages.microsoft.com/config/ubuntu/21.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
  sudo dpkg -i packages-microsoft-prod.deb
  rm packages-microsoft-prod.deb
1. .NET SDK를 사용 ( 아래 4줄 그대로 복붙)
  sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y dotnet-sdk-6.0
1. 설치 확인
dotnet --list-sdks   << 이거 돌려서 버전 확인하기
1. dotnet new console -n metrics-advisor-quickstart
1. cd  metrics-advisor-quickstart
1. dotnet build
1. dotnet add package Azure.AI.MetricsAdvisor --version 1.1.0
1. 실행 dotnet run "Program.cs"


# ✅ 주의 사항

*  test.py 파일에 코드 수정 요망

*  endpoint ="ENDPOINT"
*  subscriptionKey = "SUBSCRIPTION_KEY"
*  apiKey = "API_KEY"  

*  sqlServerConnectionString = ""
 