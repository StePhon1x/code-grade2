#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int d[4] = {a, b, c, 0};
    sort(d,d+3);
    // 判断能否构成三角形，不能直接结束。
    if (d[0] + d[1] <= d[2]){
        cout << "Not triangle" << endl;
        return 0;
    }
    // 判断属于直角，钝角，锐角三角形中哪一种。
    if(d[0]*d[0] + d[1]*d[1] == d[2]*d[2]){
        cout << "Right triangle" << endl;
    }
    else if(d[0]*d[0] + d[1]*d[1] > d[2]*d[2]){
        cout << "Acute triangle" << endl;
    }
    else if(d[0]*d[0] + d[1]*d[1] < d[2]*d[2]){
        cout << "Obtuse triangle" << endl;
    }
    // 判断属于等边，等腰三角形哪一种。
    if(d[0] == d[1]){
        cout << "Isosceles triangle" << endl;
    }
    if(d[0] == d[1] && d[1] == d[2]){
        cout << "Equilateral triangle" << endl;
    }

    return 0;
}






// 题目描述
// 给出三条线段 a,b,c 的长度，均是不大于 10000 的正整数。打算把这三条线段拼成一个三角形，它可以是什么三角形呢？

// 如果三条线段不能组成一个三角形，输出Not triangle；
// 如果是直角三角形，输出Right triangle；
// 如果是锐角三角形，输出Acute triangle；
// 如果是钝角三角形，输出Obtuse triangle；
// 如果是等腰三角形，输出Isosceles triangle；
// 如果是等边三角形，输出Equilateral triangle。
// 如果这个三角形符合以上多个条件，请按以上顺序分别输出，并用换行符隔开。

// 输入格式
// 输入 3 个整数 a、b 和 c。

// 输出格式
// 输出若干行判定字符串。