#!/usr/bin/node
function Rectangle(w, h) {
  if(w == 0 || h == 0 || w < 0 || h < 0 || w == undefined || h == undefined){
    return;
  }
  else {
    this.width = w;
    this.height = h;
  }
  this.print = function() {
    for (let i=0; i<h; i++){
      let output=""
       for (let j=0; j<w; j++){
         output += "X"
        }
        console.log(output);
    }
  }
}

module.exports.Rectangle = Rectangle;
