import sys
input = sys.stdin.readline #입력시간 줄임

"""
 [Java vs C++]

 1. 입력으로 주어진 변수가 C++ 형식에도 맞고, JAVA 형식에도 맞을 수 있음 (ex. name)
 2. "Error!"인 경우 
    2-1. (공통) 알파벳 소문자로 시작하지 않는 변수
    2-2. (Java)
        - 언더바('_')가 등장하는 변수
    2-3. (C++)
        - 언더바('_')가 연속해서 등장하는 변수
        - 대문자가 등장하는 변수

(주의) python에서 string은 immutable한 객체이다 -> 변경이 불가능
ex) 아래 코드를 실행해보세요
    a = "hello"
    a[0] = "H" 
"""

# cpp 형식으로 바꾸는 함수
def to_cpp(word): #자바형식을 때 실행
    result = "" #결과 초기화

    for c in word: #문자 하나씩 탐색
        if c == c.upper(): #문자가 대문자이면
            result += '_' #언더바 추가
        result += c.lower() #소문자로 추가
    
    return result #결과 출력

# 가능하면 java형식으로 바꾸는 함수
def to_java_if_possible(word_list): #C형식이라면
    result = [] #배열 선언
    for word in word_list: #배열 값 하나씩 탐색
        if len(word) == 0 or word != word.lower(): #단어 길이가 0이거나 단어가 모두 소문자가 아니면
            return "Error!" #에러
        result.append(word.capitalize()) #에러가 아니면 result에 append

    result[0] = result[0].lower() # 첫 단어는 capitalize하면 안됨
    return ''.join(result) #전체 word를 join

# 입력
word = input().rstrip() #입력 받음


if (not word[0].isalpha()) or word[0] == word[0].upper(): # 공통 예외에 포함되는 경우
    print("Error!") #에러 출력
elif word.isalpha():    # Java식 변수인 경우
    print(to_cpp(word)) #cpp형식으로 바꿔서 출렬
else:   # 나머지 경우 (error || cpp식 변수)
    word_list = word.split('_') #언더바 기준으로 단어를 잘라서 배열에 입력
    print(to_java_if_possible(word_list)) #자바형식으로 바꿔석 출력