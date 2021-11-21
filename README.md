# azure-metric-advisor-quickstart #
Azure SDK를 사용해 Metric Advisor를 사용하는 내용을 정리해보고, 다양한 언어로 변환해 실행해보는 프로젝트



### 👉 Azure Metrics Advisor ### 
  
Metrics Advisor는 AI 를 사용하여 시계열 데이터에서 데이터 모니터링 및 이상 감지를 수행하는 [Azure Applied AI Services](https://docs.microsoft.com/en-us/azure/applied-ai-services/what-are-applied-ai-services) 의 일부

Metircs Advisor를 사용하면, 머신 러닝을 몰라도 데이터 베이스 상의 문제를 AI 를 사용하여 빠르게 찾아내고 해결하는 것이 가능

> 생성한 Metrics Advisor Resource 에서 *key 관리 > 액세스 키 표시* 에서 **endpoint | key1** 값을 각각 test.py 내부의**endpoint | subscriptionKey** 에 부여
  
> [API key 확인 링크](https://metricsadvisor.azurewebsites.net/api-key) 를 통해서 **API Keys > Primary API Key 혹은 Secondary API Key** 값을 test.py 내부의 **apiKey** 에 부여
  
### 👉 Azure Virtual Machine ###  
  
Test 환경을 Ubuntu 20.04 환경을 사용하였기 때문에 Ubuntu 20.04 사용을 권장  
  
Azure 에서 제공하는 가상머신 리소스를 활용하여 vscode 에서 프로젝트를 수행
  

## 🛠 시작 전 개발 환경 설정 ##

### [Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=osscontributhon-event-juyoo) 설치 ###

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
  dotnet --list-sdks   << 버전 확인하기
  
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
*  => 보안 유지를 위해 key 값을 할당한 후 업로드 하지 않기

*  sqlServerConnectionString = ""
*  => 보안 유지를 위해 sql db 로그인 정보를 업로드 하지 않기
  
*  test.py 의 33 line : name 에는 중복되지 않는 data 이름을 할당
 
