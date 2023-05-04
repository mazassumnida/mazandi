# 🌱 mazandi
🌱 solved.ac 잔디를 예쁘게 보여주는 프로필 카드

## 주의사항
- 백준 온라인 저지가 아닌 solved.ac를 기준으로 잔디를 생성합니다.
- 잔디의 진함 정도가 ~solved.ac와 다를 수 있습니다.~ 이제 solved.ac와 일치합니다!

## install
```
pip install -r requirements.txt
uvicorn main:app --reload
```

## Usage
### Theme - Warm (default)
```
![mazandi profile](http://mazandi.herokuapp.com/api?handle={handle}&theme=warm)
```
```
<img src="http://mazandi.herokuapp.com/api?handle={handle}&theme=warm"/>
```

![mazandi profile](http://mazandi.herokuapp.com/api?handle=djs100201)
![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=platinum&theme=warm)

![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=gold)
![mazandi profile](http://mazandi.herokuapp.com/api?handle=pichulia)

![](https://github.com/mazassumnida/mazandi/blob/main/readme_images/bronze_warm.svg)
![](https://github.com/mazassumnida/mazandi/blob/main/readme_images/silver_warm.svg)

![](http://mazandi.herokuapp.com/api?handle=Lawali)

<br/>

### Theme - Cold
```
![mazandi profile](http://mazandi.herokuapp.com/api?handle={handle}&theme=cold)
```
```
<img src="http://mazandi.herokuapp.com/api?handle={handle}&theme=cold"/>
```
![mazandi profile](http://mazandi.herokuapp.com/api?handle=swoon&theme=cold)
![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=platinum&theme=cold)

![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=gold&theme=cold)
![mazandi profile](http://mazandi.herokuapp.com/api?handle=pichulia&theme=cold)

![](https://github.com/mazassumnida/mazandi/blob/main/readme_images/bronze_cold.svg)
![](https://github.com/mazassumnida/mazandi/blob/main/readme_images/silver_cold.svg)


![](http://mazandi.herokuapp.com/api?handle=jhnah917&theme=cold)


### Theme - Dark
```
![mazandi profile](http://mazandi.herokuapp.com/api?handle={handle}&theme=dark)
```
```
<img src="http://mazandi.herokuapp.com/api?handle={handle}&theme=dark"/>
```
![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=diamond&theme=dark)
![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=platinum&theme=dark)

![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=gold&theme=dark)
![mazandi profile](http://mazandi.herokuapp.com/api?handle=pichulia&theme=dark)

![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=silver&theme=dark)
![mazandi profile](http://mazandi.herokuapp.com/api/random?tier=bronze&theme=dark)

![](http://mazandi.herokuapp.com/api?handle=jhnah917&theme=dark)
