function solution(lottos, win_nums) {
  // 알아볼 수 없는 번호를 0
  const rank = [6, 6, 5, 4, 3, 2, 1];
  var answer = []; //최고와 최저
  let zero = 0;
  let score = 0;

  for (let x = 0; x < lottos.length; x++) {
    if (lottos[x] === 0) zero++;
    else if (win_nums.includes(lottos[x])) {
      console.log(lottos[x]);
      score++;
    }
  }
  console.log("score:", score, "zero", zero);

  answer.push(rank[score + zero]);
  answer.push(rank[score]);

  return answer;
}

let output = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]);
console.log(output); // --> 1
