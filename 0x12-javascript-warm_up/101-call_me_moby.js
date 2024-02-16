#!/usr/bin/node

exports.callMeMoby = function (num, theFunction) {
  for (let idx = 0; idx < num; idx++) {
    theFunction();
  }
};
