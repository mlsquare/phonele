# phonele
Recommend the minimum device (phone) needed for Computer Vision Tasks


Usage:
Supply clean, background-free images of the objects, a model that does a task on the images, and provide/select a set of adversatial conditions against which the model has to be tested.

Configuration:
Data: objects that need to be detected in the Application. These objects should be seperated from the background

Model: A model/function that accepts an Images, outputs success/failure codes. Definition of success/failure is preragative of the model

Data Augmentations:
Field conditions that need to be tested. For example:
Images with funcky background, extreme light conditions, de-focussed etc. Any field conditions that are likely to make the Application fail against a device
Camera resolution is an important parameter. One could be downsampling to render a low-res image for testing low-end phones.


Output:
A list of phone specs that work and that dont work
