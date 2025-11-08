#include <iostream>
using namespace std;

int main() {
    long long n, x, a, b, t=0;
    while(1){
        cin >> n >> x;
        if(n>=1 && n<=10000000 && x>=0 && x<=9) break;
        else cout << "Input again:";
    }   
    for(int i=1; i<=n; i++){
        a = i;
        while(a>0){
            b = a % 10;
            a = a / 10;
            if(b == x){
                t++;
            }
        }
    }
    cout << t << endl;


    return 0;
}









// 题目背景
// NOIP2013 普及组 T1

// 题目描述
// 试计算在区间 1 到 n 的所有整数中，数字 x（0≤x≤9）共出现了多少次？例如，在 1 到 11 中，即在 1,2,3,4,5,6,7,8,9,10,11 中，数字 1 出现了 4 次。

// 输入格式
// 2 个整数 n,x，之间用一个空格隔开。

// 输出格式
// 1 个整数，表示 x 出现的次数。