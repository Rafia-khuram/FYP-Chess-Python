from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName

white_test_data = {
    '3k4/8/8/3Pp3/8/8/8/4K3 w - e6 0 3': [
        {
            'SOURCE_SQUARE': Positions.d5,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d5,
            'TARGET_SQUARE': Positions.e6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': True,
            'CASTLE_FLAG': False,
        },

        
    ],
     '3k4/8/8/8/8/8/P7/4K3 w - - 0 3': [
        {
            'SOURCE_SQUARE': Positions.a2,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a2,
            'TARGET_SQUARE': Positions.a4,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': True,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        
    ],
     '3k4/8/8/8/8/5p2/4PP2/4K3 w - - 0 2': [
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': True,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        
    ],
      '3k4/5P2/8/8/8/8/8/4K3 w - - 0 2': [
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.BISHOP,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.KNIGHT,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.QUEEN,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.ROOK,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        
    ],

        '3k4/8/8/8/1p6/p7/PP6/4K3 w - - 0 3': [
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.b3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        }
    ],

         '3k4/8/8/3Pp3/8/8/8/4K3 w - - 0 3': [
        {
            'SOURCE_SQUARE': Positions.d5,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        }
    ],

}

black_test_data = {
    '4k3/6p1/8/8/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.g7,
            'TARGET_SQUARE': Positions.g6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g7,
            'TARGET_SQUARE': Positions.g5,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': True,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        
    ],
     '4k3/8/6p1/5P2/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.g6,
            'TARGET_SQUARE': Positions.g5,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g6,
            'TARGET_SQUARE': Positions.f5,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        
    ],
     '4k3/8/8/8/3Pp3/8/8/4K3 b - d3 0 2': [
        {
            'SOURCE_SQUARE': Positions.e4,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e4,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': True,
            'CASTLE_FLAG': False,
        },
        
    ],
     '4k3/8/8/8/8/8/2p5/4K3 b - - 0 2': [
        {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.BISHOP,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.KNIGHT,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.QUEEN,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.ROOK,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
 
    ],
     '4k3/8/8/8/4Pp2/8/2p5/2P1K3 b - - 0 2': [
        {
            'SOURCE_SQUARE': Positions.f4,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    
    ],

   

}

