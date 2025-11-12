#include <iostream>
using namespace std;

// 抽象CPU类
class CPU
{
public:
    // 抽象的计算函数
    virtual void calculate() = 0;
};

// 抽象显卡类
class VideoCard
{
public:
    // 抽象的计算函数
    virtual void display() = 0;
};

// 抽象内存类
class Memory
{
public:
    // 抽象的计算函数
    virtual void storyage() = 0;
};

// 电脑类
class Computer
{
public:
    Computer(CPU *cpu, VideoCard *vc, Memory *mem)
    {
        m_cpu = cpu;
        m_vc = vc;
        m_mem = mem;
    }

    // 工作函数
    void work()
    {
        // 让零件工作起来， 调用接口
        m_cpu->calculate();
        m_vc->display();
        m_mem->storyage();
        cout << "电脑正在运行！" << endl;
    }

    // 电脑零件的析构函数
    ~Computer()
    {
        if (m_cpu != nullptr)
        {
            delete m_cpu;
            m_cpu = nullptr;
        }

        if (m_vc != nullptr)
        {
            delete m_vc;
            m_vc = nullptr;
        }

        if (m_mem != nullptr)
        {
            delete m_mem;
            m_mem = nullptr;
        }
    }

private:
    CPU *m_cpu;      // CPU的零件指针
    VideoCard *m_vc; // 显卡的零件指针
    Memory *m_mem;   // 内存的零件指针
};

// Intel 厂商零件
// Intel的CPU类
class IntelCPU : public CPU
{
    void calculate()
    {
        cout << "Intel 的CPU开始计算了" << endl;
    }
};

// Intel 的显卡类
class IntelVideoCard : public VideoCard
{
    void display()
    {
        cout << "Intel 的显卡开始运行了" << endl;
    }
};

// Intel 的内存类
class IntelMemory : public Memory
{
    void storyage()
    {
        cout << "Intel 的内存开始存储了" << endl;
    }
};

// Lenovo 厂商零件
// Lenovo的CPU类
class LenovoCPU : public CPU
{
    void calculate()
    {
        cout << "lenovo 的CPU开始计算了" << endl;
    }
};

// Lenovo的显卡类
class LenovoVideoCard : public VideoCard
{
    void display()
    {
        cout << "lenovo 的显卡开始运行了" << endl;
    }
};

// Lenovo的内存类
class LenovoMemory : public Memory
{
    void storyage()
    {
        cout << "lenovo 的内存开始存储了" << endl;
    }
};

void test01()
{

    // 第一台电脑零件
    CPU *intel_cpu = new IntelCPU;
    VideoCard *intel_vc = new IntelVideoCard;
    Memory *intel_mem = new IntelMemory;

    // 第一台电脑
    Computer *c1 = new Computer(intel_cpu, intel_vc, intel_mem);
    c1->work();
    delete c1;

    cout << "==============================" << endl;

    // 第二台电脑零件
    CPU *lenovo_cpu = new LenovoCPU;
    VideoCard *lenovo_vc = new LenovoVideoCard;
    Memory *lenovo_mem = new LenovoMemory;

    // 第二台电脑
    Computer *c2 = new Computer(lenovo_cpu, lenovo_vc, lenovo_mem);
    c2->work();
    delete c2;

    cout << "==============================" << endl;

    // 第三台电脑
    Computer *c3 = new Computer(new IntelCPU, new LenovoVideoCard, new LenovoMemory);
    c3->work();
    delete c3;
}

int main()
{
    test01();

    return 0;
}