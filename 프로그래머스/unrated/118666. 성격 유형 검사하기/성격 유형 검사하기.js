function solution(survey, choices) {
	var answer = ''; 
  const choice = {R:0, T:0, F:0, C:0, M:0, J:0, A:0, N:0}
	for(let x = 0 ; x < survey.length; x++){
    if(x>4)choice[survey[x][1]] += (choices[x]-4);
    else choice[survey[x][0]] += (4-choices[x]);

  }
  answer+= choice.R>=choice.T?"R":"T"
  answer+= choice.C>=choice.F?"C":"F"
  answer+= choice.J>=choice.M?"J":"M"
  answer+= choice.A>=choice.N?"A":"N" 
    return answer;
}