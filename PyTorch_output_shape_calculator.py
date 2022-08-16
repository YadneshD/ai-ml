

def Conv2d(h_in, w_in, in_channels, out_channels, kernel_size, batch_size=None,
            stride=(1,1), padding=(0,0), dilation=(1,1),name='Conv2d', verbose=True):
    if padding in ["same", "valid"]:
        padding = [1,1]
    h_out = (h_in+2*padding[0]-dilation[0]*(kernel_size[0]-1)-1)/stride[0] + 1
    w_out = (w_in+2*padding[1]-dilation[1]*(kernel_size[1]-1)-1)/stride[1] + 1
    output_shape = (batch_size, out_channels, h_out, w_out)
    if verbose:
        print('output shape of', name,'=',output_shape)
    return output_shape


print(Conv2d(h_in=120, w_in=480,in_channels=3, 
            out_channels=16, kernel_size=(3, 3), stride=(1, 1), dilation=(1,1), padding="same"))

