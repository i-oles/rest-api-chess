from unittest import TestCase

class PawnTest(TestCase):
    def test_pawn_create(self):
        pawn = Pawn('H5')
        self.assertEqual(pawn.current_field, 'H5')