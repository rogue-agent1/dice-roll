#!/usr/bin/env python3
"""dice_roll - Roll dice with standard notation (2d6+3, 4d8, d20)."""
import sys, re, random

def roll(notation):
    m = re.match(r'(\d*)d(\d+)([+-]\d+)?', notation.lower())
    if not m: return None, f"Invalid: {notation}"
    count = int(m.group(1) or 1)
    sides = int(m.group(2))
    mod = int(m.group(3) or 0)
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + mod
    return {'notation': notation, 'rolls': rolls, 'modifier': mod, 'total': total}, None

def main():
    args = sys.argv[1:]
    if not args or '-h' in args:
        print("Usage: dice_roll.py NOTATION [...]\n  dice_roll.py 2d6+3 d20 4d8-1"); return
    times = int(args[args.index('-n')+1]) if '-n' in args else 1
    notations = [a for a in args if not a.startswith('-') and a not in (str(times),)]
    for _ in range(times):
        for n in notations:
            result, err = roll(n)
            if err: print(f"  ❌ {err}"); continue
            rolls_str = ', '.join(map(str, result['rolls']))
            mod_str = f" {'+' if result['modifier']>=0 else ''}{result['modifier']}" if result['modifier'] else ''
            print(f"  🎲 {n}: [{rolls_str}]{mod_str} = {result['total']}")

if __name__ == '__main__': main()
