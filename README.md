# azure-metric-advisor-quickstart
Azure SDK를 사용해 Metric Advisor를 사용하는 내용을 정리해보는 저장소

#.NET 실행 방법
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
