# Item2. 생성자에 매개변수가 많다면 빌더를 고려하라

1. Telescoping constructor / constructor chaining
  - 가독성이 좋지 않다.
    
2. javabeans pattern
  - constructor 로 객체를 생성한 후 setter 로 필드를 입력한다.

Fluent API 와 method chaining 은 같은 말로 a().b(). ... 으로 잇는 방식을 뜻한다.
