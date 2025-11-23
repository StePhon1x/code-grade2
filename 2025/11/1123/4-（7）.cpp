#include <stdio.h>
#include <stdbool.h>

#define MAX_VERTEX_NUM 20  // 最大顶点数

// 邻接表节点结构
typedef struct ArcNode {
    int adjvex;  // 邻接顶点在顶点数组中的位置
    struct ArcNode *nextarc;  // 指向下一个邻接节点
} ArcNode;

// 顶点结构
typedef struct VNode {
    int data;  // 顶点数据
    ArcNode *firstarc;  // 指向第一个邻接节点
} VNode, AdjList[MAX_VERTEX_NUM];

// 图结构
typedef struct {
    AdjList vertices;  // 邻接表
    int vexnum, arcnum;  // 顶点数和边数
} Graph;

// 深度优先搜索判断是否存在长度为k的简单路径
bool DFS(Graph *G, int v, int w, int k, int len, bool visited[]) {
    visited[v] = true;  // 标记当前顶点为已访问
    len++;  // 路径长度加1

    // 如果当前顶点是终点且路径长度为k，存在这样的路径
    if (v == w && len == k) {
        return true;
    }

    // 路径长度已达k但未到终点，或未达k但到终点，都不满足，继续遍历邻接顶点
    if (len < k) {
        ArcNode *p = G->vertices[v].firstarc;
        while (p != NULL) {
            if (!visited[p->adjvex]) {  // 若邻接顶点未访问
                if (DFS(G, p->adjvex, w, k, len, visited)) {
                    return true;  // 找到符合条件的路径，返回true
                }
            }
            p = p->nextarc;  // 遍历下一个邻接顶点
        }
    }

    visited[v] = false;  // 回溯，取消当前顶点的已访问标记
    return false;  // 未找到符合条件的路径
}

// 初始化图（此处省略图的创建逻辑，需根据实际需求实现）
void CreateGraph(Graph *G) {
    // 需根据具体输入创建图的邻接表，此处仅为示例框架
    G->vexnum = 0;
    G->arcnum = 0;
    for (int i = 0; i < MAX_VERTEX_NUM; i++) {
        G->vertices[i].firstarc = NULL;
    }
}

// 主函数：判断顶点v到w是否存在长度为k的简单路径
bool HasPath(Graph *G, int v, int w, int k) {
    if (v == w && k == 0) {  // 特殊情况：起点和终点相同且路径长度为0
        return true;
    }
    if (k < 1) {  // 路径长度小于1，不存在（简单路径至少长度为1，顶点不重复）
        return false;
    }

    bool visited[MAX_VERTEX_NUM] = {false};  // 初始化已访问数组
    return DFS(G, v, w, k, 0, visited);
}

int main() {
    Graph G;
    CreateGraph(&G);

    // 假设图已创建，此处测试：顶点0到顶点3，是否存在长度为2的简单路径
    int v = 0, w = 3, k = 2;
    if (HasPath(&G, v, w, k)) {
        printf("顶点 %d 到顶点 %d 存在长度为 %d 的简单路径\n", v, w, k);
    } else {
        printf("顶点 %d 到顶点 %d 不存在长度为 %d 的简单路径\n", v, w, k);
    }

    return 0;
}
