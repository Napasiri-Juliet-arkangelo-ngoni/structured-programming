//  While loops 
var x = 0; 
while (x <= 10) {
    if (x == 5 || x == 6) {
        x++;
        console.log(x);
        continue;
    }
    // x++
    x = x + 3;
}



// For loops
for (let mynumber = 0; mynumber <= 10; mynumber++) {

    if (mynumber % 2 == 0){
        console.log(mynumber);
    }
}