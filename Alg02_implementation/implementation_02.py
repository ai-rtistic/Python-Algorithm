# 문제 설명 : 왕실의 나이트

# 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하라.
# 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할때는 a부터 h로 표현한다.
# (왼쪽 위에서 기준으로) 오른쪽으로 abcdefgh , 아래로 12345678

# 예를 들어, c2에 있을 때 이동할 수 있는 경우의 수는 6가지이다.

#---------------------------------------------------------------------------------------

# 입력 조건
# 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌료를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.

# 출력 조건
# 첫째 줄에 나이트가 이동할 수 있는 경우릐 수를 출력한다.

# 입력 예시
# a1

# 출력 예시
# 2

#---------------------------------------------------------------------------------------

data = input()
x = int(data[1:])
idx = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
y = idx[data[0]]

count = 0
move = [[2,1],[1,2],[2,-1],[1,-2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

for a, b in move:
    nx = x + a
    ny = y + b
    if nx >=1 and nx <= 8 and ny >=1 and ny <= 8:
        count += 1

print(count)

#---------------------------------------------------------------------------------------
# 정답 예시

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
