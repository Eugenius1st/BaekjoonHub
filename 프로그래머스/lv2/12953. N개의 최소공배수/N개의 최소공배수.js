function solution(arr) {
  var answer = 0;
  let a = arr.pop();
  let b;
  let tmp; // 최소공배수
  while (arr.length > 0) {
    b = arr.pop();
    console.log("a:", a, "b:", b);
    tmp = gcdlcm(a, b);
    console.log(tmp);
    a = tmp;
  }
  return a;
}

function gcdlcm(a, b) {
  //최소공배수
  var gcd = calc_gcd(a, b);
  var lcm = (a * b) / gcd;
  return lcm;
}

function calc_gcd(a, b) {
  if (b == 0) return a;
  return a > b ? calc_gcd(b, a % b) : calc_gcd(a, b % a);
}