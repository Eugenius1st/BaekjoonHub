function solution(numbers, hand) {
  var answer = "";
  // 키패드 위치 객체로 초기화
  const keyPad = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    "*": [3, 0],
    0: [3, 1],
    "#": [3, 2],
  };
  // 첫 엄지's 위치 초기화
  let left = "*";
  let right = "#";
  let distanceL = 0;
  let distanceR = 0;
  //for문 돌려!
  for (let x of numbers) {
    // 1,4,7 경우 무조건 왼손
    if (x === 1 || x === 4 || x === 7) {
      left = x;
      answer += "L";
    }
    // 3,6,9 경우 무조건 오른손
    else if (x === 3 || x === 6 || x === 9) {
      right = x;
      answer += "R";
    }
    // 그 외의 경우 2,5,8,0은 거리 계산
    else {
      distanceR =
        Math.abs(keyPad[x][0] - keyPad[right][0]) +
        Math.abs(keyPad[x][1] - keyPad[right][1]);
      distanceL =
        Math.abs(keyPad[x][0] - keyPad[left][0]) +
        Math.abs(keyPad[x][1] - keyPad[left][1]);
      // 만약 거리가 같은 경우 왼잡 VS 오른잡 확인
      if (distanceL === distanceR) {
        if (hand === "right") {
          answer += "R";
          right = x;
        } else {
          answer += "L";
          left = x;
        }
      } else {
        if (distanceL > distanceR) {
          answer += "R";
          right= x;
        } else {
          answer += "L";
          left= x;
        }
      }
    }
  }
  return answer;
}