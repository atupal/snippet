
runtime 包中有几个处理goroutine的函数：

- Goexit
<br> 退出当前的goroutine， 但是defer函数还会继续调用
- Gosched
<br> 让出当前的goroutine的执行权限，调度器安排其他等待的任务运行，并在下次某个时候从该位置恢复执行
- NumCPU
<br> 返回CPU核数量
- NumGoroutine
<br> 返回正在执行和排队的任务总数
- GOMAXPROCS
<br> 用来设置可以运行的CPU核数
