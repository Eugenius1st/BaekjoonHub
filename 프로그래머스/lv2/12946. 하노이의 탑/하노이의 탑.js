function solution(n) {
	var answer = [];
 // 2^4-1 ==> 15
const hanoi = (num, from, to, other) => {
  if (num === 0) return
  hanoi (num - 1, from, other, to);
	answer.push([from+1,other+1]);
  hanoi (num - 1, to, from,other);  
}
	hanoi(n, 0, 1, 2)
  return answer
}