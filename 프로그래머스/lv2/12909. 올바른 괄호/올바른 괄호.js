function solution(s){
  let check = 0; 
    for(let x of s){
      if(x==="(") check ++
      else if(x===")") check -- 
      if(check < 0)return false
    }
    if(check === 0)return true;
  	else return false
}
// 스택,큐 로 다시 풀어볼까..