


## Quick Start

```bash

```


## 개발 동기 


- helm chart와 kubernetes 를 공부하면서 게임쪽 언리얼 엔진의 블루프린트 기능 처럼 시각적으로 보면서 개발하고, 동시에 cluster의 변경사항 추적과 인프라별 wiki 생성, 동시에 재설치시 playbook을 ai를 통해 생성해주는 프로젝트를 만들고 싶어서 프로젝트를 만들었습니다.

- 단순 홈랩부터 기업과 조직의 인프라를 helm,ansible,packer를 이용해서 만든 이 프로젝트를 통해 쉽게 시각적으로 그리고 ai mcp 기능을 통해서 편하게 관리하셨으면 좋겠습니다.

- 프로젝트 icon은 Google Nano Banana Pro를 통해 생성했습니다.

- SSO 지원을 위해 OIDC와 SAML을 지원합니다

## Development Motivation (EN)

- Visualizing Infrastructure: Inspired by the Blueprint system in Unreal Engine, this project provides a node-based visual development environment for Kubernetes and Helm charts.

- Autonomous Enterprise-Grade Management: Our mission is to empower individual developers to manage infrastructure with the same rigor and safety as a major corporation—efficiently, meticulously, and easily.

- AI-Powered Continuity: By integrating AI-driven change tracking and automated Wiki generation, the project ensures that every infrastructure modification is documented and every redeployment playbook is optimized via AI MCP.

- Unified Control: We streamline the orchestration of complex tools like Helm, Ansible, and Packer into a single, intuitive interface.

- OIDC and SAML Support for Single Sign On (SSO)

## Key Features (KO)

- Ansible 및 Packer를 이용한 VPS 골드 이미지 생성
    - 운영체제 최적화 및 보안 설정이 완료된 표준화된 서버 이미지(Gold Image) 제작 자동화.

- 네트워크 토폴로지 디자이너
    - 복잡한 네트워크 구조를 시각적으로 설계하고 관리하는 도구 제공.
    - open vswitch, dhcp, dns server ... 기타 등등 지원

- Code to Pod (코드에서 포드로)
    - 소스 코드를 쿠버네티스(Kubernetes) 포드 단위로 즉시 배포하는 워크플로우 지원.

- CVSS DB 연동 보안 스캐너
    - 최신 CVSS(Common Vulnerability Scoring System) 데이터베이스를 기반으로 인프라의 취약점을 분석하고 위험도 산출.

- 인프라 플레이북 및 위키(WIKI) 자동 생성
    - 구축된 인프라 설정을 바탕으로 실행 가능한 플레이북과 기술 문서를 자동으로 생성.

- 인프라 디퍼(Infra Differ, Git Diff 방식)
    - 초기 설계 상태와 현재 상태를 비교 분석(예: .bashrc 설정 변경점 확인 등 형상 관리).

- 멀티 CSP(Cloud Service Provider) 인프라 배포 지원
    - AWS, Azure, GCP 등 다양한 클라우드 환경에 대한 통합 배포 기능.

- GNS3 기반 테스트 인프라 구축
    - 가상 네트워크 시뮬레이터(GNS3)를 활용하여 실제 배포 전 테스트 환경 구현.

- 로그 기능 지원

- Git 기반 버전 관리 지원

## Key Features (EN)
- Gold Image Generation for VPS with Ansible, Packer

- Network Topology Designer 
    - open vswitch, dhcp, dns server ... etc support

- Code to Pod

- Security Scanner with CVSS DB

- Infra Playbook and WIKI Generation

- Infra Differ(like git diff)
    - check .bashrc and others to check difference form initial Design

- Multi CSP Infra Deploy Support

- Test Infra Generation with GNS3

- Support Logging

- Git Based Version Management

## Prerequisites / 사전 요구 사항

- This project use Ansible, Pakcer, OpenTofu, Python 3.10 (Django project)

### Create Conda 
```bash
conda create --prefix ./AethraPrint_env  python=3.13 -y

conda activate ./AethraPrint_env

# if clear command not working 
# alias clear='/usr/bin/clear'
```

#### Create Venv

```bash
# venv 생성
python3.13 -m venv AethraPrint_env

# 환경 활성화
source AethraPrint_env/bin/activate

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
AethraPrint/ (루트 폴더)
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

#### 사용자 생성 프로젝트 폴더 구조 

```bash
```bash

.blueprint.cf # 메타 데이터 및 프로젝트 관련 설정
.blueprint_db.sqlite3

# openTofu and vps infra
.vps_data.json
.opentofu_data.json

# kubernetes
.namespace.json
.pod.json



#network setup 
.subnet.json
.vps_network_config.json
.firewall.json
.namespace_network.json

# vps image
.vps_package.json
.kern_param.json

# pod and vps package check
.security_test_result.json

# 
.result/
  |---- opentufu/
				|--- opentufu file  
| -----  Ansible
		 | vps01
					--- playbook file
		 | vps02 
				 ----   playbook file

./credential
	|---- sealsecret_cert/
					public.pem , private.pem
  |---- ssh cert
  |---- private.sqlite3 # 각종 인프라 pw 및 credential 정보
  |----
	
./wiki
	l----- playbook.md
	|----- network_design_diagram.md
  |----- vps_image_design.md
  
  |----- secruity_repot_vps.md
  |----- security_report_network.md
  |----- security_report_pod.md
  |----- 
```
