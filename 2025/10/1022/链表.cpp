#include <iostream>
using namespace std;

// 宏与类型定义 
#define OK 0
#define ERROR -1
typedef int STATUS;

// 定义链表节点
typedef struct Node {
    int data;           // 节点数据
    struct Node *next;  // 指针域
} Node, *LinkList;

// 函数声明 
LinkList LinkInit();                         // 初始化链表（带头结点）
STATUS LinkInsert(LinkList H, int e, int i); // 在第i个结点之后插入值为e的结点
STATUS LinkDele(LinkList H, int e);          // 删除值为e的结点
Node *LinkFindi(LinkList H, int i);          // 按序号查找节点
Node *LinkFinde(LinkList H, int e);          // 按值查找节点
void LinkPrint(LinkList H);                  // 输出链表

// 函数实现 

// 初始化单链表
LinkList LinkInit() {
    LinkList H = new Node;
    H->next = NULL;
    cout << "链表初始化成功！" << endl;
    return H;
}

// 在第i个结点之后插入值为e的新结点
STATUS LinkInsert(LinkList H, int e, int i) {
    Node *p = H;
    int j = 0;
    while (p && j < i) {
        p = p->next;
        j++;
    }
    if (!p) {
        cout << "插入失败：第 " << i << " 个结点不存在！" << endl;
        return ERROR;
    }
    Node *s = new Node;
    s->data = e;
    s->next = p->next;
    p->next = s;
    cout << "在第 " << i << " 个结点之后插入值为 " << e << " 的新结点成功！" << endl;
    return OK;
}

// 删除值为e的结点
STATUS LinkDele(LinkList H, int e) {
    Node *p = H->next;
    Node *pre = H;
    while (p && p->data != e) {
        pre = p;
        p = p->next;
    }
    if (!p) {
        cout << "未找到值为 " << e << " 的结点，删除失败！" << endl;
        return ERROR;
    }
    pre->next = p->next;
    delete p;
    cout << "删除值为 " << e << " 的结点成功！" << endl;
    return OK;
}

// 按序号查找节点（返回指针）
Node *LinkFindi(LinkList H, int i) {
    Node *p = H->next;
    int j = 1;
    while (p && j < i) {
        p = p->next;
        j++;
    }
    if (!p) {
        cout << "查找失败：第 " << i << " 个元素不存在！" << endl;
        return NULL;
    }
    cout << "第 " << i << " 个结点的值为 " << p->data << endl;
    return p;
}

// 按值查找节点（返回指针）
Node *LinkFinde(LinkList H, int e) {
    Node *p = H->next;
    while (p && p->data != e) {
        p = p->next;
    }
    if (!p) {
        cout << "未找到值为 " << e << " 的结点！" << endl;
        return NULL;
    }
    cout << "找到值为 " << e << " 的结点！" << endl;
    return p;
}

// 输出链表内容
void LinkPrint(LinkList H) {
    Node *p = H->next;
    if (!p) {
        cout << "链表为空！" << endl;
        return;
    }
    cout << "当前链表内容：";
    while (p) {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
}

// 主函数测试 
int main() {
    LinkList H = LinkInit();

    // 创建一些节点
    Node *p1 = new Node{10, NULL};
    Node *p2 = new Node{20, NULL};
    Node *p3 = new Node{30, NULL};
    H->next = p1;
    p1->next = p2;
    p2->next = p3;
    LinkPrint(H);

    // 插入操作
    LinkInsert(H, 25, 2);
    LinkPrint(H);

    // 删除操作
    LinkDele(H, 20);
    LinkPrint(H);

    // 按序号查找
    LinkFindi(H, 2);

    // 按值查找
    LinkFinde(H, 25);

    return 0;
}
