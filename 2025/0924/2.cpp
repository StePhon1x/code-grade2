#include <iostream>
#include <algorithm>
using namespace std;
int p[3];
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    char i, j, k;
    cin >> i >> j >> k;
    p[0] = min({a, b, c});
    p[2] = max({a, b, c});
    int x = max(a, b);
    int y = max(b, c);
    int z = max(a, c);
    if (x == y){
        p[1] = z;
    }
    if (x == z){
        p[1] = y;
    }
    if(y == z){
        p[1] = x;
    }
    cout << p[i - 'A'] << " "  
        << p[j - 'A'] << " " 
        << p[k - 'A'] << endl;
    return 0;
}


// 题目描述
// 三个整数分别为 A,B,C。这三个数字不会按照这样的顺序给你，但它们始终满足条件：A<B<C。为了看起来更加简洁明了，我们希望你可以按照给定的顺序重新排列它们。

// 输入格式
// 第一行包含三个正整数 A,B,C，不一定是按这个顺序。这三个数字都小于或等于 100。第二行包含三个大写字母 A、B 和 C（它们之间没有空格）表示所需的顺序。

// 输出格式
// 在一行中输出 A，B 和 C，用一个 （空格）隔开。
