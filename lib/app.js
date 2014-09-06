requirejs.config({
  baseUrl: 'scripts',
  paths: {
    t3: [
      '../../dist/t3',
      'https://cdn.rawgit.com/maurizzzio/t3/gh-pages/dist/t3'
    ],
    three: [
      '../lib/three',
      'https://cdn.rawgit.com/maurizzzio/t3/gh-pages/examples/lib/three.min'
    ]
  }
});

/*define(['t3'], function (t3) {

  t3.themes.sandyStone = {
    clearColor: 0xE6E2AF,
    fogColor: 0xE6E2AF,
    groundColor: 0xA7A37E
  };

  return t3.run({
    id: 'canvas',
    theme: 'sandyStone',
    init: function () {
      var geometry = new THREE.BoxGeometry(20, 20, 20);
      var material = new THREE.MeshNormalMaterial();
      this.cube = new THREE.Mesh(geometry, material);
      this.cube.position.set(100, 100, 100);
      this.activeScene
        .add(this.cube);
    },
    update: function (delta) {
      this.cube.rotation.x += 0.01;
      this.cube.rotation.y += 0.01;
    }
  });
});*/
    // https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Sending_and_Receiving_Binary_Data
    function loadTerrain(file,scene, callback) {
        var req = new XMLHttpRequest();
        req.responseType = 'arraybuffer';
        req.open('GET', file, true);
        req.onload = function(evt) {
            if (req.response) {
                callback(new Uint16Array(req.response),scene);
            }
        };
        req.send(null);
    }


define(['t3'], function (t3) {
  return t3.run({
    id: 'canvas',
    init: function () {
      var geometry = new THREE.BoxGeometry(20, 20, 20);
      var material = new THREE.MeshNormalMaterial();
      this.cube = new THREE.Mesh(geometry, material);
      this.cube.position.set(100, 100, 100);
      // this.activeScene equals this.scenes.default
      this.activeScene
        .add(this.cube);

var scale = 200;
// x is east/red

var maxX = 150.9998611;
var minX = 147.9998611;
var unitX = (maxX - minX)/scale;
meshX = new THREE.Mesh( new THREE.SphereGeometry( 10, 16, 8 ), new THREE.MeshBasicMaterial( { color: 0xff0000 } ) );
meshX.position.x = 150;
//this.activeScene.add( meshX);

// y is north/green
var maxY = -33.0001389;
var minY = -36.0001389;
var unitY = (maxY - minY)/scale;
meshY = new THREE.Mesh( new THREE.SphereGeometry( 10, 16, 8 ), new THREE.MeshBasicMaterial( { color: 0x00ff00 } ) );
meshY.position.y = 150;
//this.activeScene.add( meshY );

var originX = 149.4998611
var originY = -34.5001389

// Z is depth/blue
var maxZ = 900;
var minZ = 600;

homeY = -35.24984
homeX = 149.13263
meshHome = new THREE.Mesh( new THREE.SphereGeometry( 10, 16, 8 ), new THREE.MeshBasicMaterial( { color: 0xff6600 } ) );
meshHome.position.x = (originX - homeX)/-unitX;
meshHome.position.y = (originY - homeY)/-unitY;
meshHome.position.z = 21
this.activeScene.add( meshHome );


    loadTerrain('../assets/canberra.bin',this.activeScene, function (data,scene){
        //console.log(data);

        var geometry = new THREE.PlaneGeometry(200, 200, 199, 199);
        geometry.computeFaceNormals();
        geometry.computeVertexNormals();

        for (var i = 0, l = geometry.vertices.length; i < l; i++) {
            geometry.vertices[i].z = data[i] / 65535 * 100;
        }

        var material = new THREE.MeshPhongMaterial({
            color: 0xdddddd, 
            wireframe: true
        });

        var plane = new THREE.Mesh(geometry, material);
        plane.castShadow = true;
        plane.receiveShadow = true;
        scene.add(plane);

});
},
    update: function (delta) {
      this.cube.rotation.x += 0.01;
      this.cube.rotation.y += 0.01;
    }
  });

}); 
