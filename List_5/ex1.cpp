#include <iostream>
#include "Field.cpp"
#include <cassert>

mpz_t modulo;
mpz_class d;

typedef Field<modulo> FField;
typedef std::pair<FField, FField> Point;

Point edwardsAddition(const Point firstPoint, const Point secondPoint)
{
    FField x1 = firstPoint.first;
    FField y1 = firstPoint.second;

    FField x2 = secondPoint.first;
    FField y2 = secondPoint.second;

    FField x = (x1 * y2 + x2 * y1) / (FField(1) + FField(d) * x1 * x2 * y1 * y2);
    FField y = (y1 * y2 - x1 * x2) / (FField(1) - FField(d) * x1 * x2 * y1 * y2);
    return std::make_pair(x, y);
}

void initModulo(long long value)
{
    mpz_init_set_ui(modulo, value);
}

void showPoint(Point point)
{
    mpz_class firstValue = point.first.getValue();
    mpz_class secondValue = point.second.getValue();

    std::cout << "Point = (" << firstValue << ", " << secondValue << ")" << std::endl;
}

int main(int argc, char const *argv[])
{
    initModulo(1009);
    d = -11;
    Point P1 = std::make_pair(FField(7), FField(415));
    Point P2 = std::make_pair(FField(23), FField(487));
    Point output = edwardsAddition(P1, P2);

    showPoint(output);

    assert(output.first == 944 && output.second == 175);

    output = edwardsAddition(P2, P1);

    assert(output.first == 944 && output.second == 175);
}
