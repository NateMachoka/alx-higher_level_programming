#!/usr/bin/node

// Visible function from outside that executes another function x times
exports.callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; ++i) {
    theFunction();
  }
};
