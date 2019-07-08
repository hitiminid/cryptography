#include <iostream>
#include <string>
#include "Field.cpp"
#include <tuple>
#include <cassert>
#include <fstream>

mpz_t modulo;
mpz_class d = -67254;
typedef Field<modulo> FField;
typedef std::pair<FField, FField> Point;

// generator is P

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

Point scalarMultiplication(mpz_class scalar, Point P)
{
    if (scalar == 0)
    {
        return std::make_pair(FField(0), FField(1));
    }

    if (scalar == 1)
    {
        return P;
    }

    Point Q = scalarMultiplication(scalar / 2, P);

    Q = edwardsAddition(Q, Q);

    if (scalar % 2 == 1)
    {
        Q = edwardsAddition(P, Q);
    }
    return Q;
}

bool isOnCurve(Point point)
{
    FField x = point.first;
    FField y = point.second;

    FField result = x * x + y * y - FField(1) - FField(d) * x * x * y * y;

    return result == FField(0);
}

void showPoint(std::string name, Point point)
{
    mpz_class firstValue = point.first.getValue();
    mpz_class secondValue = point.second.getValue();

    std::cout << name << " = (" << firstValue << ", " << secondValue << ")" << std::endl;
}

void generateModulo()
{
    mpz_ui_pow_ui(modulo, 2, 382);
    mpz_sub_ui(modulo, modulo, 105);
}

unsigned long long int getSeed()
{
    unsigned long long int seed;
    std::ifstream random("/dev/random", std::ios::in | std::ios::binary);
    random.read(reinterpret_cast<char *>(&seed), sizeof(seed));
    return seed;
}

Point createBasePoint()
{
    // (x, y)
    // x = 3914921414754292646847594472454013487047137431784830634731377862923477302047857640522480241298429278603678181725699
    // y = 17

    mpz_class x;
    x = "3914921414754292646847594472454013487047137431784830634731377862923477302047857640522480241298429278603678181725699";
    return std::make_pair(FField(x), FField(17));
}

mpz_class generatePrivateKey(gmp_randclass &rand)
{
    return rand.get_z_range(mpz_class(modulo));
}

Point generatePublicKey(mpz_class a, Point P)
{
    Point A = scalarMultiplication(a, P);
    return A;
}

Point generateMessage(Point P, gmp_randclass &r)
{
    mpz_class scalarMessage = r.get_z_range(mpz_class(modulo));
    Point message = scalarMultiplication(scalarMessage, P);
    return message;
}

std::pair<Point, Point> encrypt(Point message, Point generator, Point pubKey, gmp_randclass &rand)
{
    mpz_class k = rand.get_z_range(mpz_class(modulo));
    Point Q = scalarMultiplication(k, generator);
    Point kR = scalarMultiplication(k, pubKey);
    Point crypto = edwardsAddition(message, kR); // (m1, m2) == (M1x', M2y')
    return std::make_pair(Q, crypto);
}

Point decrypt(Point Q, Point crypto, mpz_class privKey)
{
    Point aQ = scalarMultiplication(privKey, Q);
    Point minus_aQ = std::make_pair(-aQ.first, aQ.second);
    return edwardsAddition(minus_aQ, crypto);
}

void performAssertion(Point message, Point decryptedMessage)
{
    assert(message.first == decryptedMessage.first && message.second == decryptedMessage.second);
}

//EEC x^2 + y^2 = 1 + d*x^2y^2

//E-382
// x^2+y^2 = 1-67254x^2y^2
// modulo p = 2^382 - 105

int main(int argc, char const *argv[])
{
    // 0. Init
    generateModulo();
    gmp_randclass r(gmp_randinit_default);
    r.seed(getSeed());

    // 1. Create a base point
    Point P = createBasePoint();

    // 2. Generate private and public keys
    mpz_class a = generatePrivateKey(r);
    Point A = generatePublicKey(a, P);

    // 3. Generate the message
    Point message = generateMessage(P, r);

    // 4. Perform encryption
    auto [Q, crypto] = encrypt(message, P, A, r);

    // 4. Perform decryption
    Point decryptedMessage = decrypt(Q, crypto, a);

    performAssertion(message, decryptedMessage);

    // 5. Logs
    // std::cout << "##################################" << std::endl;
    // showPoint("Message", message);
    // std::cout << std::endl;

    // std::cout << "##################################" << std::endl;
    // showPoint("Cryptogram", crypto);
    // std::cout << std::endl;

    // std::cout << "##################################" << std::endl;
    // showPoint("Decrypted Message", decryptedMessage);
}