#include <iostream>
#include <vector>
#include <unordered_map>
#include <iomanip>
#include <algorithm>
using namespace std;

struct Node {
    int address, data, next;
};

int main() {
    int first, N, K;
    cin >> first >> N >> K;

    unordered_map<int, Node> nodes;
    for (int i = 0; i < N; i++) {
        int addr, data, next;
        cin >> addr >> data >> next;
        nodes[addr] = {addr, data, next};
    }

    // 构造实际链表顺序
    vector<Node> list;
    for (int p = first; p != -1; p = nodes[p].next) {
        list.push_back(nodes[p]);
    }

    // 按K分组反转
    for (int i = 0; i + K <= (int)list.size(); i += K) {
        reverse(list.begin() + i, list.begin() + i + K);
    }

    // 重新连接next指针并输出
    cout << "=============" << endl;
    for (int i = 0; i < (int)list.size(); i++) {
        if (i < (int)list.size() - 1)
            list[i].next = list[i + 1].address;
        else
            list[i].next = -1;

        cout << setw(5) << setfill('0') << list[i].address << " "
            << list[i].data << " ";
        if (list[i].next == -1)
            cout << -1 << endl;
        else
            cout << setw(5) << setfill('0') << list[i].next << endl;
    }

    return 0;
}
