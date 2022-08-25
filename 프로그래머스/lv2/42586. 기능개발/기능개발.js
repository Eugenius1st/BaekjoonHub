function solution(progresses, speeds) {
  var answer = [];
  let multi = 0;
  let pop = 0;

  while (progresses.length > 0) {
    if (progresses[0] + speeds[0] * multi >= 100) {
      progresses.shift();
      speeds.shift();
      pop++;
    } else {
      if (pop > 0) {
        answer.push(pop);
        pop = 0;
      }
      multi++;
    }
  }
  answer.push(pop);
  return answer;
}