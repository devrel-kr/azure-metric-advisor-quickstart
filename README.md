# azure-metric-advisor-quickstart #
Azure SDK를 사용해 Metric Advisor를 사용하는 내용을 정리해보고, 다양한 언어로 변환해 실행해보는 프로젝트입니다.



## 👉 Azure Metrics Advisor ## 
  
Metrics Advisor는 AI 를 사용하여 시계열 데이터에서 데이터 모니터링 및 이상 감지를 수행하는 [Azure Applied AI Services](https://docs.microsoft.com/en-us/azure/applied-ai-services/what-are-applied-ai-services) 의 일부입니다.  

Metircs Advisor를 사용하면, 머신 러닝을 몰라도 데이터 베이스 상의 문제를 AI 를 사용하여 빠르게 찾아내고 해결할 수 있습니다.
    
  
## 👉 Azure Virtual Machine ##
  

## 🛠 시작 전 개발 환경 설정 ##

### [Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=osscontributhon-event-juyoo) ###

### 💻 Azure ###

* Student 가입: https://azure.microsoft.com/ko-kr/free/students/?ocid=AID3035128
* 일반 사용자 가입 : https://azure.microsoft.com/ko-kr/free/
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



# 🛠 Quick Start #
### 사용 프로그래밍 언어 - C# ###
**- .NET 실행 방법**  
(우분투 리눅스 기준 / 터미널에 입력 ! activate 상태인지 꼭 확인)

* .NET 설치 전 패키지 추가
  wget https://packages.microsoft.com/config/ubuntu/21.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
  sudo dpkg -i packages-microsoft-prod.deb
  rm packages-microsoft-prod.deb
  
* .NET SDK를 사용 ( 아래 4줄 그대로 복붙)
  sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y dotnet-sdk-6.0
  
* 설치 확인
  dotnet --list-sdks   << 이거 돌려서 버전 확인하기
  
* dotnet new console -n metrics-advisor-quickstart

* cd  metrics-advisor-quickstart

* dotnet build

* dotnet add package Azure.AI.MetricsAdvisor --version 1.1.0

* 실행 dotnet run "{파일명}" 

### 사용 프로그래밍 언어 - Python ###
  
* pip install azure-ai-metricsadvisor --pre  
* 실행 python3 "{파일명}"


  
## ✅ 주의 사항 ##

*  test.py 파일에 코드 수정 요망

*  endpoint ="ENDPOINT"
*  subscriptionKey = "SUBSCRIPTION_KEY"
*  apiKey = "API_KEY"  

*  sqlServerConnectionString = ""
 
