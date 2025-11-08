// 加号运算符重载
// 作用：实现两个自定义数据类型相加的运算

#include <iostream>
using namespace std;

class Person
{
public:
    int m_A, m_B;

public:
    Person() {}
    Person(int a, int b)
    {
        this->m_A = a;
        this->m_B = b;
    }
    
    // 成员函数实现运算符重载
    // Person operator+(const Person &p)
    // {
    //     Person temp;
    //     temp.m_A = this->m_A + p.m_A;
    //     temp.m_B = this->m_B + p.m_B;
    //     return temp;
    // }
};

// 全局函数实现运算符重载
Person operator+(const Person &p1, Person &p2){
    Person temp;
    temp.m_A = p1.m_A + p2.m_A;
    temp.m_B = p1.m_B + p2.m_B;
    return temp;
}

// 运算符重载 可以发生函数重载 
Person operator+(const Person &p1, int val){
    Person temp;
    temp.m_A = p1.m_A + val;
    temp.m_B = p1.m_B + val;
    return temp;
}


void test01(){
    Person p1(10,10);
    Person p2(10,10);
    int val = 10;
    Person p3 = p2 + val;
    cout << p3.m_A << endl;
    cout << p3.m_B << endl;
}




int main()
{
    test01();
    return 0;
}
