## Chapter 3 Methods common to all objects

Object 클래스는 extend 를 고려해서 설계되었다.

nonfinal methods (equals, hashCode, toString, clone, finalize) 들은 규약에 따라 override 될 것을 고려하여 설계되었다.

규약을 지키지 않을 경우 HashMap, HashSet 등 규약을 지킨다고 가정하는 클래스들에서 오류가 발생할 수 있다.

