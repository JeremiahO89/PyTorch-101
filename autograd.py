import torch

x = torch.randn(3, requires_grad = True)
print(x)

y = x + 2
print(y)

z = y*y*2
z = z.mean()
print(z)

# to run the backward function z needs to be a scalar function
z.backward() # dz/dx
print(x.grad)

#when training the function you need to state the fallowing or else it going to change the gradents
# x.requires_grad_(False)
# x.detach()
# with torch.no_grad():
