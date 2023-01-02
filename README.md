# Python

## 준비하게 된 계기

- `언어 욕심에 Javascript이외에 다른 언어를 배워보고 싶었습니다.`
- `JS가 아닌 다른 언어로 코딩테스트를 보고 싶습니다`
- `객체지향 언어에 대해서 자세히 공부해보고 인터프리터 언어에 대해서 더 깊이 공부해보고 싶습니다`

## What I've studied

- ### 2023-01-02

  - input함수(`입력받는 함수`)

    - `return값이 str type이야!`
    - `입력받는 값에 따라서 type change해줘야 해!`
    - `여러 개 입력 >>> split()사용`
    - `split(문자열을 배열로 바꿔줌)`
    - 어차피 input의 `return값이 str type`이어서 `split사용 가능함`

  - print함수(`출력하는 함수`)

    - `구분자 바꿔주기`
      - sep("구분자")
    - `끝 문자 바꿔주기`
      - end(" ") `\n이 default값`
    - `여러 줄 바꿔서 출력하기`
      ```python
      print("""
        dsdsdsd
        sdsdsds
        sdsdsds
        dsd
        """)
      ```
    - `❗️변수 포함해서 출력하는 방법❗️`

      - `1. 콤마, +로 나타내기`
        ```python
            age = 10
            print("내 나이는 >> ",age)
            print("내 나이는 >> " + age)
        ```
      - `2. format사용하기 + {}`

        - 변수가 2개 이상이면 순서대로!

        ```python
            age = 10
            print("내 나이는 {}살".format(age))

            name = "jisung"
            print("나이 > {}, 이름 > {}".format(age, name))
        ```

      - `3.f + {} 사용하기!! => 보통 이거 교수님말씀..`
        ```python
        age = 10
        hello = "hi"
        print(f"age >> {age}, hello >> {hello}")
        ```
