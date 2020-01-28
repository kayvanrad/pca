
import matplotlib.pyplot as plt

def biplot(x,coeff, classes=None, var_names=None, show_loadings= True):
    xs = x[:,0]
    ys = x[:,1]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    colours = ['blue','red']
    if classes is not None:
        plt.scatter(xs * scalex,ys * scaley, c = classes, alpha=0.2, s=5,
                    cmap=matplotlib.colors.ListedColormap(colours))
    else:
        plt.scatter(xs * scalex,ys * scaley)
    n = coeff.shape[0]
    if show_loadings:
        for i in range(n):
            plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 1, width = 0.005, head_width=0.02)
            if var_names is None:
                plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'r', ha = 'center', va = 'center')
            else:
                plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, var_names[i], color = 'r', ha = 'center', va = 'center')

    plt.xlim(-1.25,1.25)
    plt.ylim(-1.25,1.25)
    plt.axhline()
    plt.axvline()
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))