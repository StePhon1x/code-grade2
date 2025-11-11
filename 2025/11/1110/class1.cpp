#include <iostream>
using namespace std;
class Drink
{   
    public:
    virtual void Water() = 0;
    virtual void Push() = 0;
    virtual void Pull() = 0;
    virtual void Add() = 0;
    void MakeDrink(){
        Water();
        Push();
        Pull();
        Add();

    }

};

class Coffee : public Drink
{
    virtual void Water(){
        cout << "Add kuangquanshui" << endl;
    }
    virtual void Push(){
        cout << "Add dou" << endl;
    }
    virtual void Pull(){
        cout << "Pull coffee bottle" << endl;
    }
    virtual void Add(){
        cout << "Add milk" << endl;
    }
};  

class Tea : public Drink
{
    virtual void Water(){
        cout << "Add boil water" << endl;
    }
    virtual void Push(){
        cout << "Add chaye" << endl;
    }
    virtual void Pull(){
        cout << "Pull Tea bottle" << endl;
    }
    virtual void Add(){
        cout << "Add gouqi" << endl;
    }
};

void doDrink(Drink *abc){
    abc -> MakeDrink();
    delete abc;
    abc = nullptr;
}

void test01(){
    doDrink(new Coffee); 
    cout << "=======" << endl;
    doDrink(new Tea);

}
int main() {
    test01();


    return 0;
}