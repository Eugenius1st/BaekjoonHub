function solution(a, b) {
  const day = ["THU","FRI","SAT","SUN","MON","TUE","WED"] // 나머지 인덱스
  // 1월 1일은 금요일
  let acc = 0;
  var answer = '';
  // 달이 8보다 작을 때
  // 달이 2로 나누어 떨어지면 30일
  // 달이 2로 나누어 떨어지지 않으면 31일
  // 달이 8보다 크거나 같을 때
  // 달이 2로 나누어 떨어지면 31일
  // 달이 2로 나누어 떨어지지 않으면 30 일
	// 2월의 경우에는 29일
  
  for(let x = 1; x < a; x++){
    if (x<8){
        if(x===2) acc += 29
      else if(x%2===0) acc += 30
      else acc += 31
    }
    else{
      if(x%2===0) acc += 31
      else acc += 30
    }
  }
  answer = day[(acc+b)%7];
  return answer;
}