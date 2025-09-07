#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if(a > b){
        swap(a,b);
    }
    if(b > c){
        swap(b,c);
    }
    if(a > b){
        swap(a,b);
    }
    cout<<a<<' '<<b<<' '<<c;
    return 0;
}


// 给出三个整数 a,b,c(0≤a,b,c≤100)，要求把这三位整数从小到大排序。

// 输入格式
// 输入三个整数 a,b,c，以空格隔开。

// 输出格式
// 输出一行，三个整数，表示从小到大排序后的结果。