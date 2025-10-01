// 将所有成员属性设置为私有，可以自己控制读写权限
// 对于写权限，我们可以检测数据的有效性

#include <iostream>
#include <string>
using namespace std;

class Person
{
    private:
    string m_Name; //姓名 可读可写
    int m_Age; //年龄 只读 也可以写但是必须是0~·50之间
    string m_Idol; //偶像 只写

    public:
    // 写入姓名
    void setName(string name){
        m_Name = name;
    }
    // 读取姓名
    string getName(){
        return m_Name;
    }

    // 写入年龄（0~150）
    void setAge(int age){
        if(age < 0 || age > 150){
            cout << "年龄输入错误，赋值失败。" << endl;
            return;
        }
        m_Age = age;
    }
    // 读取年龄
    int getAge(){
        return m_Age;
    }
    

    // 写入偶像
    void setIdol(string idol){
        m_Idol = idol;
    }
};

int main(){
    
    Person p;
    p.setName("郑金煜");
    cout << "姓名是:" << p.getName() << endl;
    p.setAge(169);
    cout << "年龄:" << p.getAge();
    p.setIdol("zjy");
    // cout << "idol:" << p.setIdol();
    
    return 0;
}









