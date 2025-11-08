#include "class1-Circle.h"

// 写入半径
void Circle::setR(int r){
    c_R = r;
}
// 读取半径
int Circle::getR(){
    return c_R;
}
// 写入圆心
void Circle::setCenter(Point center){
    c_Center = center;
}
// 读取圆心
Point Circle::getCenter(){
    return c_Center;
}