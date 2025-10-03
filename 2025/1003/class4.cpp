
// 初始化列表
// 作用：
// C++提供了初始化列表语法，用来初始化属性
// 语法：构造函数()：属性1(值1),属性2（值2）... {}



#include <iostream>
using namespace std;

class Person
{
public:
    int p_a, p_b, p_c;
    Person(int a, int b, int c) : p_a(a), p_b(b), p_c(c)
    {
    }
};

int main()
{
    Person p(10, 20, 30);
    cout << p.p_a << p.p_b << p.p_c;
    return 0;
}