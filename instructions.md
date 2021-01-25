# Machine Learning Engineer Home Assignment

**Make a simple web app for deep learning image classification.**

![](example.png)
_Example of an image classifier web app [(source)](https://medium.com/agara-labs/image-classification-with-the-client-side-neural-network-using-tensorflow-js-8f94d3dc7c5c)._

## Assignment
Choose three models from [Keras Applications](https://keras.io/applications/) and serve predictions with them in a web app where the user can upload a picture and get out the resulting predictions. The user should be able to choose which model they want to run.

## Ideas
We encourage you to focus on **one** specific aspect/feature within the task. Here are some potential ideas for inspiration:

- Provide stress testing capabilities where multiple predictions can be queued up or run concurrently. Benchmark the latency and throughput of the backend.
- Look into speeding up the forward pass with weight quantization or pruning. How much faster does it run? Is the quality of predictions maintained?
- Inspect the predictions with Grad-CAM or similar techniques. What limitations are there with respect to automatic differentiation and model serving?
- Run the model with a live webcam feed. How do you handle unstable connections? Do you drop frames or block and retry?
- Let the user choose to either run the models server-side or locally. What are the pros/cons of cloud vs edge computation respectively?

## Guidelines
- **The assignment should not take more than two evenings to finish.** You’re allowed to leave things out if you think the assignment will take too long, but make sure to document and motivate what parts you’ve left out.
- Either go for a cloud solution or local hardware. We are able to try out your solution either way as long as you provide setup instructions.
- A basic HTML form suffices (or feel free to modify [our example frontend](https://storage.googleapis.com/bucket-8732/demo/image-classifier/classifier.html)). Don't focus on making the frontend sleek. We are more interested in how you decide to run the models and how you connect them to the GUI.
- Choose whatever programming language and deep learning tooling you're most comfortable with to complete your assignment (e.g. it is absolutely fine to use torchvision instead of Keras).
- It's probably not a good idea to run an entire training framework in a Flask server.
- Rebasing is a good idea as we will likely use `git log` for getting around your work.
- In our evaluation we will look at readability and structure of your code. It is important that it is properly packaged with clear and complete install instructions.

## Deliverables
Git commit your work in a **private** repository, complete with setup instructions so we can install and test your deployment solution. Please also provide concise high-level thoughts on:

1. What you have done and why you chose the solution you did (pros/cons).
1. Which reading material you based your work on (if any).
1. What your future steps would be if you had more time.

Hand in your work by giving [github.com/dantekind](https://github.com/dantekind), [github.com/alvaro-garcia-carrasco](https://github.com/alvaro-garcia-carrasco) and [github.com/sg10](https://github.com/sg10) (read) access to your repository.

If we decide to continue to the next step, you will be invited to Peltarion's office to present your work for the team, together with a follow-up discussion.

## Questions
If you run into problems or have questions, don't hesitate to email daniel.lind@peltarion.com or alvaro@peltarion.com. Asking questions is a good thing.
