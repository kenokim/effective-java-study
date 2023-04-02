### Item 4. Use private constructor to prevent instancing

static member 를 제공하는 유틸리티 클래스를 만들 때, abstract class 를 쓰지 말고 private constructor 로 인스턴스화를 방지하라.

static member (member = method + field) utility class = JAVA : private constructor (or abstract class) , KOTLIN : Top-Level function or companion object
