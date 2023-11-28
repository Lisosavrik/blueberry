// module aliases
var Engine = Matter.Engine,
    Render = Matter.Render,
    Runner = Matter.Runner,
    Bodies = Matter.Bodies,
    Composite = Matter.Composite;
    Body = Matter.Body;
    Query = Matter.Query;
    Vector = Matter.Vector;



let Blueberries = ["../static/img/blueberry_1.png", 
"../static/img/blueberry_2.png", 
"../static/img/raspberry.png",
"../static/img/blue_raspberry.png"];

let mapping = {
    0: 70, 
    1: 10, 
    2 : 10, 
    3: 10
}


let AllBerries = [];
let Start = Vector.create(0, 0);
let End = Vector.create(1412, 0);
// let Test = Vector.create(100, 100);
let i = 0;

var engine = Engine.create();

var render = Render.create({
    element: document.getElementById('animation'),
    engine: engine,
    options: {
        height: window.innerHeight,
        width: window.innerWidth,
        background: "#f5f5f5",
        pixelRatio: 1,
    }

});

Render.run(render);
render.options.wireframes = false;

function getRandomFromMapping(mapping) {
    let sum = 0;

    const entries = Object.entries(mapping);
    const max = entries.reduce((sum, [_, val]) => sum + val, 0);

    const randomNumber = Math.random() * max;

    const rightEl = entries.find(([_, value])=> {
        let newSum = sum + value;
        if ((randomNumber > sum) && (randomNumber < newSum)) return true;
        sum = newSum;
    })
    return rightEl[0];
}


function isTheTop(berry){
    AllBerries.push(berry);
    let TopList = Query.ray(AllBerries, Start, End)
    if (TopList.length >= 16){
        Composite.remove(engine.world, [ground])
        AllBerries.splice(0, AllBerries.length)
        setTimeout(() =>{
            let allBodies = Composite.allBodies(engine.world)
            console.log(allBodies)
            Composite.remove(engine.world, allBodies)
            Composite.add(engine.world, [ground, leftWall, rightWall])
        }, 4000);
    };
};

function  randArray(arr) {
    return arr[randInt(0, arr.length - 1)];
}


function repeat() {
    let l = randInt(0, 1360)
    const width = window.innerWidth
    const imageWidth = 300
    const berrySize = 30
    scale = 
    setTimeout(() => {
        var boxA = Bodies.circle(l, -50, 44, {
            isStatic: false,
            render: {
                sprite: {
                    texture: Blueberries[getRandomFromMapping(mapping)],
                    xScale: 0.309,
                    yScale: 0.309,
                }
            }
        });

        boxA.friction = 0.2
        boxA.frictionStatic = 0.2;
        Body.setMass(boxA, 1);
        Body.rotate(boxA, (randInt(0, 1) - 0.5) * 0.1, undefined, [updateVelocity=true]);


        Composite.add(engine.world, [boxA]);

        if (i > 40) {
            isTheTop(boxA)
        }
        repeat();
        i++;
    },  randInt(1, 5) * 500)
};


var ground = Bodies.rectangle(0, window.innerHeight+15, window.innerWidth*2, 50, {
    isStatic: true,
    render: { fillStyle: '#f5f5f5'}
});

var leftWall = Bodies.rectangle(0, 0, 10, window.innerHeight*2, {
    isStatic: true,
    render: { fillStyle: '#f5f5f5'},
});

var rightWall =  Bodies.rectangle(window.innerWidth, 0, 10, window.innerHeight*2, {
    isStatic: true,
    render: { fillStyle: '#f5f5f5'}
});


Composite.add(engine.world, [ground, leftWall, rightWall]);
Composite.remove

var runner = Runner.create();

// run the engine
Runner.run(runner, engine);

repeat()





