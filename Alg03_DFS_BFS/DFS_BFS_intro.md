# 그래프 탐색 알고리즘 DFS / BFS
- __탐색 (Search)__ : 많은 양의 데이터 중에서 __원하는 데이터를 찾는 과정__
- DFS와 BFS가 대표적인 그래프 탐색 알고리즘
- DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지!


----

## 자료구조 : 스택 (STACK), 큐(QUEUE)

- 스택
  - 먼저 들어온 데이터가 나중에 나가는 형식 (선입후출)
  - 입구와 출구가 동일한 형태로 시각화
  - 리스트의 `append` 와 `pop` 을 활용해 구현 가능




- 큐
  - 먼저 들어온 데이터가 먼저 나가는 형식 (선입선출)
  - 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화
  - `deque` 라이브러리를 활용하여 구현 가능
  - `append` 와 `popleft` 를 활용


![image](https://user-images.githubusercontent.com/84179578/131049348-707dee3b-ef69-4625-93e7-b239c8f34e1b.png)


----
## 재귀 함수 (Recursive Function)

- 재귀 함수란 __자기 자신을 다시 호출하는 함수__ 를 의미
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야함
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출됨
  - 종료 조건을 포함한 재귀 함수 예시
  ```python
  def recursive_function(i):

      # 100번째 호출을 했을 때 종료되도록 종료 조건 명싱
	  if i == 5:
          return
  	  print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
	  recursive_function(i+1)
	  print(i, '번째 재귀함수를 종료합니다.')
  
  recursive_function(1)
  ```
  출력 결과  
  ![image](https://user-images.githubusercontent.com/84179578/131050996-6886f628-160c-47f6-9bc6-6272aea60b03.png)
  
  - 함수에 대한 정보가 큐와 같은 형식으로 저장되어 비슷한 방식으로 작동함

----

## 최대공약수 계산 (유클리드 호제법) 예제

두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로 유클리드 호제법이 있다.

__유클리드 호제법__
- 두 자연수 A, B 에 대하여 (A > B) A를 B로 나눈 나머지를 R 이라하자.
- 이때, A와 B의 최대공약수는 B와 R의 최대공약수와 같다
- 위 아이디어를 재귀 함수로 작성 가능


예시

|단계|A|B|
|:----:|:----:|:----:|
|1|192|162|
|2|162|30|
|3|30|12|
|4|12|6|

```python
def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a%b)
```


----

### DFS (Depth-First Searh)  
-> 깊이 우선 탐색  

-> 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘  

-> 스택 자료구조(혹은 재귀함수)를 이용  

- 동작 과정  
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함  
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리를 함. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄  
3. 더이상 2번 과정을 수행할 수 없을 때까지 반복함  


![img (6)](https://user-images.githubusercontent.com/84179578/162215989-f1fd3ca8-e390-4e4a-a426-4e556d13c0c5.gif)


_왼쪽 이미지_  



### BFS (Breadth-First Search)

-> 너비 우선 탐색  

-> 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘  

-> 큐 자료구조를 이용  

- 동작 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함  
2. 큐에서 노드를 꺼낸 뒤에 해당노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 함 
3. 더 이상 2번의 과정을 수행할 수 없을때까지 반복  


---

Quiz 1  

![image](https://user-images.githubusercontent.com/84179578/162346264-e9c208ce-c9b8-4747-aab2-df41aba30836.png)
![image](https://user-images.githubusercontent.com/84179578/162346290-9eea8934-786a-40f3-b954-b716b450b161.png)


<br/>

Quiz 2

![image](https://user-images.githubusercontent.com/84179578/162354287-c408779a-2b84-4d78-a1e4-a9dafac4ef53.png)


![image](https://user-images.githubusercontent.com/84179578/162354259-1a9a969d-ff97-4387-8119-cfac70523250.png)
