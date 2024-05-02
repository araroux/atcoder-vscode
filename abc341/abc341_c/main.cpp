#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


int64_t solve(int H, int64_t W, int64_t N, std::string T, const std::vector<std::string> &S) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int H;
    int64_t W, N;
    std::string T;
    std::cin >> H;
    std::vector<std::string> S(H);
    std::cin >> W >> N >> T;
    REP (i, H) {
        std::cin >> S[i];
    }
    auto ans = solve(H, W, N, T, S);
    std::cout << ans << '\n';
    return 0;
}
