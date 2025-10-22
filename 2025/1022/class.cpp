#include <iostream>
#include <string>

using namespace std;

// 打印输出类
class My_Print
{
public:
    // 重载函数调用运算符
    void operator()(string test)
    {
        cout << test << endl;
    }
};

// 加法类
class MyAdd
{
public:
    int operator()(int num1, int num2)
    {
        return num1 + num2;
    }
};

void test01()
{
    My_Print my_Print;
    my_Print("Hello world!"); // 称为仿函数
}

void test02()
{
    MyAdd myadd;
    int res = myadd(100, 120);
    cout << res << endl;

    // 匿名函数对象调用
    cout << MyAdd()(100, 120) << endl;
}

int main()
{
    test01();
    test02();
    return 0;
}