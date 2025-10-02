#include <iostream>
using namespace std;
int n;
int main() {
    cin >> n;
    int a[n+1], mina;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    mina = a[0];
    for(int i=0; i<n; i++){
        if(a[i] < mina){
            mina = a[i];
        }
    }
    cout << mina << endl;

    return 0;
}


// 题目描述
// 给出 n 和 n 个整数 a 
// i
// ​
//  ，求这 n 个整数中最小值是什么。

// 输入格式
// 第一行输入一个正整数 n，表示数字个数。

// 第二行输入 n 个非负整数，表示 a 
// 1
// ​
//  ,a 
// 2
// ​
//  …a 
// n
// ​
//  ，以空格隔开。

// 输出格式
// 输出一个非负整数，表示这 n 个非负整数中的最小值。