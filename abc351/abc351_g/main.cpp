#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

constexpr int64_t MOD = 998244353;
auto solve(auto a, auto b, const std::vector<auto> &c, const std::vector<auto> &d, const std::vector<auto> &e, const std::vector<auto> &f) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    auto a, b;
    std::cin >> a;
    std::vector<auto> c(a), d(a);
    std::cin >> b;
    std::vector<auto> e(b), f(b);
    REP (i, a) {
        std::cin >> c[i];
    }
    REP (i, a) {
        std::cin >> d[i];
    }
    REP (i, b) {
        std::cin >> e[i] >> f[i];
    }
    auto ans = solve(a, b, c, d, e, f);
    // failed to analyze output format
    // TODO: edit here
    std::cout << ans << '\n';
    return 0;
}
