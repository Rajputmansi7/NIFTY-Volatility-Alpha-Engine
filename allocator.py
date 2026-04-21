def choose_strategy(row):
    if row['iv_rank']<0.2 and row['forecast_vol_up']==1:
        return 'LONG_STRADDLE'
    if row['iv_rank']>0.8 and row['range_prob']>0.6:
        return 'IRON_CONDOR'
    if row['trend_up']==1:
        return 'BULL_CALL_SPREAD'
    if row['trend_down']==1:
        return 'BEAR_PUT_SPREAD'
    return 'NO_TRADE'