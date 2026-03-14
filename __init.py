import torch
import torch.nn as nn

class BinaryActivation(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        # Convert to +1 or -1
        return torch.sign(input)

    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        # Hard-tanh gradient: help the model learn near the boundary
        grad_input = grad_output.clone()
        grad_input[input.abs() > 1.0] = 0
        return grad_input

class XNORLinear(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_features, in_features))

    def forward(self, x):
        # 1. Binarize weights and inputs
        binary_w = BinaryActivation.apply(self.weight)
        binary_x = BinaryActivation.apply(x)
        
        # 2. In software, we use standard matmul (it mimics XNOR-Popcount)
        # In actual hardware (FPGA/ASIC), this would be XNOR + Popcount
        return torch.matmul(binary_x, binary_w.t())
