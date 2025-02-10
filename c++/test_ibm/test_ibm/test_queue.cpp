#include <iostream>
#include <queue>
#include <random>
#include "test_queue.h"
using namespace std;

void print_queue() {
    queue<int> q;

    std::random_device rd;  // Fuente de entropía
    std::mt19937 gen(rd()); // Generador Mersenne Twister

    // Definir el rango de los números aleatorios
    std::uniform_int_distribution<> distrib(1, 150);

    q.push(distrib(gen));
    q.push(distrib(gen));
    q.push(distrib(gen));

    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;
}