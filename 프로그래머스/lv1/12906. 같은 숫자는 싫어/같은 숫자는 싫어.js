function solution(arr)
{
    var answer = [arr[0]];
    for(let x=1;x<arr.length;x++){
        if(answer[answer.length-1]!==arr[x]) answer.push(arr[x]) ; 
    }
    return answer;
}