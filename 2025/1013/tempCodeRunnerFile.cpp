#include <iostream>
using namespace std;

class Person
{
public:
    Person(int age)
    {
        m_Age = new int(age);
    }

~Person(){
        if(m_Age != nullptr){
            delete m_Age;
            m_Age = nullptr;
        }
    }

    int *m_Age;
};

void test01()
{
    Person p1(18);
    cout << *p1.m_Age << endl;
    Person p2(20);
    p2 = p1; // 赋值操作
    cout << *p2.m_Age << endl;
}

int main()
{
    test01();

    return 0;
}