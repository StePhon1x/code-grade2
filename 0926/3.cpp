#include <iostream>
using namespace std;

int main() {
    int a, n=0;
    const int MAX_A = 1000000000;
    // 限制a的输入范围
    while(true){
        cin >> a;
        if(a>=1 && a <= MAX_A){
        break;
        }
    }
    // 计算小于1所需天数
    while(a >= 1){
        a = (int)a / 2;
        n++;
    }
    cout << n << endl;

    return 0;
}