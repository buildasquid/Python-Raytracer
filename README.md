# Python-Raytracer

## Project Overview
This project is a simple yet powerful Ray Tracer implemented in Python. The program generates 3D scenes and renders them into 2D images using ray tracing techniques. This is a fundamental project in computer graphics, demonstrating key concepts such as lighting, shading, reflection, and material properties.

The project is designed to be educational, showcasing the basic principles behind rendering realistic images by simulating the behavior of light as it interacts with objects in a virtual environment.

##Features

-Basic Ray Tracing: Implementation of ray tracing to render 3D objects into 2D images.
-Materials and Shading: Supports different materials including diffuse and reflective surfaces, as well as a chequered material.
-Lighting Models: Implements basic lighting models including ambient, diffuse (Lambertian), and specular (Blinn-Phong) shading.
-Multiple Light Sources: Ability to handle multiple light sources with different colors and intensities.
-Scene Configuration: Scenes can be easily configured with different objects, materials, and lights.

##Structure

-main.py: The entry point of the application. Handles the setup and rendering of the scene.
-image.py: Manages the creation and saving of the rendered image.
-ray.py: Defines the Ray class, which represents a ray in 3D space.
-color.py: Defines the Color class, which handles color operations.
-point.py: Defines the Point class, representing a point in 3D space.
-vector.py: Defines the Vector class, representing vectors in 3D space.
-sphere.py: Implements the Sphere class, representing spherical objects in the scene.
-material.py: Defines different materials like diffuse and chequered materials.
-light.py: Implements the Light class, representing light sources in the scene.
-scene.txt: A sample scene file defining objects, lights, and camera position.
