#include <iostream>
using namespace std;

int main() {
    int n;
    while(true){
        cout << "Please input n (1<=n<=13): ";
        cin >> n;
        if(n>=1 && n<=13) break;
        else cout << "Input range error, please re-enter." << endl;
    }
    int c = 1;
    for(int i=n; i>=1; i--) {
        for(int j=1; j<=i; j++) {
            if(c<10){
                cout << "0" << c;
                c++;
            }
            else{
                cout << c;
                c++;
            }
        }
    cout << endl;
    }


    return 0;
}


// 题目描述
// 给出 n，请输出一个直角边长度是 n 的数字直角三角形。所有数字都是 2 位组成的，如果没有 2 位则加上前导 0。

// 输入格式
// 输入一个正整数 n。

// 输出格式
// 输出如题目要求的数字直角三角形。