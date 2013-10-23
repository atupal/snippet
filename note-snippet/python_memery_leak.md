当你的数据结构有循环引用时，就会出现内存泄露，
因为python的垃圾收集器不会收集环中的任何一个node,
因为每个node的引用计数都不为0. 虽然说python有一个
专门的垃圾收集器来收集这些循环引用。但是它很长时间才运行
一次，所以你不能依赖它。

解决的方法有两个，

- 采用弱引用。`weakref.ref(node)`, 详见http://docs.python.org/2/library/weakref.html
- 在不适用这个数据结构了时主动破坏环结构（不推荐，不pythonic）
