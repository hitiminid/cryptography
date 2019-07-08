#include <iostream>
#include <array>
#include <vector>
#include <sstream>
#include <string>
#include <fstream>

// BEGIN DEFINITIONS
long D_VALUE;
long N_VALUE;
long T_VALUE;
long OUT_BIT;
std::string OUT_FILE;
static const unsigned int key[] = {155, 240, 121, 136, 50, 170, 165, 101, 215, 193,
                                    0, 182, 75, 193, 23, 159, 34, 12, 177, 172, 218,
                                    211, 243, 197, 165, 11, 219, 14, 197, 27, 86, 120,
                                    67, 65, 224, 24, 16, 109, 140, 15, 93, 10, 246, 15, 186,
                                    29, 232, 217, 19, 116, 193, 53, 112, 60, 18, 82, 229, 75,
                                    43, 113, 71, 6, 219, 129, 16, 69, 243, 66, 108, 55, 137,
                                    91, 143, 248, 166, 5, 244, 222, 29, 204, 196, 226, 150, 6,
                                    164, 159, 203, 30, 159, 30, 9, 56, 251, 230, 223, 74, 38, 38,
                                    218, 189, 219, 244, 149, 39, 98, 111, 108, 33, 64, 253, 97, 5,
                                    225, 65, 129, 49, 14, 38, 128, 20, 180, 227, 170, 123, 140, 138,
                                     45, 218};
// END DEFINITIONS

unsigned int KEY_LEN;

static std::vector<int> S;
static unsigned int PRGA_I = 0;
static unsigned int PRGA_J = 0;

void KSA(const int N, const int T)
{
  // Initialize S with 0...n-1
  S.clear();
  for (unsigned int i = 0; i < N; i++)
  {
    S.push_back(i);
  }

  // Shuffle S
  unsigned int j = 0;
  for (unsigned int i = 0; i <= T; i++)
  { // Run loop T+1 times
    j = (j + S[i % N] + key[i % KEY_LEN]) % N;
    std::swap(S[i % N], S[j % N]);
  }
}

unsigned int PRGA()
{
  // Run loops D_VALUE + 1 times.
  for (int i = 0; i < D_VALUE + 1; i++)
  {
    PRGA_I = (PRGA_I + 1) % N_VALUE;
    PRGA_J = (PRGA_J + S[PRGA_I]) % N_VALUE;
    std::swap(S[PRGA_J], S[PRGA_I]);
  }
  return S[(S[PRGA_J] + S[PRGA_I]) % N_VALUE];
}

std::ofstream myfile;

int xw = 0;
int xn = 0;
long long awrite_bits(char res)
{
  xw = xw << OUT_BIT;
  xw += res;
  xn += OUT_BIT;
  if (xn == 8)
  {
    myfile << (char)xw;
    xw = 0;
    xn = 0;
    return 1;
  }
  return 0;
}

int main(int argc, char *argv[])
{

  if (argc != 5)
  {
    // std::cout << argv[1] << std::endl;
    std::cout << "Not enough parameters" << std::endl;
    return 0;
  }

  std::ostringstream sstr;

  N_VALUE = std::stol(argv[1]);
  T_VALUE = std::stol(argv[2]);
  D_VALUE = std::stol(argv[3]);
  KEY_LEN = std::stoi(argv[4]);

  if (N_VALUE == 256)
  {
    OUT_BIT = 8;
  }
  else
  {
    OUT_BIT = 4;
  }

  sstr << "test_N" << N_VALUE << "_T" << T_VALUE << "_D" << D_VALUE << "_K" << KEY_LEN;

  OUT_FILE = sstr.str();

  std::cout << OUT_FILE << std::endl;

  KSA(N_VALUE, T_VALUE);

  myfile.open(OUT_FILE, std::ios::binary);
  // 100000
  // 100000
  for (long i = 0; i < 100000; i++)
  {
    for (long j = 0; j < 10000;)
    {
      j += awrite_bits(PRGA());
    }
    myfile.flush();
  }


  myfile.close();
  return 0;
}