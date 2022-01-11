import Pawn as pw
import PawnCaptureImplementation as pwci

pawnCapture = dict()
for k in pw.PawnType:
    pawnCapture[k] = list()

pawnCapture[pw.PawnType.HORIZONTAL].append((pwci.is_horizontal_pawn_capture, pwci.horizontal_pawn_capture))
pawnCapture[pw.PawnType.DIAGONAL].append((pwci.is_diagonal_pawn_capture, pwci.diagonal_pawn_capture))
pawnCapture[pw.PawnType.ROYAL].append((pwci.is_royal_pawn_capture, pwci.royal_pawn_capture))