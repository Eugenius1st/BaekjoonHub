function solution(n, k) {
  var answer = 0;
  let tmpArr;
  let tmpStr;
  let flag = true;
  // k진수로 바꾸기
  tmpStr = n.toString(k);
  // split 으로 떼어내기
  tmpArr = tmpStr.split("0");
  // 소수인지 확인하기
  for (let x of tmpArr) {
    flag = true;
    if (isNaN(x) || x === "") continue;
    x = Number(x);
    if (x === 2) answer++;
    if (x >= 2) {
      for (let i = 2; i < Math.sqrt(x) + 1; i++) {
        if (x % i === 0) {
          console.log("xx", x);
          flag = false;
          break;
        }
      }
      if (flag) {
        answer += 1;
        console.log("x", x, "ans", answer);
      }
    }
  }
  return answer;
}

console.log(solution(437674, 3));
