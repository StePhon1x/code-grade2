/*
**菱形继承概念：**
​	两个派生类继承同一个基类
​	又有某个类同时继承者两个派生类
​	这种继承被称为菱形继承，或者钻石继承

**菱形继承问题：**
1. 羊继承了动物的数据，驼同样继承了动物的数据，当草泥马使用数据时，就会产生二义性。

2. 草泥马继承自动物的数据继承了两份，其实我们应该清楚，这份数据我们只需要一份就可以。
*/

#include <iostream>
using namespace std;

// 动物类
class Animal
{
public:
    int m_Age;
};

// 利用虚继承 解决菱形继承的问题
// 在继承前加上关键字 Virtual 变为虚继承
// Animal类称为虚基类

// 羊类
class Sheep : virtual public Animal
{
};

// 骆驼类
class Camel : virtual public Animal
{
};

// 羊驼类
class SheepCamel : public Sheep, public Camel
{
};

void test01()
{
    SheepCamel sc;

    sc.Sheep::m_Age = 18;
    sc.Camel::m_Age = 28;

    // 当菱形继承时， 两个父类有相同的数据， 需要加以作用域区分
    cout << "sc.Sheep::m_Age = " << sc.Sheep::m_Age << endl;
    cout << "sc.Camel::m_Age = " << sc.Camel::m_Age << endl;
    cout << "sc.m_Age = " << sc.m_Age << endl;

    // 这份数据多余了一份 资源浪费
}

int main()
{
    test01();

    return 0;
}