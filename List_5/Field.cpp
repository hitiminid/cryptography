#include "gmpxx.h"

// mpz_t - typ z c sluzacy do przechowywania duzych liczb

template <mpz_t mod>
class Field
{
  private:
    mpz_class value;

  public:
    Field(mpz_t value)
    {
        mpz_mod(this->value.get_mpz_t(), value, mod);
    }

    Field(mpz_class value)
    {
        // what, where, mod
        mpz_mod(this->value.get_mpz_t(), value.get_mpz_t(), mod);
    }

    Field(int value)
    {
        mpz_t tmp;
        mpz_init_set_si(tmp, value); // set signed integer
        mpz_mod(this->value.get_mpz_t(), tmp, mod);
    }

    void getValue(mpz_t ret)
    {
        mpz_init_set(ret, this->value.get_mpz_t());
    }

    mpz_class getValue()
    {
        return this->value;
    }

    Field operator+(Field const &obj)
    {
        return Field(value + obj.value);
    }

    Field operator-(Field const &obj)
    {
        return Field(value - obj.value);
    }

    Field operator-()
    {
        return Field(-value);
    }

    Field operator*(Field const &obj)
    {
        return Field(value * obj.value);
    }

    Field operator/(Field const &obj)
    {
        mpz_t tmp;
        mpz_init(tmp);
        mpz_invert(tmp, obj.value.get_mpz_t(), mod);
        mpz_mul(tmp, value.get_mpz_t(), tmp);
        return Field(tmp);
    }

    Field operator%(Field const &obj)
    {
        return Field(value % obj.value);
    }

    bool operator==(Field const &field)
    {
        return mpz_cmp(value.get_mpz_t(), field.value.get_mpz_t()) == 0;
    }

    bool operator!=(Field const &field)
    {
        return mpz_cmp(value.get_mpz_t(), field.value.get_mpz_t()) != 0;
    }
};