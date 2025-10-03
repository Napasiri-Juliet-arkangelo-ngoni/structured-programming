function calculateGrade(mark) {
    // Using conditions to assign grades
    if (mark >= 80) {
        return "A";
    } else if (mark >= 70) {
        return "B";
    } else if (mark >= 60) {
        return "C";
    } else if (mark >= 50) {
        return "D";
    } else {
        return "F";
    }
}

// Array of student marks (real-world example: class exam results)
let studentMarks = [85, 72, 90, 60, 45, 78];

// Loop through all students and assign grades
for (let i = 0; i < studentMarks.length; i++) {
    let grade = calculateGrade(studentMarks[i]);
    console.log("Student " + (i+1) + " scored " + studentMarks[i] + " and got grade " + grade);
}

/*
Why use conditions; To decide grade category based on score.
Why use a loop; To process multiple students’ marks automatically.
Why use a function; To avoid repeating grade logic many times and make code reusable.
*/