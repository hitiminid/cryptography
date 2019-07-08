#include "Field.hpp"

typedef Field<modulo> Number;
typedef std::pair<Number, Number> Point;
// generator is P

// wywalić do utils.cpp
// 1) edwardsAddition
// 2) getSeed()

Point edwardsAddition(const Point firstPoint, const Point secondPoint)
{
}

Point scalarMultiplication(mpz_class scalar, Point P)
{
}

bool isOnCurve(Point point)
{
}

void printPoint(Point point)
{
}

void log()
{
}

void generateModulo()
{
}

unsigned long long int getSeed()
{
}

Point createBasePoint()
{
}

mpz_class generatePrivateKey(gmp_randclass &rand)
{
}

Point generatePublicKey(mpz_class a, Point P)
{
}

Point generateMessage(Point P, gmp_randclass &r)
{
}

std::tuple<Point, Point> encrypt(Point message, Point generator, Point pubKey, gmp_randclass &rand)
{
}

Point decrypt(Point Q, Point crypto, mpz_class privKey)
{
}

void performAssertion(Point message, Point decryptedMessage)
{
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