
// 深拷贝与浅拷贝

// 深浅拷贝是面试经典问题，也是常见的一个坑

// 浅拷贝：简单的赋值拷贝操作
// 深拷贝：在堆区重新申请空间，进行拷贝操作

// 总结：如果属性有在堆区开辟的，一定要自己提供拷贝构造函数，防止浅拷贝带来的问题

#include <iostream>
using namespace std;


class Person
{
    
public:
    int m_age;
    int *m_height;
    Person(){
        cout << "moren" << endl;

    }

    Person(int age, int height){
        m_age = age;
        m_height = new int(height);
        cout << "youcan" << endl;
    }
    ~Person(){
        if(m_height != NULL){
            delete m_height;
            m_height = NULL;
        }
        cout << "xigou" << endl;

    }

    Person(const Person &p){
        cout << "kaobei" << endl;
        m_age = p.m_age;
        m_height = new int(*p.m_height); //深拷贝
    }


};

int main() {
    Person p1(18, 160);
    cout << p1.m_age << *p1.m_height << endl;
    Person p2(p1);
    cout << p2.m_age << *  p2.m_height << endl;


    return 0;
}