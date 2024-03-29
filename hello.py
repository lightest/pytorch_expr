from __future__ import print_function
import torch
import numpy as np

x = torch.tensor([5.5, 3]);
print(x);

x = x.new_ones(5, 3, dtype=torch.double)
print(x);

x = torch.randn_like(x, dtype=torch.float);
print(x);
print(x.size());
y = torch.rand(5, 3)
print(x + y)
print(torch.add(x, y))
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

y.add_(x)
print(y);
print(x[:, 1])
x = torch.randn(4, 4)
y = x.view(16)
print("x.view(16)", y);
z = x.view(-1, 8);
print("x.view(-1, 8)", z);
print(x.size(),  y.size(), z.size())

x = torch.randn(1);
print(x);
print(x.item());

#============ NymPy brdg ============
print('\n#============ NymPy brdg ============');
a = torch.ones(5);
print(a, "// tensor");
b = a.numpy();
print(b, '// numpy arr');
a.add_(1);
print(a, b, '// values change sync');
a = np.ones(5);
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a, b);

print('checking if cuda is available...')
if torch.cuda.is_available():
  print('generating tenzors on cuda...')
  device = torch.device('cuda')
  y = torch.ones_like(x, device='cuda')
  x = x.to('cuda')
  z = x + y
  print(x, y, z)
  print(z.to('cpu', torch.double))
