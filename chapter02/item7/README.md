## Item 7 Eliminate obsolete object references

Memory leaks happens when the program still holds the obsolete object references.

Memory leaks can lead to 2 severe problems;

1. Performace degradation caused by increased memory usage and garbage collections.
2. Program termination caused by disk paging or OOM error.

Whenever a class manages its own memory, the programmer should be alert for memory leaks.

Memory leaks can be discovered by careful code inspection or heap profiler.
