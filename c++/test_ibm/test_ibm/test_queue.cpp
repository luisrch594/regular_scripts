#include <iostream>
#include <queue>
#include <random>
#include "test_queue.h"
using namespace std;

void print_queue() {
    queue<int> q;

    std::random_device rd;  // Fuente de entrop�a
    std::mt19937 gen(rd()); // Generador Mersenne Twister

    // Definir el rango de los n�meros aleatorios
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