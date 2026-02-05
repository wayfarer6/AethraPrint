


## Quick Start

```bash

```


## 개발 동기 


- helm chart와 kubernetes 를 공부하면서 게임쪽 언리얼 엔진의 블루프린트 기능 처럼 시각적으로 보면서 개발하고, 동시에 cluster의 변경사항 추적과 인프라별 wiki 생성, 동시에 재설치시 playbook을 ai를 통해 생성해주는 프로젝트를 만들고 싶어서 프로젝트를 만들었습니다.

- 단순 홈랩부터 기업과 조직의 인프라를 helm,ansible,packer를 이용해서 만든 이 프로젝트를 통해 쉽게 시각적으로 그리고 ai mcp 기능을 통해서 편하게 관리하셨으면 좋겠습니다.

- 프로젝트 icon은 Google Nano Banana Pro를 통해 생성했습니다.

## Development Motivation (EN)

- Visualizing Infrastructure: Inspired by the Blueprint system in Unreal Engine, this project provides a node-based visual development environment for Kubernetes and Helm charts.

- Autonomous Enterprise-Grade Management: Our mission is to empower individual developers to manage infrastructure with the same rigor and safety as a major corporation—efficiently, meticulously, and easily.

- AI-Powered Continuity: By integrating AI-driven change tracking and automated Wiki generation, the project ensures that every infrastructure modification is documented and every redeployment playbook is optimized via AI MCP.

- Unified Control: We streamline the orchestration of complex tools like Helm, Ansible, and Packer into a single, intuitive interface.



## Prerequisites / 사전 요구 사항

- This project use Ansible, Pakcer, Opentufu, Python 3.10 (Django project)

### Create Conda 
```bash
conda create --prefix ./OpenBlueprint_env  python=3.13 -y

conda activate ./OpenBlueprint_env

# if clear command not working 
# alias clear='/usr/bin/clear'
```

#### Create Venv

```bash
# venv 생성
python3.13 -m venv OpenBlueprint_venv

# 환경 활성화
source OpenBlueprint_venv/bin/activate

```

### Install Essential Packages

```bash

명령어로도 설치 가능!conda install django djangorestframework -c conda-forge # conda 
conda install --file requirements.txt


# export
#pip freeze> requirements.txt
```


### Project Structure

```bash
OpenBlueprint/ (루트 폴더)
├── manage.py          # 실행 파일
├── open_blueprint/    # 설정 폴더 (settings.py, 전역 urls.py)
├── core/              # 공통 유틸리티, 추상 모델 등
├── main/              # 
├── pages/             # 
└── account/           # 로그인, 회원가입, 프로필 관리
```

### Run Server 

- frontend

```bash
npx next dev -H 0.0.0.0
```

-backend 

```bash
python3 manage.py runserver [port_numer]
```

