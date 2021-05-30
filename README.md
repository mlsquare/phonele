# PhoneLe
Recommend the minimum device (phone) needed for Computer Vision Tasks


Usage:

Proide (User)
1. clean, background-free images of the objects, 
2. a model that does a task on the images. A model here is a function that accepts an image, outputs success/failure codes. Definition of success/failure is prerogative of the model
3. provide/select a set of adversatial conditions against which the model has to be tested.

Approach:

1. Take the objects, and compose a synthetic image with Photoshop-like effects. The photoshop effects should reflect the reality, desribed the user in (3) above
2. Run the user supplied model against the image. Record fail/pass
3. Do (1) and (2) for thousands of scenariors. Determine the boundary conditions in terms of the adversarial conditions
4. Map the adversarial conditions to a known list of device specs
5. Recommend the minimum Phone mode;l/make that works under those condtions


For Task-1 above, one could use GANs or use openCV image processing techniques, develop custom effects/filters. Or one could also apply GANS or take MNIST, COCO and other datasets and form a libary of images.

For (2), one needs to create/write a simulation engine that generates synthetic data with the desired tags. Almost like a GANs

For (3) One needs can run a decision tree or run a explainable AI technique

For (4) a small database of phones with model/make mapped to its specs is needed.
