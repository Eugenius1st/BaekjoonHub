function solution(video_len, pos, op_start, op_end, commands) {
  const videoLenInt = timeInt(video_len);
  let posInt = timeInt(pos);
  const op_startInt = timeInt(op_start);
  const op_endInt = timeInt(op_end);
  for (let command of commands) {
    if (op_startInt <= posInt && posInt <= op_endInt) {
      posInt = op_endInt;
      console.log("jump", op_startInt, posInt, op_endInt);
    }
    console.log(op_startInt, posInt, "zz", posInt, op_endInt);
    if (command === "next") {
      console.log("next");
      if (posInt + 10 >= videoLenInt) posInt = videoLenInt;
      else posInt = posInt + 10;
    } else if (command === "prev") {
      console.log("prev");
      if (posInt - 10 <= 0) posInt = 0;
      else posInt = posInt - 10;
    }
    if (op_startInt <= posInt && posInt <= op_endInt) {
      posInt = op_endInt;
      console.log("jump", op_startInt, posInt, op_endInt);
    }
    console.log(posInt);
  }

  var answer = intTime(posInt);
  console.log(answer);
  return answer;
}

function timeInt(time) {
  const mm = Number(time.slice(0, 2));
  const ss = Number(time.slice(3, 5));
  return mm * 60 + ss;
}

function intTime(number) {
  const mm = String(Math.floor(number / 60)).padStart(2, "0");
  const ss = String(number % 60).padStart(2, "0");
  return mm + ":" + ss;
}
