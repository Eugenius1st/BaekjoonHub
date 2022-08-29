function solution(numbers){
  arr = []
  answer = []
	for(let x = 0 ;x < numbers.length-1; x++){
  	for(let y = x+1 ; y < numbers.length;y++){
    	arr.push(numbers[x]+numbers[y]);
  	}
  }
  arr = new Set(arr);
  arr = [...arr]
  
  answer = arr.sort((a,b)=>a-b)
  return answer
}