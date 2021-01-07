function rad(d){
  return d*Math.PI/180;
}

function deg(r){
  return r*180/Math.PI;
}

function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}

function connect_nodes(start, end){
  // create the cylinder
  const distance = start.position.distanceTo(end.position)
  const cylinder = create_cylinder(10, 10, distance , 32, 0x2e342f);

  // Starting sphere position
  const sx = start.position.x
  const sy = start.position.y
  const sz = start.position.z

  // Ending sphere position
  const ex = end.position.x
  const ey = end.position.y
  const ez = end.position.z

  let quadrent = 1
  if (ex > sx && ey > sy){
    quadrent = -1
  }
  else if (ex < sx && ey < sy){
    quadrent = -1
  }

  // XY angle and position
  const xy_plane = [Math.abs(sx-ex), Math.abs(sy-ey)]
  const xy_angle = Math.atan(xy_plane[0]/xy_plane[1]) * quadrent
  console.log(deg(xy_angle))
  cylinder.rotation.z = xy_angle
  cylinder.position.x = (sx+ex)/2
  cylinder.position.y = (sy+ey)/2

  // XZ angle and position UNFINISHED
  const xz_plane = [Math.abs(sx-ex), Math.abs(sz-ez)]
  const xz_angle = rad(90) - Math.atan(xz_plane[0]/xz_plane[1])
  console.log(deg(xz_angle))
  cylinder.rotation.y = xz_angle
  cylinder.position.z = (sz+ez)/2

  return cylinder
}

function create_cylinder(top_radius, bot_radius, height, segments, color ){
  const geometry = new THREE.CylinderGeometry( top_radius, bot_radius, height, segments );
  const material = new THREE.MeshLambertMaterial( {color: color} );
  const cylinder = new THREE.Mesh( geometry, material );
  return cylinder
}

function create_sphere(radius, segments, rings, color){
  // create the sphere's material
  const sphereMaterial =
    new THREE.MeshLambertMaterial(
      {
        color: color
      });

  // Create a new mesh with
  // sphere geometry - we will cover
  // the sphereMaterial next!
  const sphere = new THREE.Mesh(

    new THREE.SphereGeometry(
      radius,
      segments,
      rings),

    sphereMaterial);
  return sphere
}


function create_camera(VIEW_ANGLE, ASPECT, NEAR, FAR){
    return new THREE.PerspectiveCamera(
        VIEW_ANGLE,
        ASPECT,
        NEAR,
        FAR
    );
}

function create_node(x, y, id){
    const sphere = create_sphere(50, 16, 16, 0x00a029 );
    sphere.position.z = -1000;
    sphere.position.x = x;
    sphere.position.y = y;
    node_list[id]=sphere
    scene.add(sphere)
}

function random_node(){
    x = getRndInteger(-1500,1500)
    y = getRndInteger(-700, 700)
    id = getRndInteger(-700, 700)
    create_node(x,y,id)
}

function create_edge(id1, id2){
    const node1 = node_list[id1]
    const node2 = node_list[id2]
    const edge = connect_nodes(node1, node2);
    scene.add(edge)
}

function create_lighting(x, y, z, color){
    const pointLight = new THREE.PointLight(color);

    // set its position
    pointLight.position.x = x;
    pointLight.position.y = y;
    pointLight.position.z = z;
    return pointLight
}

// Get data passed to html by django
const users = JSON.parse(document.getElementById('users').textContent);
console.log(users)

// Set the scene size.
// 75, window.innerWidth / window.innerHeight, 0.1, 1000
const WIDTH = window.innerWidth;
const HEIGHT = window.innerHeight;

// Set some camera attributes.
const VIEW_ANGLE = 75;
const ASPECT = WIDTH / HEIGHT;
const NEAR = 0.1;
const FAR = 10000;

// Create a WebGL renderer, camera
// and a scene
const renderer = new THREE.WebGLRenderer();
const camera = create_camera(VIEW_ANGLE, ASPECT, NEAR, FAR);

const scene = new THREE.Scene();

// Add the camera to the scene.
scene.add(camera);

// Start the renderer.
renderer.setSize(WIDTH, HEIGHT);

// Set background color
scene.background = new THREE.Color( 0xffffff );

// Attach the renderer-supplied
// DOM element
document.getElementById('container').appendChild(renderer.domElement)

// node_list will hold all the spheres as {id: username}
let node_list = {}

// create_node creates a sphere, positions it, then adds it to node_list
create_node(0, 200, 1);
create_node(300, 0, 2);
create_node(-300, 0, 3);
create_node(500, -200, 4);
create_node(100, -200, 5);
create_node(-100, -200, 6);
create_node(-500, -200, 7);

create_edge(1,2)
create_edge(1,3)
create_edge(2,4)
create_edge(2,5)
create_edge(3,6)
create_edge(3,7)


// create a point light
const pointLight = create_lighting(10, 50, 130, 0xFFFFFF)

// add to the scene
scene.add(pointLight);

// Draw!
renderer.render(scene, camera);
function start_zoom(){
    zoom = true;
}
let zoom = false;

function update () {
    // Draw!
    renderer.render(scene, camera);

    // Schedule the next frame.
    requestAnimationFrame(update);
    if (zoom){
        camera.position.z -= 10
        camera.lookAt(node_list[1].position)
    }

}

// Schedule the first frame.
requestAnimationFrame(update);

/*
const sphere = create_sphere(50, 16, 16, 0x00a029 );
const sphere2 = create_sphere(50, 16, 16, 0xCC0000);
const sphere3 = create_sphere(50, 16, 16, 0xCC0000);


// Move the Sphere back in Z so we
// can see it.
sphere.position.z = -1000;
sphere.position.x = 0;
sphere.position.y = 0;

sphere2.position.z = -1000;
sphere2.position.x = -200;
sphere2.position.y =  200;

sphere3.position.z = -1000;
sphere3.position.x = 300;
sphere3.position.y = 0;

const cylinder = connect_nodes(sphere, sphere2 );
const cylinder2 = connect_nodes(sphere, sphere3 );

// Finally, add the sphere to the scene.
scene.add(sphere);
scene.add(sphere2);
scene.add(sphere3);
scene.add(cylinder);
scene.add(cylinder2);
*/