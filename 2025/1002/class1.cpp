// 练习案例2：点和圆的关系
// 设计一个圆形类（Circle），和一个点类（Point），计算点和圆的关系。
// 注意： 圆心也是一个点，本案例中（Circle）类中又套了一个（Point）类。

#include "class1-point.h"
#include "class1-Circle.h"
#include <iostream>
using namespace std;

// // 点类
// class Point
// {
// private:
//     int c_x, c_y; 

// public:
//     // 写入c_x
//     void setX(int x){
//         c_x = x;
//     }
//     // 读取c_x
//     int getX(){
//         return c_x;
//     }
//     // 写入c_y
//     void setY(int y){
//         c_y = y;
//     }
//     // 读取c_y
//     int getY(){
//         return c_y;
//     }

// };



// // 圆类
// class Circle
// {
// private:
//     int c_R; // 半径
//     Point c_Center; // 圆心

// public:
//     // 写入半径
//     void setR(int r){
//         c_R = r;
//     }
//     // 读取半径
//     int getR(){
//         return c_R;
//     }
//     // 写入圆心
//     void setCenter(Point center){
//         c_Center = center;
//     }
//     // 读取圆心
//     Point getCenter(){
//         return c_Center;
//     }
// };

// 全局函数判断点是否在圆内
void isinCircle(Circle &c, Point &p){
    // 计算点到圆心的距离平方
    int distance = (c.getCenter().getX() - p.getX()) *
                    (c.getCenter().getX() - p.getX()) + 
                    (c.getCenter().getY() - p.getY()) *
                    (c.getCenter().getY() - p.getY());
    
    // 计算半径的平方
    int rDistance = c.getR() * c.getR();

    // 判断关系
    if(distance == rDistance){
        cout << "ON" << endl;
    }
    else if(distance < rDistance){
        cout << "INSIDE" << endl;
    }
    else if(distance > rDistance){
        cout << "OUTSIDE" << endl;
    }
}




int main() {
    // 创建圆
    Circle c;
    c.setR(10);
    Point Center;
    Center.setX(10);
    Center.setY(0);
    c.setCenter(Center);
    
    // 创建点
    Point p;
    p.setX(10);
    p.setY(11);

    // 调用全局函数判断关系
    isinCircle(c, p);


    return 0;
}