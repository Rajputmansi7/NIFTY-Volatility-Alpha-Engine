import numpy as np

def metrics(ret):
    ret=np.array(ret)
    eq=(1+ret).cumprod()
    cagr=eq[-1]**(252/len(ret))-1
    sharpe=np.mean(ret)/np.std(ret)*np.sqrt(252)
    dd=eq/np.maximum.accumulate(eq)-1
    maxdd=dd.min()
    sortino=np.mean(ret)/np.std(np.minimum(ret,0))*np.sqrt(252)
    return {
        'CAGR':float(cagr),
        'Sharpe':float(sharpe),
        'Sortino':float(sortino),
        'MaxDrawdown':float(maxdd)
    }