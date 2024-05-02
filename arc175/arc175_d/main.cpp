#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

const std::string YES = "Yes";
const std::string NO = "No";
auto solve(int N, int64_t K, const std::vector<int64_t> &u, const std::vector<int64_t> &v) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N;
    int64_t K;
    std::cin >> N;
    std::vector<int64_t> u(N - 1), v(N - 1);
    std::cin >> K;
    REP (i, N - 1) {
        std::cin >> u[i] >> v[i];
    }
    auto ans = solve(N, K, u, v);
    std::cout << Yes << '\n';
    REP (i, N) {
        std::cout << P[i] << ' ';
    }
    std::cout << '\n';
    return 0;
}
