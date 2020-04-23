# This directory is where we are going to put the classifier.

I'm thinking that we should write a basic neural network and train it on the MNIST handwritten digits dataset. I was also thinking it could be cool if we made a UI for the user to draw a digit on and it will

I think we should split the program into a few modules:

* dataset_prep.py	-	module to import the dataset, then split it into training and test.
* train_model.py	-	module to train the model on the training set.
* evaluate_accuracy.py	-	module to test the accuracy of the model on the test set.
* digit_ui.py		-	module for the user to draw a digit into.

We can then call these modules to get the final program working. We could put it all in one `.py` file, but I think it's nicer this way.

## Suggested order of things to do:
This is only suggested, so you can do what you want really
1. Ariel              -   digit_ui.py
2. Guillaume          -   dataset_prep.py
3. Guillaume / Ariel  -   train_model.py
4. Guillaume / Ariel  -   evaluate_accuracy.py

### What the UI needs to have:
This doesn't need to be too complicated. I was thinking you make this with PyGame. All it needs is:
- [ ] A 28x28 pixel, black and white canvas which the user can draw a number on.
- [ ] A button to clear the canvas.
- [ ] A button to run the model on the number that the user drew.
- [ ] We want this to return an 28x28 array of greyscale pixel values. **This doesn't have to be sorted out immediately, we'll probably sort this out at the end.**

### What the dataset preparation needs to do:
- [ ] Import the MNIST handwritten digits dataset.
- [ ] Split the dataset into training and test sets (70%, 30%).

### What the model training needs to do:
- [ ] Build a model on the prepared training dataset.

### What the accuracy evaluation needs to have.
- [ ] Test the model on the remaining test dataset.
