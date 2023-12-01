/*
* Version: 1.1.0
* Template: Hope-Ui Pro - Responsive Bootstrap 5 Admin Dashboard Template
* Author: iqonic.design
* Design and Developed by: iqonic.design
* NOTE: This file contains the script for initialize & listener Template.
*/

/*----------------------------------------------
Index Of Script
------------------------------------------------

------- Plugin Init --------

:: Three Js Setup

------------------------------------------------
Index Of Script
----------------------------------------------*/
"use strict";
const container = document.querySelector('#three-js-webgl')
const threeDProduct = container.getAttribute('data-path')
if (container !== null) {
    let camera
    let scene
    let render
    let product
    let controls
    function init() {
        scene = new THREE.Scene()
        const fov = 2.5
        const aspect = container.clientWidth / container.clientHeight
        const near = 1
        const far = 200

        camera = new THREE.PerspectiveCamera(fov, aspect, far, near)
        // const gui = new dat.GUI();
        camera.position.set(6, -4, 1)

        // const cam = gui.addFolder('Camera');
        // cam.add(camera.position, 'x', -3, 7);
        // cam.add(camera.position, 'y', -3, 3);
        // cam.add(camera.position, 'z', -3, 3);
        // cam.add(camera.rotation, 'x', -3, 3);
        // cam.add(camera.rotation, 'y', -3, 3);
        // cam.add(camera.rotation, 'z', -3, 3);


        const hemiLight = new THREE.HemisphereLight( 0xffffff, 0xffffff, 3 );
        hemiLight.position.set( 0, 50, 0 );
        scene.add( hemiLight );

        // const lt1 = gui.addFolder('HemiLight');
        // lt1.add(hemiLight.position, 'x', -50, 50);
        // lt1.add(hemiLight.position, 'y', -50, 50);
        // lt1.add(hemiLight.position, 'z', -50, 50);
        // lt1.add(hemiLight, 'intensity', 0, 3);

        const light = new THREE.DirectionalLight( 0xaabbff, 0.5 );
        light.position.x = 0;
        light.position.y = -7;
        light.position.z = 10;
        light.castShadow = true;
        light.shadow.mapSize.width = 500; // default
        light.shadow.mapSize.height = 500; // default
        light.shadow.camera.near = 1; // default
        light.shadow.camera.far = 500;
        scene.add( light );

        // const dt =  gui.addFolder('DirectionalLight');
        // dt.add(light.position, 'x', -50, 50);
        // dt.add(light.position, 'y', -50, 50);
        // dt.add(light.position, 'z', -50, 50);
        // dt.add(light, 'intensity', 0, 3);


        const leftlight = new THREE.DirectionalLight( 0xaabbff, 0.5 );
        leftlight.position.x = 0;
        leftlight.position.y = 7;
        leftlight.position.z = -10;
        leftlight.castShadow = true;
        leftlight.shadow.mapSize.width = 500; // default
        leftlight.shadow.mapSize.height = 500; // default
        leftlight.shadow.camera.near = 1; // default
        leftlight.shadow.camera.far = 500;
        scene.add( leftlight );

        // const ldt = gui.addFolder('LeftDirectionalLight');
        // ldt.add(leftlight.position, 'x', -50, 50);
        // ldt.add(leftlight.position, 'y', -50, 50);
        // ldt.add(leftlight.position, 'z', -50, 50);
        // ldt.add(leftlight, 'intensity', 0, 3);

        render = new THREE.WebGLRenderer({antialias: true, alpha: true})
        render.setSize(container.clientWidth, container.clientHeight)
        render.setPixelRatio(window.devicePixel)
        container.appendChild(render.domElement)
        let loader = new THREE.GLTFLoader()
        loader.load(threeDProduct, function (gltf) {
            scene.add(gltf.scene)
            product = gltf.scene.children[0]
            product.position.y = 0
            product.rotation.x = 0
            product.rotation.z = 0

            render.render(scene, camera)
            animate()
        })
        controls = new THREE.OrbitControls( camera, render.domElement );
        controls.target.set( 0, 0, 0 );
        controls.autoRotate = true;
        controls.dampingFactor = 0.5
        controls.autoRotateSpeed *= -2;
        // const orbitGui = gui.addFolder("Orbit Control");
        // orbitGui.add(controls.target, 'x', -5, 5);
        // orbitGui.add(controls.target, 'y', -5, 5);
        // orbitGui.add(controls.target, 'z', -5, 5);
        controls.enableZoom = false;
        window.addEventListener( 'resize',function(){

            const sizes = {}
            // Update sizes
            sizes.width = container.clientWidth
            sizes.height = container.clientHeight

            // Update camera
            camera.aspect = sizes.width / sizes.height
            camera.updateProjectionMatrix()

            // Update renderer
            render.setSize(sizes.width, sizes.height)
            render.setPixelRatio(Math.min(window.devicePixelRatio, 1))

        });
    }
    function animate() {
        window.requestAnimationFrame(animate)
        controls.update();
        render.render(scene, camera)
    }
    init()
}
