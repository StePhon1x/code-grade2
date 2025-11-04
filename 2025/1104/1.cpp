#include <iostream>
using namespace std;

bool tree[10002];

int main()
{
    int l, m, sum = 0;
    cin >> l >> m;

    for (int i = 0; i < m; i++)
    {
        int le, ri;
        cin >> le >> ri;

        for (int j = le; j <= ri; j++)
        {
            if (tree[j] == 0)
            {
                sum++;
                tree[j] = 1;
            }
        }
    }

    cout << l + 1 - sum << endl;

    return 0;
}