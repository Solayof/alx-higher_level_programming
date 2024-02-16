#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let idx = 0;

  for (let i = list.length - 1; i >= 0; i--) {
    revList[idx] = list[i];
    idx++;
  }

  return revList;
};
