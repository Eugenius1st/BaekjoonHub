function solution(clothes) {
  var answer = 1;
  const clothesMap = new Map();
  for (const [clothName, clothCategory] of clothes) {
    clothesMap.set(clothCategory, (clothesMap.get(clothCategory) || 0) + 1); // 누적으로 더함. 최종적으로 +1 을 한 것은, 아무것도 입지 않는 경우도 고려해야 하기 때문
  }
  for (let clo of clothesMap) {
    answer *= clo[1] + 1;
  }
  return answer - 1;
}