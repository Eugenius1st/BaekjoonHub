function isPrime(x) {// 소수인지 판별하는 함수
  for (let i = 2; i <= Math.sqrt(x); i++) {
    if (x % i === 0) return false;
  }
  return true;
}
function solution(n) {
  let answer = 0;
  for (let i = 2; i <= n; i++) {
    // 소수이면 소수의 개수에 1 추가
    if (isPrime(i)) answer++;
  }
  return answer;
}