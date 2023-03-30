static factory method 의 장점

1. 이름을 가질 수 있다.

2. Flyweight pattern 처럼 사용할 수 있다.

3. subclass 를 반환할 수 있다.

4. 같은 타입의 parameter 로 다른 클래스를 반환할 수 있다.

5. service provider framework 를 만들수 있다. 반환할 타입이 개발되지 않았어도 생성자를 만들 수 있다.




단점

1. 상속을 하려면 public 이나 protected 가 필요하므로 static 으로는 불가능하다.

2. 개발자가 찾기 어렵다.
