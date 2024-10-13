function solution(phone_book) {
  const phoneMap = new Map();
  // 해시 맵에 저장
  for (const phone of phone_book) {
    phoneMap.set(phone, true);
  }
  // 해시맵에 존재하는지 확인
  for (const phone of phone_book) {
    let prefix = ""; // 접두사
    for (let i = 0; i < phone.length - 1; i++) {
      // 같은 번호가 중복해서 들어가지 않으니, 마지막까지 확인할 필요 없음
      prefix += phone[i];
      if (phoneMap.has(prefix)) return false;
    }
  }
  return true;
}