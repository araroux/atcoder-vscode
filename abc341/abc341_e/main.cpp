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
auto solve(auto N, auto Q, auto S, const std::vector<auto> &query) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    auto N, Q, S;
    std::cin >> N >> Q;
    std::vector<auto> query(Q);
    std::cin >> S;
    REP (i, Q) {
        std::cin >> query[i];
    }
    auto ans = solve(N, Q, S, query);
    // failed to analyze output format
    // TODO: edit here
    std::cout << ans << '\n';
    return 0;
}
