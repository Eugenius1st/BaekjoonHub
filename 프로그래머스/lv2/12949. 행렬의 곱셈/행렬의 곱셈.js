function solution(arr1, arr2) {
    // var answer = Array.from({length:arr1.length},()=>Array.from({length:arr2[0].length},()=>0));
	// push 안쓰고 한번에 배열 크기 만들어서 넣는것은 왜 시간초과 날까..?
  let row, col, tmp, res;
  const answer = [];
  	for(let x = 0; x < arr1.length; x++){
      tmp=[];
      for(let y = 0; y < arr2[0].length;y++){
        res = 0
        for(let z = 0 ; z< arr2.length;z++){
        row = arr1[x][z]; 
        col = arr2[z][y];
        // console.log(row,col)
        res +=row*col;
        }
        tmp.push(res);
      }
      answer.push(tmp);
    }
    return answer;
}