#include <iostream>
using namespace std;

int main() {
    int k, n;
    double S=0;
    cin >> k;
    for(int i=1; S<=k; i++){
        S += 1.0/i;
        n = i;
    }
    cout << n << endl;

    return 0;
}

// 题目描述
// 已知：S_n = 1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n}
// ​显然对于任意一个整数 k，当 n 足够大的时候，S_n > k。

// 现给出一个整数 k，要求计算出一个最小的 n，使得 S_n >k。

// 输入格式
// 一个正整数 k。

// 输出格式
// 一个正整数 n。
