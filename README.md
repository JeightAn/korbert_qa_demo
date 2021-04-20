# korbert_qa_demo
ETRI에서 제공하는 korbert pretrained 모델을 이용해 qa_demo 를 구현합니다.

## 사용 방법
1. git repository를 clone 합니다.  
    - `git clone https://github.com/JeightAn/korbert_qa_demo.git`

2. 가상환경을 설정합니다.
    - `conda create -n qa_demo python=3.6`

3. 가상환경을 실행합니다.
    - `conda activate qa_demo`

3. 필요한 모듈을 설치합니다.
    - `pip install -r requirements.txt`

4. 플라스크 앱 경로를 설정합니다.
    - `export FLASK_APP=app/server.py`

5. 실행합니다.
    - `flask run`
