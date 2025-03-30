from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    copies_available = models.IntegerField(
        default = 1,
        verbose_name="Доступные экземпляры"
    )
    loan_records = models.JSONField(
        default=list,
        verbose_name="История выдачи",
        help_text="Список дат в формате ['YYYY-MM-DD', ...]"
    )

    def is_available(self):
        return self.copies_available > 0
    def get_most_recent_loan(self):
        if not self.loan_records:
            return"Не выдалось"
        return max(self.loan_records)
    
    def __str__(self):
        return f"{self.title} (Автор: {self.author})"
