from pathlib import Path
import numpy as np
import pandas as pd
from statsmodels.api import OLS, add_constant
from statsmodels.tsa.stattools import coint, adfuller
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/raw/nifty50_prices.csv'; OUT=ROOT/'outputs'
PAIR=('HDFCBANK.NS','KOTAKBANK.NS')
SPLIT=pd.Timestamp('2023-08-04')
LOOKBACK=20; ENTRY=1.5; EXIT=0.5; COST=0.0005

def load():
 d=pd.read_csv(RAW).rename(columns={'Unnamed: 0':'Date'}); d['Date']=pd.to_datetime(d.Date); return d.set_index('Date').sort_index()

def positions(z):
 state=0; out=[]
 for v in z:
  if np.isnan(v): out.append(state); continue
  if state==0:
   if v>ENTRY: state=-1
   elif v<-ENTRY: state=1
  elif state==1 and v>-EXIT: state=0
  elif state==-1 and v<EXIT: state=0
  out.append(state)
 return pd.Series(out,index=z.index,dtype=float)

def main():
 d=load()[list(PAIR)].dropna(); train=d.loc[d.index<SPLIT]; test=d.loc[d.index>=SPLIT]
 fit=OLS(np.log(train[PAIR[0]]),add_constant(np.log(train[PAIR[1]]))).fit(); beta=float(fit.params.iloc[1]); alpha=float(fit.params.iloc[0])
 coint_p=float(coint(train[PAIR[0]],train[PAIR[1]])[1])
 spread=np.log(d[PAIR[0]])-beta*np.log(d[PAIR[1]])
 z=(spread-spread.rolling(LOOKBACK).mean())/spread.rolling(LOOKBACK).std()
 zt=z.loc[test.index]; pos=positions(zt)
 ra=test[PAIR[0]].pct_change(); rb=test[PAIR[1]].pct_change()
 gross=pos.shift(1).fillna(0)*(ra-beta*rb)/(1+abs(beta))
 turnover=pos.diff().abs().fillna(0); net=gross-COST*turnover
 equity=(1+net.fillna(0)).cumprod(); dd=equity/equity.cummax()-1
 years=(equity.index[-1]-equity.index[0]).days/365.25
 cagr=equity.iloc[-1]**(1/years)-1; vol=net.std(ddof=0)*np.sqrt(252); sharpe=net.mean()/net.std(ddof=0)*np.sqrt(252)
 downside=net[net<0].std(ddof=0); sortino=net.mean()/downside*np.sqrt(252)
 spread_train=(np.log(train[PAIR[0]])-beta*np.log(train[PAIR[1]])).dropna(); adf_p=float(adfuller(spread_train)[1])
 metrics={'pair':f'{PAIR[0]} / {PAIR[1]}','train_start':str(train.index[0].date()),'train_end':str(train.index[-1].date()),'test_start':str(test.index[0].date()),'test_end':str(test.index[-1].date()),'cointegration_p_value':coint_p,'adf_p_value':adf_p,'hedge_ratio_beta':beta,'lookback':LOOKBACK,'entry_z':ENTRY,'exit_z':EXIT,'transaction_cost':COST,'cagr':cagr,'annualized_volatility':vol,'sharpe':sharpe,'sortino':sortino,'max_drawdown':dd.min(),'final_equity':equity.iloc[-1],'position_changes':int((turnover>0).sum())}
 OUT.joinpath('tables').mkdir(parents=True,exist_ok=True); pd.DataFrame([metrics]).to_csv(OUT/'tables/case_study_metrics.csv',index=False)
 pd.DataFrame({'spread':spread.loc[test.index],'z_score':zt,'position':pos,'gross_return':gross,'net_return':net,'equity':equity,'drawdown':dd}).to_csv(OUT/'tables/case_study_timeseries.csv')
 plt.figure(figsize=(10,5)); plt.plot(equity.index,equity.values); plt.title('Out-of-Sample Equity Curve'); plt.xlabel('Date'); plt.ylabel('Equity'); plt.tight_layout(); plt.savefig(OUT/'plots/equity_curve.png',dpi=160); plt.close()
 plt.figure(figsize=(10,4)); plt.plot(zt.index,zt.values); plt.axhline(ENTRY,linestyle='--'); plt.axhline(-ENTRY,linestyle='--'); plt.axhline(0,linestyle=':'); plt.title('Rolling Spread Z-Score'); plt.xlabel('Date'); plt.ylabel('Z-score'); plt.tight_layout(); plt.savefig(OUT/'plots/z_score.png',dpi=160); plt.close()
 print(pd.Series(metrics))

if __name__=='__main__': main()
