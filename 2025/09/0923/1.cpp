#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int mi = min({a, b, c});
    int mx = max({a, b, c});
    cout << mi / __gcd(mi, mx) << "/" 
            << mx / __gcd(mi, mx) << endl;
    // __gcd 是 C++17 标准引入的,用来计算最大公约数
    return 0;
}


// 题目描述
// 输入一组勾股数 a,b,c（a
// 
// =b
// 
// =c），用分数格式输出其较小锐角的正弦值。（要求约分。）

// 输入格式
// 一行，包含三个正整数，即勾股数 a,b,c（无大小顺序）。

// 输出格式
// 一行，包含一个分数，即较小锐角的正弦值