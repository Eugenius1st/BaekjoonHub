function solution(n, arr1, arr2) {
  var answer = [];
  let tmp1, tmp2;
  for (let x = 0; x < n; x++) {
    let transN = "";
    tmp1 = arr1[x].toString(2);
    tmp1 = tmp1.padStart(n, "0"); // 자바스크립트 최신 메서드, 앞에서부터 채움
    tmp2 = arr2[x].toString(2);
    tmp2 = tmp2.padStart(n, "0"); // 자바스크립트 최신 메서드, 앞에서부터 채움
    for (let y = 0; y < n; y++) {
      if (tmp1[y] === "1" || tmp2[y] === "1") transN += "#";
      else transN += " ";
    }

    answer.push(transN);
  }
  return answer;
}