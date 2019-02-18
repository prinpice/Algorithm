# Stack2

## Stack2

### 1. 계산기

#### 1. 계산기에서 Stack의 활용
* 문자열 수식 계산의 일반적 방법

  1. 중위표기법의 수식을 후위표기법으로 변경

     * 스택 이용

     * 중위표기법(infix notation) : 연산자를 피연산자의 가운데 표기하는 방법

       예) A + B

  2. 후위표기법의 수식을 스택을 이용하여 계싼

     * 후위표기법(postfix notation) : 여난자를 피연산자 뒤에 표기하는 방법

       예) AB+

#### 2. 중위표기식을 후위표기식으로 변환

* Step1. 중위표기식의 후위표기식으로 변환 방법1

  1. 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현
  2. 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동

  예) A*B-C/D 변환 방법

  * 
    * 1단계 : ( (A*B) - (C/D) )
    * 2단계 : ( (A B) * (C D)/ )-
    * 3단계 : AB*CD/-

  * 문제점
    * **사람의 손으로 처리하기는 쉽지만** 프로그램으로 작성하기는 어려움!
  * Solution
    * 중위표기식을 **후위표기식으로 변환하는 알고리즘** 개발!

* Step1. 중위표기식의 후위표기식으로 변환 방법2(스택 이용)

  * 중위표기법에서 후위표기법으로의 변환 알고리즘

  1. 입력 받은 중위표기식에서 토큰을 읽음
  2. 토큰이 피연산자이면 토큰을 출력
  3. 토큰이 연산자(괄호포함)일 경우
     * 우선순위가 높으면 -> 스택에 push
     * 우선순위가 안 높으면 -> 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push
     * 만약 top에 연산자가 없으면 -> push
  4. 토큰이 오른쪽 괄호 ')'일 경우
     * 스택 top에 왼쪽 괄호 '('가 올 때까지 스택에 pop 연산을 수행
     * pop한 연산자를 출력
     * 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않음
  5. 중위표기식에 더 읽을 것이 없다면 중지, 더 읽을 것이 있다면 1부터 반복
  6. 스택에 남아 있는 연산자를 모두 pop하여 출력
     * 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음  

#### 3. 후위표기법 수식을 스택으로 계산

* Step2. 후위표기법의 수식을 스택을 이용하여 계산

  1. 피연산자를 만나면 스택에 push함
  2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push함
  3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

  * 계산 시 주의 사항!
    * 후위 표기식을 계산 시, **피연산자를 스택에 쌓아 계산!**


#### 4. 수식을 eval() 내장 함수로 계산

* 문자열로 된 수식을 계산 시
  * 스택을 두 번 사용해서 처리했던 연산을 파이썬에서 제공되는 **eval() 내장 함수**로 계산할 수 있음
  * eval(수식)
    * 문자열로 된 수식을 계산함
    * Evaluation = " 값을 구함 " 이란 뜻
    * 올바른 수식이 아닌 경우 SyntaxError 예외가 발생함
    * eval("6+5*(2-8)/2") 는 문자열로 된 수식의 계산결과를 반환함

### 2. 백트래킹

#### 1. 백트래킹 기법의 정의

* 백트래킹(Backtracking)

  * 해를 찾는 도중에 '막히면', (즉, 해가 아니면) 되돌아가서 다시 해를 찾아가는 기법
  * 최적화(Optimazation) 문제
  * 결정(Decision) 문제
    * 문제의 조건을 만족하는 해가 존재하는 지의 여부를 'yes' 또는 'no' 로 답하는 문제
    * 미로 찾기
    * n-Queen 문제
    * Map coloring
    * 부분 집합의 합(Subset Sum) 문제 등 

  => **해결**

#### 2. 백트래킹 - 미로 찾기

예) 백트래킹 기법 활용 - 미로찾기

 	1. 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제
 	2. 이동할 수 있는 방향은 4방향으로 제한
     * 스택을 이용하여 경로를 찾기
     * 스택을 이용하여 지나온 경로를 역으로 되돌아감
     * 스택을 이용하여 다시 경로를 찾기
* 백트래킹과 깊이 우선 탐색의 차이
  * 백트래킹
    * 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 **시도의 횟수를 줄임**
    * 가지치기(Prunning)
    * 불필요한 경로의 조기 차단
    * N! 가지의 경우의 수를 가진 문제에 대해 백트레킹에 가하면 일반적으로 **경우의 수가 줄어들지만** 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능
    * 모든 후보를 검사하지 않음
  * 깊이 우선 탐색
    * 모든 경로를 추적
    * N! 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 **처리 불가능한 문제**
    * 모든 후보를 검사

#### 3. 백트래킹 알고리즘의 특징

* 백트래킹 기법
  * 어떤 노드의 유망성을 점검한 후에 유망(Promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(Backtracking) 다음 자식 노드로 감
  * 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 함
  * 반대로 **해답의 가능성이 있으면 유망하다**고 함
  * 가지치기(Pruning): 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않음
* 백트래킹을 이용한 알고리즘의 절차
  1. 상태 공간 Tree의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지를 점검
  3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속

#### 4. 백트래킹 알고리즘

* 일반 백트래킹 알고리즘
  * n * n의 정사각형 안에 n개의 queen을 배치하는 문제로, 모든 queen은 자신의 일직선상 및 대각선상에 아무 것도 놓이지 않아야 함
* 깊이 우선 검색 VS 백트래킹
  * 순수한 깊이 우선 탐색
    * **155** 노드
  * 백트래킹(위에보다 수행속도 1/5)
    * **27** 노드
#### 4. 백트래킹 알고리즘
* Power Set
  * 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합
  * 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n^이 나옴
* 백트래킹 기법으로 Power Set 구하기
  * 일반적인 백트래킹 접근 방법 이용
  * n개의 원소가 들어있는 집합의 2^n^개의 부분집합을 만들 때 True 또는 False값을 가지는 항목들로 구성된 n개의 리스트를 만드는 방법 이용
  * 리스트의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값
* Power Set을 구하는 백트래킹 알고리즘

```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
 def construct_candidate(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)
```

* 순열을 구하는 백트래킹 알고리즘

```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k+1):
            print(a[i], end="")
        print()
    else:
        k+=1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX
    
    for i in range(1, k):
        in_perm[a[i]] = True
        
    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates
```

### 3. 분할 정복

#### 1. 분할 정복 알고리즘

* 설계 전략

  * 분할(Divide)
    * 해결할 문제를 **여러 개의 작은 부분**dmfh sksna
  * 정복(Conquer)
    * 나눈 작은 문제를 **각각 해결**
  * 통합(Combine)
    * (필요하다면) 해결된 **해답을 모음**

* 거듭 제곱(Exponentiation) 알고리즘: O(n)

  ```python
  def Power(Base, Exponent):
      if Base == 0: return 1
      result = 1 # Base^0은 1이므로
      for i in range(Exponent):
          result *= Base
      return result
  ```

* 분할 정복 기반의 알고리즘 : O(log2n)

  ```python
  def Power(Base, Exponent):
      if Exponent == 0 or Base == 0:
          return 1
      if Exponent % 2 == 0:
          NewBase = Power(Base, Exponent/2)
          return NewBase * NewBase
      else:
          NewBase = Power(Base, (Exponent-1)/2)
          return (NewBase * NewBase) * Base
  ```

#### 2. 퀵 정렬

* 퀵 정렬과 합병 정렬의 비교

  * 공통점
    * 주어진 리스트를 두 개로 분할하고, 각각을 정렬
  * 차이점
    * 합병 정렬
      * 분할할 때, 단순하게 두 부분으로 나눔
      * 각 부분 정렬이 끝난 후, **'합병'이란 후처리 작업이 필요함**
    * 퀵 정렬
      * 분할할 때, 기준 아이템(Pivot Item)을 중심으로, 이보다 **작은 것은 왼편, 큰 것은 오른편**에 위치시킴
      * 각 부분 정렬이 끝난 후, **후처리 작업이 필요로 하지 않음**

* 퀵 정렬 알고리즘

  ```python
  def quickSort(a, begin, end):
      if begin < end:
          p = partition(a, begin, end)
          quickSort(a, begin, p-1)
          quickSort(a, p+1, end)
  ```

* 주어진 리스트에서 피봇을 구하는 알고리즘

  ```python
  def partition(a, begin, end):
      pivot = (begin + end) // 2
      L = begin
      R = end
      while L < R:
          while(a[L] < a[pivot] and L < R): L += 1
          while(a[R] < a[pivot] and L < R): R -= 1
          if L < R:
              if L == pivot: pivot = R
                  a[L], a[R] = a[R], a[L]
      a[pivot], a[R] = a[R], a[pivot]
      return R
  ```

* 퀵 정렬 수앵 과정
  1. 원소 2를 피봇으로 선택하고 퀵 정렬 시작하기
  2. 오른쪽 부분 집합에 대해서 퀵 정렬 수행하기
  3. 피봇 15의 왼쪽 부분 집합에서 원소 10을 피봇으로 선택하여 퀵 정렬 수행하기
  4. 원소 16에 대한 오른쪽 부분 집합에 대해 퀵 정렬을 수행하기
  5. 오른쪽 부분 집합에 대해서 퀵 정렬 수행하기
* 퀵 정렬의 최악의 시간 복잡도는 O(n^2^) -> 합병정렬에 비해 좋지 못함
  * 왜 빠른(Quick) 정렬인가? 퀵 정렬의 평균 복잡도는 **nlogn**이기 때문
  * 평균적으로 가장 빠름