#include <iostream>
using namespace std;
class Person
{
public:
    Person(string name, int age){
        p_name = name;
        p_age = age;
    }

    string p_name;
    int p_age;

    // 重载==
    bool operator==(const Person &p){
        if(this->p_name == p.p_name 
            && this->p_age == p.p_age){
                return true;
            }
        return false;
    }

    // 重载!=
    bool operator!=(const Person &p){
        if(this->p_name != p.p_name 
            || this->p_age != p.p_age){
                return true;
            }
        return false;

    }

};

void test01(){
    Person p1("Tom", 18);
    Person p2("Alice", 18);
    
    if(p1 == p2){
        cout << "==" << endl;
    }
    else{
        cout << "!=" << endl;
    }
    
    if(p1 != p2){
        cout << "!=" << endl;
    }
    else{
        cout << "==" << endl;
    }

}



int main() {
    test01();


    return 0;
}