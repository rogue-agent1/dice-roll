#!/usr/bin/env python3
"""dice_roll - Roll dice using D&D notation."""
import sys, re, random
def roll(expr):
    m = re.match(r"(\d+)?d(\d+)([+-]\d+)?", expr.lower())
    if not m: raise ValueError(f"Bad dice: {expr}")
    n, sides, mod = int(m[1] or 1), int(m[2]), int(m[3] or 0)
    rolls = [random.randint(1, sides) for _ in range(n)]
    total = sum(rolls) + mod
    return rolls, mod, total
if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: dice_roll <NdS+M> [NdS+M...]"); sys.exit(1)
    for expr in sys.argv[1:]:
        rolls, mod, total = roll(expr)
        mod_str = f" + {mod}" if mod > 0 else f" - {abs(mod)}" if mod < 0 else ""
        print(f"{expr}: {rolls}{mod_str} = {total}")
