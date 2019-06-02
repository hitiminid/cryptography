#include <iostream>
#include "Field.cpp"
#include <tuple>
#include <cassert>
#include <fstream>

mpz_t modulo;
mpz_class d = -67254;
typedef Field<modulo> Number;
typedef std::pair<Number, Number> Point;

// generator is P
// TODO: extract to utils
// TODO: change assertion
// TODO:

Point edwardsAddition(const Point firstPoint, const Point secondPoint)
{
    auto [x1, y1] = firstPoint;
    auto [x2, y2] = secondPoint;
    Number x = (x1 * y2 + x2 * y1) / (Number(1) + Number(d) * x1 * x2 * y1 * y2);
    Number y = (y1 * y2 - x1 * x2) / (Number(1) - Number(d) * x1 * x2 * y1 * y2);
    return std::make_pair(x, y);
}

Point scalarMultiplication(mpz_class scalar, Point P)
{
    if (scalar == 0)
    {
        return std::make_pair(Number(0), Number(1));
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
    Number x = point.first;
    Number y = point.second;

    Number result = x * x + y * y - Number(1) - Number(d) * x * x * y * y;

    return result == Number(0);
}

void printPoint(Point point)
{
    std::cout << point.first.getValue() << " " << point.second.getValue() << std::endl;
}

void log()
{
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
    return std::make_pair(Number(x), Number(17));
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

std::tuple<Point, Point> encrypt(Point message, Point generator, Point pubKey, gmp_randclass &rand)
{
    mpz_class k = rand.get_z_range(mpz_class(modulo));
    Point Q = scalarMultiplication(k, generator);
    Point kR = scalarMultiplication(k, pubKey);
    Point crypto = edwardsAddition(message, kR);
    return std::make_tuple(Q, crypto);
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
    mpz_class a = generatePrivateKey(r); // private key
    Point A = generatePublicKey(a, P);   // public key

    // 3. Generate the message
    Point pointMessage = generateMessage(P, r);

    std::cout << "MESSAGE" << std::endl;
    printPoint(pointMessage);
    std::cout << std::endl;

    // 4. Perform encryption
    auto [Q, crypto] = encrypt(pointMessage, P, A, r);
    std::cout << "CRYPTO" << std::endl;
    printPoint(crypto);
    std::cout << std::endl;

    // 4. Perform decryption
    Point decMessage = decrypt(Q, crypto, a);
    std::cout << "DECRYPT" << std::endl;
    printPoint(decMessage);

    performAssertion(pointMessage, decMessage);
}