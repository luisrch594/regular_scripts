#include <iostream>
#include <stack>
#include <random>
#include "test_stack.h"
using namespace std;

void stack_print() {
    stack<int> s;

    std::random_device rd;  // Fuente de entropía
    std::mt19937 gen(rd()); // Generador Mersenne Twister

    // Definir el rango de los números aleatorios
    std::uniform_int_distribution<> distrib(1, 150);

    
    s.push(distrib(gen));
    s.push(distrib(gen));
    s.push(distrib(gen));

    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}