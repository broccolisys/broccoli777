"""
제네레이터는 말그래도 값을 생성하는 함수입니다. 알다시피 함수는 값을 반환한 다음 자신의 스코프를 소멸시키고 , 다시 함수를 호출하면, 처음부터 다시 시작됩니다. 즉 한 번 실행됩니다. 그러나 제네레이터 함수는 값을 생성하고 함수의 실행을 일시 중지 할 수 있습니다. 컨트롤이 호출 스코프로 반환되며 ,
원하는 경우 실행을 다시 시작하여 다른 값 (있는 경우)을 얻을 수 있습니다. 이 예제를 보시죠.
"""
def simple_gen():
    yield "Hello"
    yield "World"


gen = simple_gen()
print(next(gen))
print(next(gen))

"""
제네레이터 함수는 어떤 값도 직접 반환하지 않고, 호출되면 반복자와 같은 제네레이터 객체를 건네줍니다. 그 후 제네레이터 
객체에 대해 next ()를 호출하여 값을 반복 할 수 있습니다. 또는 for 루프를 실행하여 처리합니다.
요약 : 제네레이터 함수는 하나의 값을 반환하는 대신 실행을 일시 중지하고 여러 값을 생성 할 수있는 함수입니다.
"""
