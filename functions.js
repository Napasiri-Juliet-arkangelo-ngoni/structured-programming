function AddMarks (courseworkmarks, exammarks, percentageofattendance){
    return (courseworkmarks + exammarks) * percentageofattendance;
}

let results = AddMarks(30, 20, 0.7)

console.log(AddMarks (40,50));

if (finalmark < 50) {
    console.log("You have a retake");
} else {
    console.log("You have successfully passed");
}

// Range (0 - 49 F) (50 - 59 C) (60 - 69 B) (70 AND ABOVE A)
if (finalmark <= 49) {
    console.log("GRADE F");
     if (finalmark == 0) {
        console.log("You should repeat")
    }
} else if ( 50 <= finalmark <= 59) {

} else if ( 60 <= finalmark <= 69) {
    console.log("GRADE B")
} else {
    console.log("GRADE A")
}