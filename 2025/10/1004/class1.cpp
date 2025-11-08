// 类做友元

#include <iostream>
#include <string>
using namespace std;



class Building
{
    friend class GoodGay; // 友元GoodGay类
public:
    string m_SittingRoom; // 客厅

    Building();

private: 
    string m_BedRoom; // 卧室
};

class GoodGay
{
public:
    GoodGay();

    void visit(); // 参观函数 访问Building中的属性

private:
    Building *building;
};

// 类外写成员函数
Building::Building()
{
    m_SittingRoom = "ke ting";
    m_BedRoom = "wo shi";
}

GoodGay::GoodGay()
{
    // 创建建筑物对象
    building = new Building;
}

void GoodGay::visit()
{
    cout << "zhengzai visit: " << building->m_SittingRoom << endl;
    cout << "zhengzai visit: " << building->m_BedRoom << endl;
}

void test01()
{
    GoodGay gg;
    gg.visit();
}

int main()
{
    test01();

    return 0;
}