/*
继承

**继承是面向对象三大特性之一**

有些类与类之间存在特殊的关系，例如下图中：

我们发现，定义这些类时，下级别的成员除了拥有上一级的共性，还有自己的特性。

这个时候我们就可以考虑利用继承的技术，减少重复代码
*/

#include <iostream>
using namespace std;

// 公共页面类
class BasePage{
public:
    void header(){
        cout << "首页， 公开课， 。。。" << endl;
    }
    void bottom(){
        cout << "帮助中心， 交流合作。。。" << endl;
    }
    void left(){
        cout << "Java, Python, C++, ..." << endl;
    }

};

// Java类
class Java:public BasePage{
public:
    void content(){
        cout << "Java学科视频" << endl;

    }
};

// Python类
class Python:public BasePage{
public:
    void content(){
        cout << "Python学科视频" << endl;

    }
};

// C++类
class Cpp:public BasePage{
public:
    void content(){
        cout << "C++学科视频" << endl;

    }
};

void test01(){
    cout << "====JAVA====" << endl;

    Java ja;
    ja.header();
    ja.bottom();
    ja.left();
    ja.content();

    cout << "====Python====" << endl;
    
    Python py;
    py.header();
    py.bottom();
    py.left();
    py.content();

    cout << "====C++====" << endl;
    
    Cpp cpp;
    cpp.header();
    cpp.bottom();
    cpp.left();
    cpp.content();
}
int main() {

    test01();

    return 0;
}