# Fast.ai Assignment Solutions

Jeremy Howard and Rachhel Thomas teaches **practical deep learning** at [fast.ai](http://course.fast.ai/). The course aims a practical learning process rather than covering theoretical concepts from ground-up. Therefore includes lots of practical tips and i think this is highly useful for anybody who wants to dive into details (even if ones with the knowledge of linear algebra, statistics, machine learning, some deep learning, etc).

## Lesson 01 - Recognizing Cats and Dogs

This lesson includes tools and tricks for machine learning people. Dives into the kaggle competition named [cats and dogs redux](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition) in order to cover classification and transfer learning (by fine tuning the imagenet model vgg16). Jeremy also tells about making deep learning inclusive by making neural networks uncool again! In conclusion, we are in the club, thank you for that!

solutions for lesson 01 are [here](./assignment-lesson-01.ipynb) and [here](./assignment-lesson-01-v02.ipynb).

## Lesson 02 - Convolutional Neural Networks

Lesson 2, covers convolutional neural networks and visualization of convolutional layers to show why transfer learning is applicable. solutions are [here](./assignment-lesson-02.ipynb).

### Suggested papers for lesson 02

Papers suggested in the lession plus additional ones.

#### Transfer learning

* [M. D. Zeiler, R. Fergus, "Visualizing and Understanding Convolutional Networks", arXiv, 2013.](https://arxiv.org/abs/1311.2901)
* [Jason Yosinski, Jeff Clune, Yoshua Bengio, Hod Lipson, "How transferable are features in deep neural networks?", arXiv, 2014.](https://arxiv.org/abs/1411.1792)

## Lesson 03 - Overfitting and Underfitting

This lesson covers the details of overfitting and underfitting, dropout is not used to avoid the underfitting and, after that, data augmentation techniques are applied to avoid overfitting. Batch normalization is covered.

I have implemented the bottleneck feature saving process [here](./assignment-lesson-03.ipynb), However it is only a demonstration with the sample set. Bottleneck features for the train set is about 2GB in size, even with 8gb GPUs of amazon i wasing able to fit the feature arrays in memory to save. Now i am using 1080 ti but i skipped the feature saving step and fine tuned the dense layers by just *freezing* the conv layers which is implemented [here](./assignment-lesson-03-v02.ipynb).

### Suggested papers for lesson 03

* [S. Ioffe, C. Szegedy, "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift", arXiv, 2015.](https://arxiv.org/abs/1502.03167)