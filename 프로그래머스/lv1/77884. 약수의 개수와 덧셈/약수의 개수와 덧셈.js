function solution(left, right) {
  var answer = 0;
  let numCnt = 0;
  for (let i = left; i <= right; i++) {
    for (let x = 1; x <= i; x++) {
      if (i % x === 0) numCnt++;
    }
    numCnt % 2 === 0 ? (answer += i) : (answer -= i);
    numCnt = 0;
  }
  return answer;
}