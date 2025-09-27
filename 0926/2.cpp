#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, k;
    int st=0, sf=0, nt=0, nf=0;
    cin >> n >> k;
    int a[n+1];
    for(int i=1; i<n+1; i++){
        a[i - 1] = i;
        if(a[i - 1] % k == 0){
            st+=a[i - 1];
            nt++;
        }
        else{
            sf+=a[i - 1];
            nf++;
        }
    }
    cout <<fixed <<setprecision(1) 
        << 1.0*st/nt << " " 
        << 1.0*sf/nf << endl;


    return 0;
}






// 题目描述
// 给定 n 和 k，将从 1 到 n 之间的所有正整数可以分为两类：A 类数可以被 k 整除（也就是说是 k 的倍数），而 B 类数不能。请输出这两类数的平均数，精确到小数点后 1 位，用空格隔开。

// 数据保证两类数的个数都不会是 0。

// 输入格式
// 输入两个正整数 n 与 k。

// 输出格式
// 输出一行，两个实数，分别表示 A 类数与 B 类数的平均数。精确到小数点后一位。