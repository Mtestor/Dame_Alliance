import Pawn as pw
import PawnMovePredicatImplementation as pwmpi

pawnMovePredicat = dict()
for k in pw.PawnType:
    pawnMovePredicat[k] = list()

pawnMovePredicat[pw.PawnType.HORIZONTAL].append(pwmpi.is_horizontal_pawn_deplacement)
pawnMovePredicat[pw.PawnType.DIAGONAL].append(pwmpi.is_diagonal_pawn_deplacement)
pawnMovePredicat[pw.PawnType.ROYAL].append(pwmpi.is_royal_pawn_deplacement)