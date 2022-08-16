function solution(new_id) {
  var answer = "";

  //1
  new_id = new_id.toLowerCase();
  //2
  for (let x of new_id) {
    if (x === "-" || x === "_" || x === ".") answer += x;
    else if (!isNaN(x)) {
      answer += x;
    } else if (
      (x.charCodeAt() >= 65 && x.charCodeAt() <= 90) ||
      (x.charCodeAt() >= 97 && x.charCodeAt() <= 122)
    )
      answer += x;
  }
  //3 ..을 계속 . 으로
  while (answer.includes("..")) {
    answer = answer.replace("..", ".");
  }
  //4 마침표가 처음이나 끝에 있을 경우 제거!!! 이부분 공부
  answer = answer.replace(/^\.|\.$/g, "");
  //5
  if (answer === "") answer = "a";
  //6
  if (answer.length >= 16) {
    answer = answer.substring(0, 15);
  }
  answer = answer.replace(/^\.|\.$/g, "");
  //7
  while (answer.length <= 2) {
    answer += answer[answer.length - 1];
  }

  return answer;
}

let output = solution("...!@BaT#*..y.abcdefghijklm");
console.log(output); // --> 1

output = solution("z-+.^.");
console.log(output); // --> 2

output = solution("123_.def");
console.log(output); // --> 2
