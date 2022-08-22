
function solution(n, lost, reserve) {
  var answer = 0;
  const lostArr = Array.from({ length: n }, () => 1); //1 있다
  const reserveArr = Array.from({ length: n }, () => 0); // 0 없다
  // 체육복이 없는 바보들 체크
  for (let x of lost) lostArr[x - 1] = 0;
  // 여벌 있는 사람들 체크
  for (let x of reserve) reserveArr[x - 1] = 1;

  // for문 돌려서 체육복에 따른 수업 참여 여부 알아보자
  for (let x = 0; x < n; x++) {

    if (lostArr[x] === 0 && reserveArr[x] === 1) {
      lostArr[x] = 1;
      reserveArr[x] = 0;
    } 
  }
for (let x = 0; x < n; x++) {
console.log("x:",x,lostArr,reserveArr)
 if (lostArr[x] === 0) {
      if (reserveArr[x - 1] === 1) {
        lostArr[x] = 1;
        reserveArr[x - 1] = 0;
      } else if (reserveArr[x+1] === 1) {
        lostArr[x] = 1;
        reserveArr[x + 1] = 0;
      }
    }
}
answer = lostArr.reduce((acc, cur) => acc + cur);
  
  // 만약 여벌을 내가 갖고 있다면, 체육복 있다고 체크
  // 만약 체격 하나 작은 여벌이 있다면. 체육복 있다고 체크
  return answer;
}

// n은 전체 학생 수, lost도난당한 학생들 배열, reverse여벌 체육복 가져온 학생들 배열

console.log(solution(5, [1,2, 3,4, 5], [5]));
