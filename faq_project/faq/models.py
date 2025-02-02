from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field('Answer', config_name='extends')  # Use CKEditor 5
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = CKEditor5Field('Answer (Hindi)', config_name='extends', blank=True, null=True)
    answer_bn = CKEditor5Field('Answer (Bengali)', config_name='extends', blank=True, null=True)
    
    def __str__(self):
        return self.question

    def get_translated_text(self, field, lang):
        """Retrieve translated text dynamically."""
        if lang == 'en':
            return getattr(self, field)
        translated_field = f"{field}_{lang}"
        return getattr(self, translated_field) or getattr(self, field)

    def save(self, *args, **kwargs):
        """Automate translations during object creation."""
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)