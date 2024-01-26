# Deploying PyTorch Models on Amazon SageMaker - A Guide

Hello there! 👋

If you've ever struggled with deploying a PyTorch model on Amazon SageMaker, you're not alone. I faced challenges, fought server mysteries, and scoured AWS for working examples. Recently, I tried deploying a custom PyTorch model on Amazon SageMaker but encountered challenges. Despite following AWS examples, I faced server issues I couldn't comprehend. I struggled to find working code for a simple start and had no one to ask for help. :( \
But fear not, for I conquered, and now I share my journey with you. I hope this helps beginners aiming to do the same, reducing time and effort.

## Quick Start:

Start by reading and following these three links. They are sufficient to grasp what you need to know and do: \
&emsp;        1. [Hosting YOLOv8 on Amazon SageMaker Endpoints](https://aws.amazon.com/blogs/machine-learning/hosting-yolov8-pytorch-model-on-amazon-sagemaker-endpoints/) \
&emsp;        2. [Getting Started with PyTorch on SageMaker](https://sagemaker-examples.readthedocs.io/en/latest/frameworks/pytorch/get_started_mnist_deploy.html) \
&emsp;        3. [Deploy a Custom ML Model as a SageMaker Endpoint](https://towardsdatascience.com/deploy-a-custom-ml-model-as-a-sagemaker-endpoint-6d2540226428) \

After carefully reading them, now it's time to **explore my simple example to deploy your model, and do not forget the inference code!** Feel free to adapt them. \
Note: My model.pt is an empty file; it's a secret! 🤫

## Library Requirements:

Pay attention to the requirements.txt file. Some tutorials miss this! List the libraries your code needs. Watch out for versions - another crucial aspect is ensuring compatibility between library versions, as well as with Python and PyTorch versions.

## Final Step - Tar and Upload:

Prepare a compressed file (model.tar.gz) with this structure:

model.tar.gz \
├─ code/ \
 │&emsp;├── inference.py \
 │&emsp;└── requirements.txt \
└── model.pt

Upload this to your S3 bucket.

I hope this helps! If you have questions, feel free to ask. Happy coding! 🚀🌟
