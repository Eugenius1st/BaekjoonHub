function solution(dartResult) {
  // 0에서 10 사이 정수
  //S, D, T(**1,**2,**3)
  // 옵션은 *(*2)이나 #(-)
  //주의 :  스타상(*) 당첨 시 해당 점수와 && 바로 전에 얻은 점수를 각 2배로
  // 주의2 : 0~10사이의 정수이다.
  var answer = 0;
  const val = [];
  for (let x = 0; x < dartResult.length; x++) {
    console.log(val);
    if (!isNaN(dartResult[x])) {
      if (dartResult[x] === "0" && dartResult[x - 1] === "1") {
        val[val.length - 1] = 10;
      } else val.push(dartResult[x]);
    } else if (dartResult[x] === "*") {
      if (val.length === 1) val[val.length - 1] = val[val.length - 1] * 2;
      else {
        val[val.length - 1] = val[val.length - 1] * 2;
        val[val.length - 2] = val[val.length - 2] * 2;
      }
    } else if (dartResult[x] === "#")
      val[val.length - 1] = val[val.length - 1] * -1;
    else if (dartResult[x] === "S")
      val[val.length - 1] = val[val.length - 1] ** 1;
    else if (dartResult[x] === "D")
      val[val.length - 1] = val[val.length - 1] ** 2;
    else if (dartResult[x] === "T")
      val[val.length - 1] = val[val.length - 1] ** 3;
  }
  answer = val.reduce((acc, cur) => acc + cur);
  return answer;
}