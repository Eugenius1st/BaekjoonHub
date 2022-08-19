function solution(s){
  let check = 0; 
    for(let x of s){
      if(x==="(") check ++
      else if(x===")") check --//여기서 삼항연산자 (x==="(")? check ++:check-- 쓰면 시간초과 
      if(check < 0)return false
    }
    if(check === 0)return true;
  	else return false
}