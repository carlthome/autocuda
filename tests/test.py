%load_ext autocuda
%autocuda

import torch
assert torch.cuda.is_available()
%env CUDA_VISIBLE_DEVICES
torch.cuda.device_count()
