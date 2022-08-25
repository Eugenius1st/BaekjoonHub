function solution(numbers) {
    var answer = 0;
    const arr = Array.from({length:10},()=>1);
    for(let x of numbers){
        arr[x] = 0;
    }
    for(let y = 0 ; y <10;y++){
        if(arr[y]===1) answer += y
    }
    return answer;
}