from figure import Figure

class Pawn(Figure):    
    def move(self):
        x, y = self.current_field
        y = int(y)
        if y > 8:
            return False
        elif y == 2:
            y +=2
        else:
            y += 1
        return x + str(y)    

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


p = Pawn('A2')
print(p.move())