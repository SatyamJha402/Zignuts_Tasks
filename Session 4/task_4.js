class University {
    constructor(name) {
        this.name = name;
        this.departments = [];
    }

    // adding a department
    addDepartment(deptName) {
        if (!this.departments.includes(deptName)) {
            this.departments.push(deptName);
            console.log(`Department "${deptName}" added.`);
        } else {
            console.log(`Department "${deptName}" already exists.`);
        }
    }

    // removing a department
    removeDepartment(deptName) {
        const index = this.departments.indexOf(deptName);
        if (index !== -1) {
            this.departments.splice(index, 1);
            console.log(`Department "${deptName}" removed.`);
        } else {
            console.log(`Department "${deptName}" not found.`);
        }
    }

    // for displaying the departments
    displayDepartments() {
        console.log(`Departments in ${this.name}:`);
        if (this.departments.length === 0) {
            console.log("No departments yet.");
        } else {
            this.departments.forEach((dept, i) => {
                console.log(`${i + 1}. ${dept}`);
            });
        }
    }
}

const uni = new University("Tech University");

uni.addDepartment("Computer Science");
uni.addDepartment("Mathematics");
uni.addDepartment("Physics");
uni.displayDepartments();

uni.removeDepartment("Mathematics");
uni.displayDepartments();
