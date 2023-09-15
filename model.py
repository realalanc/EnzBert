from torch import nn

class BertClassifier(nn.Module):
    def __init__(self,dropout=0.5):
        super(BertClassifier,self).__init__()
        self.linear1=nn.Linear(1024,100)
        self.relu=nn.ReLU()
        self.linear2=nn.Linear(100,8) # Enzyme 1-7(following EC code) , 0 means not a enzyme
        self.softmax=nn.Softmax(dim=-1)

    def forward(self,x):
        x=self.linear1(x)
        x=self.relu(x)
        x=self.linear2(x)
        x=self.softmax(x)
        return x
