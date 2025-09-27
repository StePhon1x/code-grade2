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




// 题目描述
// 《庄子》中说到，“一尺之棰，日取其半，万世不竭”。第一天有一根长度为 a 的木棍，从第二天开始，每天都要将这根木棍锯掉一半（每次除 2，向下取整）。第几天的时候木棍的长度会变为 1？

// 输入格式
// 输入一个正整数 a，表示木棍长度。

// 输出格式
// 输出一个正整数，表示要第几天的时候木棍长度会变为 1。