#include <stdlib.h>
#include <iostream>
#include <array>
#include <vector>
#include <sstream>
#include <string>
#include <fstream>


// BEGIN DEFINITIONS
#define D_VALUE 3
#define N_VALUE 256
#define T_VALUE 256

#define OUT_SIZE 1000000000
#define OUT_BIT 8
#define OUT_FILE "out_N_D0_T1233"

static const unsigned int key[] = {};

/*static const unsigned int key[] = { 248, 16, 215, 227, 15, 4, 14, 255, 7, 204, 10, 245, 181, 237, 13, 78, 197, 210,
 51, 241, 98, 24, 3, 115, 97, 238, 16, 81, 153, 166, 130, 151, 31, 195, 19, 108,
 169, 229, 12, 150, 191, 238, 240, 109, 178, 171, 230, 123, 248, 128, 231, 21,
 171, 166, 197, 22, 171, 60, 9, 7, 244, 7, 94, 14, 193, 35, 75, 201, 159, 190,
 216, 125, 192, 33, 199, 48, 94, 73, 59, 202, 88, 47, 96, 6, 206, 31, 227, 99,
 96, 12, 218, 204, 95, 94, 127, 144, 33, 217, 137, 85, 138, 211, 136, 197, 152,
 70, 79, 23, 31, 152, 60, 141, 46, 207, 158, 65, 18, 59, 145, 209, 209, 46, 36,
 127, 162, 205, 123, 81 };
*/
// END DEFINITIONS

static unsigned int KEY_LEN = sizeof(key) / sizeof(int);

static std::vector<int> S;
static unsigned int PRGA_I = 0;
static unsigned int PRGA_J = 0;

void KSA(const int N, const int T) {
  // Initialize S with 0...n
  S.clear();
  for (unsigned int i = 0; i <= N; i++) {
    S.push_back(i);
  }

  // Shuffle S
  unsigned int j = 0;
  for (unsigned int i = 0; i <= T; i++) { // Run loop T+1 times
    j = (j + S[i % N] + key[i % KEY_LEN]) % N;
    std::swap(S[i % N], S[j % N]);
  }
}

unsigned int PRGA() {
  // Run loops D_VALUE + 1 times.
  for (int i = 0; i < D_VALUE+1; i++) {
    PRGA_I = (PRGA_I + 1) % N_VALUE;
    PRGA_J = (PRGA_J + S[PRGA_I]) % N_VALUE;
    std::swap(S[PRGA_J], S[PRGA_I]);
  }
  return S[(S[PRGA_J] + S[PRGA_I]) % N_VALUE];
}


int main(int argc, char* argv[]) {

  // std::cout << atoi(argv[1]);

  KSA(N_VALUE, N_VALUE);

  std::ostringstream sstr;
  std::ofstream myfile;
  myfile.open (OUT_FILE, std::ios::binary);

  long long i = 0;

  for (unsigned long long iii = 1; i < OUT_SIZE/100000; iii++) {
    myfile << (char) PRGA();
    if (!(iii % 10000)) {
      myfile.flush();
      i++;
  }
  myfile.close();
  return 0;
}
