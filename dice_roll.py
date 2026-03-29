#!/usr/bin/env python3
"""dice_roll - Dice roller."""
import sys,argparse,json,random,re
from collections import Counter
def roll(notation):
    m=re.match(r"(\d*)d(\d+)([+-]\d+)?",notation)
    if not m:return [int(notation)],0
    count=int(m.group(1) or 1);sides=int(m.group(2));mod=int(m.group(3) or 0)
    rolls=[random.randint(1,sides) for _ in range(count)]
    return rolls,mod
def main():
    p=argparse.ArgumentParser(description="Dice roller")
    p.add_argument("dice",nargs="+",help="Dice notation (e.g. 2d6+3)")
    p.add_argument("-n","--times",type=int,default=1)
    p.add_argument("--stats",action="store_true")
    args=p.parse_args()
    all_results=[]
    for _ in range(args.times):
        total=0;details=[]
        for d in args.dice:
            rolls,mod=roll(d)
            s=sum(rolls)+mod;total+=s
            details.append({"dice":d,"rolls":rolls,"modifier":mod,"subtotal":s})
        all_results.append({"total":total,"details":details})
    if args.stats and args.times>1:
        totals=[r["total"] for r in all_results]
        freq=Counter(totals)
        print(json.dumps({"rolls":args.times,"min":min(totals),"max":max(totals),"mean":round(sum(totals)/len(totals),2),"distribution":dict(sorted(freq.items()))}))
    else:
        print(json.dumps(all_results[0] if args.times==1 else {"results":all_results[:20]},indent=2))
if __name__=="__main__":main()
