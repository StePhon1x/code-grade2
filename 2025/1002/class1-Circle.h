#pragma once
#include "class1-point.h"
#include <iostream>
using namespace std;

// 圆类
class Circle
{
private:
    int c_R; // 半径
    Point c_Center; // 圆心

public:
    // 写入半径
    void setR(int r);
    // 读取半径
    int getR();
    // 写入圆心
    void setCenter(Point center);
    // 读取圆心
    Point getCenter();
};
