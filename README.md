# Namuwiki Extractor
[파이썬으로 나무위키 JSON 덤프 데이터 파싱하기](https://heegyukim.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4-json-%EB%8D%A4%ED%94%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%8C%8C%EC%8B%B1%ED%95%98%EA%B8%B0-8f41cee1e155) 이용하여 만든 Namuwiki Extractor  

### 개선사항
- 명령형으로 사용가능하게 변경
- 색상코드 제외 정규식 추가
- kss를 이용한 문장 나누기 추가

### 사용법
##### 0. 패키지 설치
```text
ijson
kss<2
namu-wiki-extractor
```
##### 1. 나무위기 덤프 다운로드
[나무위키 덤프 다운로드 페이지](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%8D%A4%ED%94%84)에서 나무위키 덤프 다운로드 
![](https://images.velog.io/images/nawnoes/post/f7211354-e0b3-40a8-af68-087df9a69473/image.png)
##### 2. Namuwiki Extrator 다운로드
![](https://images.velog.io/images/nawnoes/post/1939c2cf-6ca9-4ae5-abf9-17114d786166/image.png)
[nawnoes/NamuwikiExtractor](https://github.com/nawnoes/NamuwikiExtractor) 에서 `NamuwikiExtractor.py` 다운로드.
##### 3. 명령어 실행
`NamuwikiExtractor.py` 경로에서 아래 명령어 실행. 
```sh
python3 NamuwikiExtractor.py --dump_path "[나무위키 덤프 경로]" --output_file "[출력 파일경로]"
```

###### 사용예  
```sh
python3 NamuwikiExtractor.py --dump_path "/Volumes/My Passport for Mac/00_nlp/나무위키/docData200302.json" --output_file "./namuwiki.txt"
```


##### 4. 파일 생성
위에 인자로 사용한 `출력 파일경로`에 아래와 같이 나무위키 텍스트 파일 생성
![](https://images.velog.io/images/nawnoes/post/37b3bbf2-b5cd-41c7-94ba-212b6085608b/image.png)



## Reference
[파이썬으로 나무위키 JSON 덤프 데이터 파싱하기](https://heegyukim.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4-json-%EB%8D%A4%ED%94%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%8C%8C%EC%8B%B1%ED%95%98%EA%B8%B0-8f41cee1e155)
