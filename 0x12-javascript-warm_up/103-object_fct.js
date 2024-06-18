#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function() {
    this.value++;  // Increment the value property of myObject
  }
};

console.log(myObject);

// Increment myObject value
myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
