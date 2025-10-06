// 递增运算符重载
// 作用： 通过重载递增运算符，实现自己的整型数据


#include <iostream>
using namespace std;

class Integer
{
    friend ostream& operator<<(ostream &out, const Integer &i);
public:
    Integer(){
        m_num = 0;
    }
    
    // 重载前置--
    Integer& operator--(){
    --(this->m_num);
    return *this;
    }

    // 重载后置--
    Integer operator--(int){
        Integer temp = *this;
        (this->m_num)--;
        return temp;
    }


private:
    int m_num; 
};




ostream& operator<<(ostream &out, const Integer &i){
    out << i.m_num;
    return out;
}

void test01(){
    Integer i;
    cout << --i << endl;
    cout << i << endl;

}


int main() {
    test01();


    return 0;
}