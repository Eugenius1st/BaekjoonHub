function solution(N, stages) {
  var answer = [];
  let divNum = stages.length;
  let fail = {};
  let sortedFail = [];
  for (let x of stages) {
    if (!fail[x]) fail[x] = 1;
    else fail[x]++;
  }
  for (let y = 1; y <= N; y++) {
    if (!fail[y]) fail[y] = 0;
    sortedFail.push([y, fail[y] / divNum]);
    divNum -= fail[y]; // 이부분 문제
  }

  sortedFail.sort((a, b) => b[1] - a[1]); // 값으로 정렬
  for (let z of sortedFail) {
    answer.push(z[0]);
  }
  return answer;
}