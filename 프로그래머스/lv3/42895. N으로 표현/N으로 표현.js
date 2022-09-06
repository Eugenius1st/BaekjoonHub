function solution(N, number) {
  if (N == number) return 1; //애초에 같을 경우 1 리턴

  // 전체 집합 공간 할당
  const dp = [...Array(9)].map(() => new Set());
  let ans = -1; // 순회 다 돌아도 값이 없을 경우 -1 리턴
  let stringN = String(N);

  dp[1].add(N);

  for (let i = 2; i <= 8; i++) {
    // i에 대한 집합 만들기
    stringN += N; // 55,555,5555... 넣어두기
    dp[i].add(Number(stringN));

    for (let j = 1; j < i; j++) {
      for (const num1 of dp[i - j]) {
        for (const num2 of dp[j]) {
          dp[i].add(num1 + num2); //dp 배열의 2 ~ 8 을 채운다 (집합 구성요소) 사칙연산 (집합 구성요소)
          dp[i].add(num1 - num2);
          dp[i].add(num1 * num2);
          dp[i].add(num1 / num2);
        }
      }
    }
    // i집합에 number가 포함되어 있다면 i가 정답
    if (dp[i].has(number)) {
      ans = i;
      break;
    }
  }
  return ans;
}