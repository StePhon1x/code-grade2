// 两种分类方式：
// 按参数分为： 有参构造和无参构造
// 按类型分为： 普通构造和拷贝构造

// 三种调用方式：
// ​括号法
// ​显示法
// ​隐式转换法

#include <iostream>
using namespace std;

class Person
{
    int age;
    
    // 有参构造函数 普通构造
    Person(int a){
        age = a;
    }

    // 拷贝构造函数 
    Person(const Person &p){
        age = p.age;
    }
};





int main() {



    return 0;
}