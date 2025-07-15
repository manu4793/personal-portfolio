from django.db import models

class Game(models.Model):
    player_x = models.CharField(max_length=50, default="Player X")
    player_o = models.CharField(max_length=50, default="Player O")
    winner = models.CharField(max_length=10, choices=[('X', 'X'), ('O', 'O'), ('Tie', 'Tie')])
    board = models.JSONField()  # Store as array like ["X", "O", "", ...]
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_x} vs {self.player_o} - {self.winner}"
