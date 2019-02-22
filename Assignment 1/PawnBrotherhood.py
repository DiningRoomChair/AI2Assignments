def safe_pawns(pawns: set) -> int:
    safe_count = 0
    for pawn in pawns:
        safepos1 = chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1)
        safepos2 = chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1)
        if safepos1 in pawns or safepos2 in pawns:
            safe_count += 1
            continue
    return safe_count

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))  # == 6
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))  # == 1
