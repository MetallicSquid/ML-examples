# This directory is where we are going to put the classifier.

I'm thinking that we should write a basic neural network and train it on the MNIST handwritten digits dataset. I was also thinking it could be cool if we made a UI for the user to draw a digit on and it will

I think we should split the program into a few modules:

* build_model.py	-	module to gather the dataset and train the model on the training set.
* evaluate_accuracy.py	-	module to test the accuracy of the model on the test set.
* digit_ui.py		-	module for the user to draw a digit into.

We can then call these modules to get the final program working. We could put it all in one `.py` file, but I think it's nicer this way.

## Suggested order of things to do:
This is only suggested, so you can do what you want really
1. Ariel              	-   digit_ui.py
3. Guillaume		-   build_model.py
4. Guillaume / Ariel  	-   evaluate_accuracy.py

### What the UI needs to have:
This doesn't need to be too complicated. I was thinking you make this with PyGame. All it needs is:
- [ ] A 28x28 pixel, black and white canvas which the user can draw a number on.
- [ ] A button to clear the canvas.
- [ ] A button to run the model on the number that the user drew.
- [ ] We want this to return an 28x28 array of greyscale pixel values. **This doesn't have to be sorted out immediately, we'll probably sort this out at the end.**

### What the model training needs to do:
- [x] Gather the MNIST handwritten digits dataset.
- [x] Split the dataset up into training and test sets.
- [ ] Build a model on the prepared training dataset.

### What the accuracy evaluation needs to have.
- [ ] Test the model on the remaining test dataset.

## Notes:

The dataset prep was so easy that I'll probably merge it with the `train_model.py` script.

I have merged it, it is now called `build_model.py`.
