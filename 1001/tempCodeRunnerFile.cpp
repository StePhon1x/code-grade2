// 练习案例1：设计立方体类**
// 设计立方体类(Cube)
// 求出立方体的面积和体积
// 分别用全局函数和成员函数判断两个立方体是否相等。
#include <iostream>
using namespace std;

class cube
{
private:
    //属性
    int c_L, c_W, c_H;

public:
    // 写入长
    void setL(int l){
        c_L = l;
    }
    //读取长
    int getL(){
        return c_L;
    }
    // 写入宽
    void setW(int w){
        c_W = w;
    }
    // 读取宽
    int getW(){
        return c_W;
    }
    // 写入高
    void setH(int h){
        c_H = h;
    }
    // 读取高
    int getH(){
        return c_H;
    }
    
    // 计算立方体的面积
    int calculateS(){
        return 2*c_L*c_H + 2*c_L*c_W + 2*c_W*c_H;
    }

    // 计算立方体的体积
    int calculateV(){
        return c_H*c_L*c_W;
    }

    // 利用成员函数判断两个立方体是否相等
    bool isSameByclass(cube &c){
        if(c_L() == c.getL() 
        && c_W() == c.getW() 
        && c_H() == c.getH()){
            return true;
        }
        return false;
    }



};


// 利用全局函数判断两个立方体是否相等
bool isSame(cube &c1, cube &c2){
    if(c1.getL() == c2.getL() 
        && c1.getW() == c2.getW() 
        && c1.getH() == c2.getH()){
            return true;
        }
        return false;
}



int main(){
    cube c1;
    c1.setL(10);
    c1.setW(10);
    c1.setH(10);
    cout /*<< "c1的面积为：" */<< c1.calculateS() << endl;
    cout /*<< "c1的体积为：" */<< c1.calculateV() << endl;
    
    cube c2;
    c2.setL(10);
    c2.setW(10);
    c2.setH(10);
    cout /*<< "c1的面积为：" */<< c2.calculateS() << endl;
    cout /*<< "c1的体积为：" */<< c2.calculateV() << endl;
    
    // bool result = isSame(c1, c2);
    bool result = c1.isSameByclass(c2);
    if(result){
        cout << "is same." << endl; 
    }
    else cout << "not same." << endl;
    
    
    return 0;
}

