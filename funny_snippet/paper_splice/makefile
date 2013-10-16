# $@  表示目标文件
# $^  表示所有的依赖文件
# $<  表示第一个依赖文件
# $?  表示比目标还要新的依赖文件列表

opencv_lib = -I /usr/include/opencv/ -L /usr/lib -lm `pkg-config opencv --cflags --libs`
head = -I /usr/include/opencv

main:base.cpp
	g++ -g $< -o $@ $(opencv_lib)

1_main:1_base.cpp
	g++ -g $< -o $@ $(opencv_lib)

fe:feature.cpp
	g++ -g $< -o $@ $(opencv_lib)

clean:
	rm *.o main
