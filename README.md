# Python-Raytracer

## Project Overview
This project is a simple yet powerful Ray Tracer implemented in Python. The program generates 3D scenes and renders them into 2D images using ray tracing techniques. This is a fundamental project in computer graphics, demonstrating key concepts such as lighting, shading, reflection, and material properties.

This project is, more than anything, an attempt to understand raytracing and how it works, as well as get more accustomed to python programming. I am passionate about 3D modeling, but until now I haven't paid much attention to the inner workings of rendering images.

Hence, the project is designed to be educational, showcasing the basic principles behind rendering realistic images by simulating the behavior of light as it interacts with objects.

## Features

- Ray Tracing Algorithm: A basic ray tracing algorithm capable of rendering scenes with multiple light sources, reflective materials, and realistic shading.
- Scene Description File: The ability to define custom scenes in separate files, which are then loaded and rendered by the main program.
- Phong Shading: Supports ambient, diffuse, and specular lighting using the Phong shading model for realistic lighting effects.
- Chequered Material: Includes a chequered pattern material that provides a textured appearance based on the object's surface.
- Recursive Reflection: Handles reflections by recursively tracing rays for reflective surfaces, adding realism to the rendered scenes.
- Testing Suite: A set of unit tests to ensure the correctness of the Vector class, which is fundamental to the ray tracing calculations.


## Structure

- color.py: Defines the Color class, representing RGB colors and supporting operations like addition, multiplication, and conversion from hexadecimal.
- engine.py: Contains the RenderEngine class, which handles the rendering process, including ray tracing, light calculations, and recursive reflections.
- image.py: Implements the Image class, responsible for creating and manipulating the final image, setting pixel colors, and saving the image to a file.
- light.py: Defines the Light class, representing point light sources in the scene and their properties.
- main.py: The entry point of the application. Loads a scene from a specified file and triggers the rendering process using the RenderEngine.
- material.py: Contains the Material and ChequeredMaterial classes, which define surface properties of objects, such as color, reflection, and texture patterns.
- point.py: Implements the Point class, representing 3D points in space, used extensively in ray-object intersection calculations.
- ray.py: Defines the Ray class, representing a ray with an origin and direction, essential for tracing the path of light through the scene.
- scene.py: Contains the Scene class, which manages the collection of objects, lights, and the camera within the 3D environment.
- sphere.py: Implements the Sphere class, representing spherical objects in the scene, including methods for determining ray-sphere intersections.
- tests.py: A test suite for validating the functionality of the Vector class, ensuring correctness in vector operations used throughout the project.
- vector.py: Defines the Vector class, which handles 3D vector operations, such as addition, subtraction, dot product, cross product, and normalization.


## Render Engine
The RenderEngine class, located in engine.py, is the core component responsible for:

- Rendering Process: Iterates over each pixel in the image, shooting rays into the scene to determine the color based on intersections with objects and lighting.
- Ray Tracing: Traces rays from the camera through each pixel, calculates intersections with objects, and determines the final color using the Phong shading model.
- Recursive Reflections: Handles reflective surfaces by recursively tracing rays to simulate reflections, contributing to the realism of the rendered image.
- Lighting Calculations: Calculates the effect of light sources on the color of objects, including ambient, diffuse, and specular reflections.

## Usage
1. Scene Setup: Create a scene description file specifying the camera, objects, lights, and their properties.
2. Running the Project: Use the following command to render a scene:
   ```python main.py foldername.filename```
   Since my scene files were inside a folder called "examples" that was inside my project folder, i ran the command
   ```python main.py examples.trafficlight```
4. Output: The rendered image will be saved in the specified format (e.g., PPM) in the project directory.

## Example output
### Output for the file "6spheres.py"
![image](https://github.com/user-attachments/assets/b028c139-35f7-49b4-a01e-ebe25639fecf)
### Output for the file "trafficlight.py"
![image](https://github.com/user-attachments/assets/ebbb1177-aa7c-4e37-a923-33aaf068124d)

## Future Modifications / Enhancements
- Support for More Shapes: Adding support for additional geometric shapes such as planes(currently planes are represented by very large spheres), triangles, or other meshes.
- Advanced Materials: Implementing more complex materials like glass (refraction) and metals.
- Shadows and Anti-aliasing: Adding shadow rays for realistic lighting and anti-aliasing to reduce jagged edges.
- Other Materials: Experimenting more with texture and patterns

## Tools
Since the rendered images are .ppm format, i used IrfanView to view the rendered images

### License
This project is open source and available under the MIT License

