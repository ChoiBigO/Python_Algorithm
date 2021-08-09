# Chapter 033 yield from을 사용해 여러 제너레이터를 합성하라

```py
def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    print(f'Delta: {delta: .1f}')


def run(func):
    for delta in func():
        render(delta)

run(animate)
```

- 이코드의 문제점은 animate가 너무 반복적 이라는 것이다.
- for 문과 yield 식이 반복되면서 잡음이 늘고 가독성이 떨여 진다.
- yield from을 사용해 for 루프를 내포 시키고 yield를 처리하도록 만든다.
- 제너레이터를 합성 한다면 가급적 yield from을 사용하라

```py
def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

run(animate_composed)
```
