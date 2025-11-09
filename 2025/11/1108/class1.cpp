// 多态的优点：

// * 代码组织结构清晰
// * 可读性强
// * 利于前期和后期的扩展以及维护

#include <iostream>
using namespace std;

// 抽象计算器类
class Abstract_Calculator
{
public:
    virtual int getResult() = 0;

    int m_Num1, m_Num2;
};

// 加法计算器
class AddCalculator : public Abstract_Calculator
{
    int getResult() override
    {
        return m_Num1 + m_Num2;
    }
};

// 减法计算器
class SubCalculator : public Abstract_Calculator
{
    int getResult() override
    {
        return m_Num1 - m_Num2;
    }
};

// 乘法计算器
class MulCalculator : public Abstract_Calculator
{
    int getResult() override
    {
        return m_Num1 * m_Num2;
    }
};

// 除法计算器
class ChuCalculator : public Abstract_Calculator
{
    int getResult() override
    {
        return m_Num1 / m_Num2;
    }
};

void test01()
{
    // 加法运算
    Abstract_Calculator *abc = new AddCalculator;
    abc->m_Num1 = 10;
    abc->m_Num2 = 10;

    cout
        << abc->m_Num1
        << " + " << abc->m_Num2
        << " = " << abc->getResult()
        << endl;

    // 用完记得销毁
    delete abc;
    abc = nullptr;

    // 减法运算
    abc = new SubCalculator;
    abc->m_Num1 = 100;
    abc->m_Num2 = 109;

    cout
        << abc->m_Num1
        << " - " << abc->m_Num2
        << " = " << abc->getResult()
        << endl;

    // 用完记得销毁
    delete abc;
    abc = nullptr;

    // 乘法运算
    abc = new MulCalculator;
    abc->m_Num1 = 100;
    abc->m_Num2 = 2;

    cout
        << abc->m_Num1
        << " * " << abc->m_Num2
        << " = " << abc->getResult()
        << endl;

    // 用完记得销毁
    delete abc;
    abc = nullptr;

    // 除法运算
    abc = new ChuCalculator;
    abc->m_Num1 = 100;
    abc->m_Num2 = 50;

    cout
        << abc->m_Num1
        << " / " << abc->m_Num2
        << " = " << abc->getResult()
        << endl;

    // 用完记得销毁
    delete abc;
    abc = nullptr;
}
int main()
{
    test01();
    return 0;
}

// 总结：C++开发提倡利用多态设计程序架构，因为多态优点很多