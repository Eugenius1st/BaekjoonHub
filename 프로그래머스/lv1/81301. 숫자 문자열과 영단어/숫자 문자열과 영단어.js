function solution(s) {
    var answer = "";
  	const numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let tmp = "";
    for(let x of s){
      if(!isNaN(x)){
        answer+=x;
      }
      else{
        tmp += x;
        if(numbers.includes(tmp)){
           answer += numbers.indexOf(tmp);
           tmp = "";
         }
    	}
    }
    return Number(answer);
}