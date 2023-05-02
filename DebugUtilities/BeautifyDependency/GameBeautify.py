import numpy as numpy

from DebugUtilities.BeautifyDependency.StringBeautify import print_by_padding, pad_str_list, bool_to_str
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.EncryptionDependency.MoveEncryptions.DecodeMove import decode_move_all

from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask

white_pieces_char = 'PNBRQK'
black_pieces_char = 'pnbrqk'


def print_bitboard(bit_board: int):
    bin_val = get_binary(bit_board)
    for i, file in zip(range(8), range(8, 0, -1)):
        print(file, end='\t')
        for j in range(8):
            print(bin_val[i * 8 + j], end='  ')
        print()
    print()
    print('\t', end='')
    for char in 'abcdefgh':
        print(char, end='  ')
    print()


def get_binary(number: int, start='', end='') -> str:
    return start + '{:064b}'.format(number) + end


def print_moves(move_list: list):
    if len(move_list) == 0:
        return
    str_length = 198
    print_by_padding('', str_length)
    print_by_padding('', str_length, start_end_only=True)
    print_by_padding('MOVES TABLE', str_length, start_end_only=True)
    print_by_padding('', str_length, start_end_only=True)
    print_by_padding('', str_length)
    print(pad_str_list(
        ['PIECE NAME', 'SOURCE SQ.', 'TARGET SQ.', 'DOUBLE PUSH', 'ENPASSANT', 'CAPTURE', 'CASTLE', 'PROMOTION PIECE',
         'MOVE NAME'],
        total_length=str_length))
    print_by_padding('', str_length)
    for move in move_list:
        piece_name, source_square, target_square, promotion_piece, capture, double_push, enpassant, castle = decode_move_all(
            move)
        print(pad_str_list(
            [piece_name.name, source_square.name, target_square.name, bool_to_str(double_push), bool_to_str(enpassant),
             bool_to_str(capture), bool_to_str(castle), promotion_piece.name, ''],
            str_length))
    print_by_padding('', str_length)


def print_game_board(white_state: int, white_pieces: list, black_state: int, black_pieces: list):
    white_pieces = numpy.array(white_pieces, dtype=numpy.uint64)
    black_pieces = numpy.array(black_pieces, dtype=numpy.uint64)

    for i, file in zip(range(8), range(8, 0, -1)):
        print(file, end='\t')
        for j in range(8):
            current_square_mask = square_bitmask[i * 8 + j]
            if current_square_mask & white_state:
                print(white_pieces_char[int((white_pieces & current_square_mask).nonzero()[0])], end='  ')
            elif current_square_mask & black_state:
                print(black_pieces_char[int((black_pieces & current_square_mask).nonzero()[0])], end='  ')
            else:
                print(' ', end='  ')
        print()
    print()
    print('\t', end='')
    for char in 'abcdefgh':
        print(char, end='  ')
    print()


def print_attack_map(attack_map: list):
    for position in reversed(list(Positions)[:-1]):
        print(f'\'{position.name}\':')
        binary = get_binary(attack_map[position.value])
        print('\'\'\'')
        for index, bit in enumerate(binary):
            if index != 0 and index % 8 == 0:
                print()
            print(bit, end=' ')
        print()
        print('\'\'\',')
