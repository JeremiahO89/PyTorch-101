import torch


x = torch.empty(3)
 # x.dtype is the same as the type peramitor
 
y = torch.random (2,2)
# y.size() prints the size so its a 2x2

z = torch.zeros(2,2)
u = torch.ones(2,2)
z.add_(u) # will add u's values to z
# any function with a trailing underscore will do an inplace function
#there are basic math functions available

data_lst = [1,2,3,4,5]
x = torch.tensor([data_lst])

