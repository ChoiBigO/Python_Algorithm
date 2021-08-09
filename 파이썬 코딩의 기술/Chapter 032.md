# Chapter 032 긴 리슽트 컴프리헨션보다는 제너레이터 식을 사용하라

- 컴프리헨션의 문제점은 입력 시퀀스와 같은 수의 원소가 들어 있는 리스트 인스턴스를 만들어 낼 수 있다는 것이다.
- 이는 입력이 작으면 문제가 되지 않지만 입력이 커지면 메모리를 상당히 많이 사용한다.
- 다음과 같이 입력이 작으면 큰 문제가 되지 않는다.

```py
value = [len(x) for x in open('c:\\TestSpace\\My_File.txt')]

```

- () 사이에 리스트 컴프리헨션과 비슷한 구문을 넣어 제너레이터 식을 만들 수 있다.
```py
it = (len(x) for x in open('c:\\TestSpace\\My_File.txt'))
print(it)
print(next(it))
print(next(it))
print(next(it))
```

- 제너레이터 식의 또다른 강력한 특징은 두 제너레이터 식을 합성할 수 있다는 것이다.
```py
it = (len(x) for x in open('c:\\TestSpace\\My_File.txt'))

roots = ((x, x**0.5) for x in it)

print(next(roots))
print(next(roots))
print(next(roots))
print(next(roots))
```

- 아주 큰 입력 스트림에 대해 여러 기능을 합성해 적용해야 한다면, 제너레이터 식을 사용해라