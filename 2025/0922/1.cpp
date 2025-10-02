#include <iostream>
using namespace std;

int main() {
    int x, n, g=0;
    cin >> x >> n;
    for(int i=1; i<=n; i++){
        if(x!=6 && x!=7){
            g += 250;           
        }
        x++; 
        if (x > 7){
            x  = 1;
        }
    }
    cout << g << endl;

    return 0;
}



// 题目描述
// 有一只小鱼，它平日每天游泳 250 公里，周末休息（实行双休日)，假设从周 x 开始算起，过了 n 天以后，小鱼一共累计游泳了多少公里呢？

// 输入格式
// 输入两个正整数 x,n，表示从周 x 算起，经过 n 天。

// 输出格式
// 输出一个整数，表示小鱼累计游泳了多少公里。