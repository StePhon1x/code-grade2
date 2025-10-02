#pragma once
#include <iostream>
using namespace std;

// 点类
class Point
{
private:
    int c_x, c_y; 

public:
    // 写入c_x
    void setX(int x);
    // 读取c_x
    int getX();
    // 写入c_y
    void setY(int y);
    // 读取c_y
    int getY();

};