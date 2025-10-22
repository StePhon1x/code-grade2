#include <iostream>
using namespace std;

// 宏定义与结构定义 
#define LIST_SIZE 20   // 线性表最大容量
#define OK 0
#define ERROR -1

typedef int STATUS;    // 状态类型

// 定义顺序表结构体
typedef struct SeqList {
    int data[LIST_SIZE];  // 存放数据的数组
    int length;           // 当前线性表长度
} SeqList;

// 函数声明
STATUS InsertList(SeqList *L, int i, int x);     // 插入
STATUS DeleteList(SeqList *L, int i, int *mydata); // 删除
STATUS SearchList(SeqList *L, int i, int *mydata); // 查找
void PrtList(SeqList *L);                         // 输出
void InitList(SeqList *L);                        // 初始化
void DestroyList(SeqList *L);                     // 销毁线性表

// ======= 函数实现 =======

// 初始化线性表
void InitList(SeqList *L) {
    L->length = 0;
    cout << "线性表已初始化为空表！" << endl;
}

// 插入函数：在第i个位置插入数据x
STATUS InsertList(SeqList *L, int i, int x) {
    if (L->length >= LIST_SIZE) {
        cout << "线性表已满，无法插入！" << endl;
        return ERROR;
    }
    if (i < 1 || i > L->length + 1) {
        cout << "插入位置 " << i << " 非法！" << endl;
        return ERROR;
    }

    // 元素后移
    for (int j = L->length; j >= i; j--) {
        L->data[j] = L->data[j - 1];
    }

    L->data[i - 1] = x;  // 插入元素
    L->length++;
    cout << "成功在位置 " << i << " 插入元素 " << x << "！" << endl;
    return OK;
}

// 删除函数：删除第i个元素，用mydata返回删除的值
STATUS DeleteList(SeqList *L, int i, int *mydata) {
    if (L->length == 0) {
        cout << "线性表为空，无法删除！" << endl;
        return ERROR;
    }
    if (i < 1 || i > L->length) {
        cout << "删除位置 " << i << " 非法！" << endl;
        return ERROR;
    }

    *mydata = L->data[i - 1];
    for (int j = i - 1; j < L->length - 1; j++) {
        L->data[j] = L->data[j + 1];
    }
    L->length--;
    cout << "成功删除第 " << i << " 个元素，值为 " << *mydata << "。" << endl;
    return OK;
}

// 查找函数：查找第i个元素，并返回其值
STATUS SearchList(SeqList *L, int i, int *mydata) {
    if (i < 1 || i > L->length) {
        cout << "查找位置 " << i << " 非法！" << endl;
        return ERROR;
    }
    *mydata = L->data[i - 1];
    cout << "第 " << i << " 个元素的值为 " << *mydata << "。" << endl;
    return OK;
}

// 打印线性表
void PrtList(SeqList *L) {
    if (L->length == 0) {
        cout << "线性表为空！" << endl;
        return;
    }
    cout << "当前线性表内容：";
    for (int i = 0; i < L->length; i++) {
        cout << L->data[i] << " ";
    }
    cout << endl;
}

// 销毁线性表
void DestroyList(SeqList *L) {
    L->length = 0;
    cout << "线性表已销毁（重置为空）！" << endl;
}

// 主函数测试 
int main() {
    SeqList L;
    int x, pos;
    STATUS s;

    InitList(&L);

    // 插入数据
    InsertList(&L, 1, 10);
    InsertList(&L, 2, 20);
    InsertList(&L, 3, 30);
    PrtList(&L);

    // 删除操作
    int deleted;
    DeleteList(&L, 2, &deleted);
    PrtList(&L);

    // 查找操作
    int found;
    SearchList(&L, 1, &found);

    // 测试非法位置
    InsertList(&L, -1, 999); // 错误插入
    DeleteList(&L, 10, &deleted); // 错误删除

    // 销毁线性表
    DestroyList(&L);
    PrtList(&L);

    return 0;
}