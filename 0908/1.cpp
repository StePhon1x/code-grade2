#include <iostream>
using namespace std;

int main() {
    int y, m;
    cin >> y >> m;
    if(m == 1 || m == 3 || 
        m == 5 || m == 7 || 
        m == 8 || m == 10 ||
        m == 12) {
        cout << "31" << endl;
    } else if(m == 4 || m == 6 || 
                m == 9 || m == 11) {
        cout << "30" << endl;
    } else if(m == 2) {
        if((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0)) {
            cout << "29" << endl;
        } else {
            cout << "28" << endl;
        }
    }


    return 0;
}

// 输入年份和月份，输出这一年的这一月有多少天。需要考虑闰年。

// 输入格式
// 输入两个正整数，分别表示年份 y 和月数 m，以空格隔开。

// 输出格式
// 输出一行一个正整数，表示这个月有多少天。