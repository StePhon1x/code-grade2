#include <iostream>
using namespace std;

class Person
{
    // 友元函数声明
    friend ostream &operator<<(ostream &out, const Person &p);

private:
    int m_A, m_B;

public:
    Person(int a, int b) : m_A(a), m_B(b) {}
};

// 全局函数实现 << 运算符重载
ostream &operator<<(ostream &out, const Person &p)
{
    out << p.m_A << " " << p.m_B;
    return out; // ✅ 返回 out，支持链式调用
}

void test01()
{
    Person p(10, 20);
    cout << p << endl;
}

int main()
{
    test01();
    return 0;
}
