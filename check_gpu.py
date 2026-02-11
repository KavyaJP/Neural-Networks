import torch

print("CUDA available:", torch.cuda.is_available())
print("Device count:", torch.cuda.device_count())
print("Device name:", torch.cuda.get_device_name(0))

x = torch.randn(5000, 5000, device="cuda")
y = torch.randn(5000, 5000, device="cuda")
z = x @ y
print("Success")
