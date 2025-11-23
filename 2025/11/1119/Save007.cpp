#include <iostream>
using namespace std;
#define MaxSize 100

int N, D; // 顶点个数，007能跳的距离

struct coordinate_
{
    int x;
    int y;
} coordinate[MaxSize];

bool Visited[MaxSize] = {false};

bool firstJump(int x, int y)
{
    if (x * x + y * y <= (7.5 + D) * (7.5 + D))
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool Jump(int V, int i) // 非第一跳
{
    int x1 = coordinate[V].x;
    int y1 = coordinate[V].y;
    int x2 = coordinate[i].x;
    int y2 = coordinate[i].y;
    if ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= D * D)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool isSave(int V)
{
    if (coordinate[V].x + D >= 50 || coordinate[V].y + D >= 50 || (coordinate[V].x - D) <= -50 || (coordinate[V].y - D) <= -50)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool DFS(int V)
{
    bool answer = false;
    Visited[V] = true;
    // 首先判断是否可以达到陆地
    if (isSave(V))
    {
        return true;
    }
    else
    {
        for (int i = 0; i < N; i++)
        {
            if (!Visited[i] && Jump(V, i))
            {
                answer = DFS(i);
                if (answer == true)
                {
                    break;
                }
            }
        }
    }
    return answer;
}

void Svave007()
{
    bool answer = false;
    for (int i = 0; i < N; i++)
    {
        if (!Visited[i] && firstJump(coordinate[i].x, coordinate[i].y))
        {
            answer = DFS(i);
            if (answer == true)
            {
                break;
            }
        }
    }
    if (answer == true)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }
}

int main()
{
    scanf("%d %d", &N, &D);

    for (int i = 0; i < N; i++)
    {
        scanf("%d %d", &coordinate[i].x, &coordinate[i].y);
    }

    Svave007();

    return 0;
}