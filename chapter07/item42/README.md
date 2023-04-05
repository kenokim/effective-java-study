### Item 42. Prefer lambda to anonymous class

Function object 를 표현하여 함수형 프로그래밍을 할 수 있다.

이를 anonymous class 로 작성할 경우 코드가 너무 길다.

Functional interface 의 인스턴스를 lambda 로 작성하면 더 간결하다.

'''java
(s1, s2) -> Integer.compare(s1.length(), s2.length());
'''

람다의 매개변수 타입은 생략할 수 있다. 컴파일러가 타입을 추론한다.

