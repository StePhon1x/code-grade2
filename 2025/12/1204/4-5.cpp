#include <iostream>
#include <vector>
#include <algorithm> // 包含 std::swap

/**
 * @brief 将线性表（此处用std::vector表示）中的负整数和正整数分开。
 * 负数在前，正数在后，不要求排序，尽量减少交换次数。
 * * @param arr 待处理的整数向量。
 */
void separateNegativesAndPositives(std::vector<int>& arr) {
    // 数组为空或只有一个元素时，无需操作
    if (arr.empty() || arr.size() < 2) {
        return;
    }

    int left = 0;
    int right = arr.size() - 1;
    int swap_count = 0; // 用于统计交换次数

    // 当 left < right 时，表示两指针还未相遇或交错
    while (left < right) {
        
        // 1. left 指针从左向右移动，跳过所有负数（arr[left] < 0）
        // 负数已经就位，不需要交换。
        while (left < right && arr[left] < 0) {
            left++;
        }

        // 2. right 指针从右向左移动，跳过所有正数（arr[right] > 0）
        // 正数已经就位，不需要交换。
        while (left < right && arr[right] > 0) {
            right--;
        }

        // 3. 如果 left 仍然小于 right，说明 left 找到了一个错位的正数，
        //    right 找到了一个错位的负数，进行交换。
        if (left < right) {
            // 使用 std::swap 进行交换
            std::swap(arr[left], arr[right]);
            swap_count++;

            // 交换完成后，两个指针都向前/向后移动一步
            left++;
            right--;
        }
    }
    
    // 打印交换次数（可选）
    std::cout << "总共进行了 " << swap_count << " 次交换。" << std::endl;
}

// 辅助函数：打印向量内容
void printVector(const std::vector<int>& arr) {
    std::cout << "[";
    for (size_t i = 0; i < arr.size(); ++i) {
        std::cout << arr[i] << (i == arr.size() - 1 ? "" : ", ");
    }
    std::cout << "]" << std::endl;
}

// 示例用法
int main() {
    std::vector<int> list1 = {1, -2, 5, -8, 0, 9, -3, 6, -10};
    std::cout << "原始列表 1: ";
    printVector(list1);

    separateNegativesAndPositives(list1);

    std::cout << "处理后列表 1: ";
    printVector(list1);
    
    std::cout << "\n------------------\n";

    std::vector<int> list2 = {-5, -1, 3, 2, -4, 6};
    std::cout << "原始列表 2: ";
    printVector(list2);

    separateNegativesAndPositives(list2);

    std::cout << "处理后列表 2: ";
    printVector(list2);

    return 0;
}