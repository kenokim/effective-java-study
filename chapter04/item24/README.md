. ## Item 24, 멤버 클래스는 되도록 static 으로 만들라

클래스 in 클래스를 nested class 라고 하며, static 일 경우 static nested class, 아닐 경우 inner class

둘의 차이는 상위 클래스의 멤버 접근 가능성


Principle of least privileadge (이거랑 관련있나) 이런거 처럼 접근 권한은 최소한으로 주는게 좋다.

언제 nested class 를 쓰는가?

1. It is a way of logically grouping classes that are only used in one place
2. It increases encapsulation
3. It can lead to more readable and maintainable code
