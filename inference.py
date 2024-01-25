# import whatever your model needs
import json
import numpy as np
import torch.nn as nn

# define wheterver function you need to load your model.
def some_function(some_input):
    return 'some_output'

# define your model class
class model_name(nn.Module):
    init()
    eval()
    
    
# Here we need the four necessary functions to load our model, feed input, and return output.
# Note that you may not change the names of these functions:

# This is to load your model. Pay attention to your specific model name.
def model_fn(model_dir):
    model = model_name(pretrained_model=os.path.join(model_dir, "model.pt"))
    return model

# preprocess your input
def input_fn(request_body, request_content_type):
    print("Your request_content_type:", request_content_type)
    print("Your type(request_body):", type(request_body))
    
    try:
        jpg_original = np.load(io.BytesIO(request_body), allow_pickle=True)
        img = jpg_original.astype(np.float32)
        print("img.dtype:", img.dtype)
    except Exception as e:
        print(f"Error uploading to S3: {e}")

    return img

# call your model
def predict_fn(input_object, model):
    model_output = model.eval(input_object)
    return model_output

# return outout from endpoint
def output_fn(predictions, content_type):  
    print("my custom content should be ", content_type)
    data = {"model output": predictions}
    json_string = json.dumps(data)
    return json_string
