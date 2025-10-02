// const student = {
//     Fullname:"Napasiri Juliet",
//     Yob: 2005,
//     Accessno: "M25B13/053",
//     Gender: "Female",
//     Phone: "0787938158",
// };
// console.log("student.Accessno.");

class students {
    constructor(Fullname, Accessno, Regno, Yob, Gender, Phone, Isregistered) {
        this.Fullname = Fullname;
        this.Accessno = Accessno;
        this.Regno = Regno;
        this.Yob = Yob;
        this.Gender = Gender;
        this.Phone = Phone;
        this.Isregistered = Isregistered;
    }

    studentAge() {
        // AGE = CURRENT YEAR - STUDENT YEAR OF BIRTH
        const currentyear = new Date().getFullYear();
        const age = currentyear - this.Yob;
        console.log(`The student is ${age} years old`);
    }
}

const student1 = new students(
    "Napasiri Juliet",
    "B33496",
    "M25B13/053",
    2005,
    "Female",
    "0787938158",
    true
);

const student2 = new students(
    "Emmanulla Dwatuka",
    "B33475",
    "M25B13/052",
    2000,
    "Female",
    "0789738158",
    true
);

console.log(student1);
console.log(student2);
student1.studentAge();
student2.studentAge();
