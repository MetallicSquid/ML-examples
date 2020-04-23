# This directory is where we are going to put the classifier.

I'm thinking that we should write a basic neural network and train it on the MNIST handwritten digits dataset. I was also thinking it could be cool if we made a UI for the user to draw a digit on and it will

I think we should split the program into a few modules:

* dataset_prep.py	-	module to import the dataset, then split it into training and test.
* train_model.py	-	module to train the model on the training set.
* evaluate_accuracy.py	-	module to test the accuracy of the model on the test set.
* digit_ui.py		-	module for the user to draw a digit into.

We can then call these modules to get the final program working. We could put it all in one `.py` file, but I think it's nicer this way.


