from itertools import chain


def sep(*vals: int) -> str:
    return ";".join(str(v) for v in vals)


def sgr(*vals: int) -> str:
    return f"\x1b[{sep(*vals)}m"


RESET = sgr(0)

nms1 = ["BLA", "RED", "GRE", "YEL", "BLU", "MAG", "CYA", "WHI", "DEF"]
nms2 = ["L-BLA", "L-RED", "L-GRE", "L-YEL", "L-BLU", "L-MAG", "L-CYA", "L-WHI"]


FALIGN = ">6"
PAD = 6
ALIGN = f"<{PAD}"
LINE = "―" * ((((PAD + 2) * 9) - 1))


def main():

    print(RESET)

    print(f"{"fg╲bg":{FALIGN}} ", end="")
    for nm in nms1:
        print(f" {nm:{ALIGN}}  ", end="")
    print()

    it = iter(chain(nms1, nms2))
    for fv in chain(range(30, 38), [39]):
        print(f"{next(it):{FALIGN}} ", end="")
        for bv in chain(range(40, 48), [49]):
            print(f"{sgr(fv,bv)} {sep(fv,bv):{ALIGN}} {RESET} ", end="")
        print()

    for fv in range(90, 98):
        print(f"{next(it):>6} ", end="")
        for bv in chain(range(40, 48), [49]):
            print(f"{sgr(fv,bv)} {sep(fv,bv):{ALIGN}} {RESET} ", end="")
        print()

    print(f"{" " * (6 + 1)}{LINE}")

    it = iter(chain(nms1, nms2))
    for fv in chain(range(30, 38), [39]):
        print(f"{next(it):{FALIGN}} ", end="")
        for bv in range(100, 108):
            print(f"{sgr(fv,bv)} {sep(fv,bv):{ALIGN}} {RESET} ", end="")
        print()

    for fv in range(90, 98):
        print(f"{next(it):{FALIGN}} ", end="")
        for bv in range(100, 108):
            print(f"{sgr(fv,bv)} {sep(fv,bv):{ALIGN}} {RESET} ", end="")
        print()

    print(f"{"fg╱bg":{FALIGN}} ", end="")
    for nm in nms2:
        print(f" {nm:{ALIGN}}  ", end="")
    print("\n")


if __name__ == "__main__":
    raise SystemExit(main())
