function solution(board, moves) {
  var answer = 0;
  let res = [];
  for (let x of moves) {
    for (let i = 0; i < board.length; i++) {
      if (board[i][x - 1] !== 0) {
        res.push(board[i][x - 1]);
        board[i][x - 1] = 0;
        while(res.length >= 2 && res[res.length - 1] === res[res.length - 2]) {
          res.pop();
          res.pop();
          answer += 2;
      }
        break;//break가 중요!!
      } else continue;
    }
  }
  return answer;
}
