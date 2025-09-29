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