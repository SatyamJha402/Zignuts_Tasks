class Shape{
    constructor(radius){
        this.radius = radius
    }
    area(){}
}

//inheriting the circle from shape
class Circle extends Shape{
    constructor(radius){
        super(radius);
    }
    area(){
        console.log(`area of this circle is ${3.14 * this.radius * this.radius}`);
        
    }
}

//inheriting triangle from shape
class Triangle extends Shape{
    constructor(height, radius){
        super(radius);
        this.height = height;
    }
    area(){
        console.log(`area of this triangle is ${0.5 * this.radius * this.height}`);
    }
}


const cir = new Circle(7)
cir.area();

const tri = new Triangle(5, 4)
tri.area();